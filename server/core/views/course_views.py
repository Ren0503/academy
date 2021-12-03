from django.shortcuts import render

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from core.models import Certificate, Course, Enroll, Review, Lesson, Quiz, Answer
from core.serializers import CertificateSerialize, CourseDetailSerialize, CourseSerialize, EnrollSerialize

from rest_framework import status

# Guest


@api_view(['GET'])
def getCourses(request):
    query = request.query_params.get('keyword')
    if query == None:
        query = ''

    courses = Course.objects.filter(
        name__icontains=query).order_by('-createdAt')

    page = request.query_params.get('page')
    paginator = Paginator(courses, 5)

    try:
        courses = paginator.page(page)
    except PageNotAnInteger:
        courses = paginator.page(1)
    except EmptyPage:
        courses = paginator.page(paginator.num_pages)

    if page == None:
        page = 1

    page = int(page)
    print('Page:', page)
    serializer = CourseSerialize(courses, many=True)
    return Response({'products': serializer.data, 'page': page, 'pages': paginator.num_pages})


@api_view(['GET'])
def getTopCourses(request):
    courses = Course.objects.filter(rating__gte=4).order_by('-rating')[0:5]
    serializer = CourseSerialize(courses, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getCourse(request, pk):
    course = Course.objects.get(_id=pk)
    serializer = CourseDetailSerialize(course, many=False)
    return Response(serializer.data)

# User


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createCourseReview(request, pk):
    user = request.user
    course = Course.objects.get(_id=pk)
    data = request.data

    # 1 - Review already exists
    alreadyExists = course.review_set.filter(user=user).exists()
    if alreadyExists:
        content = {'detail': 'Course already reviewed'}
        return Response(content, status=status.HTTP_400_BAD_REQUEST)

    # 2 - No Rating or 0
    elif data['rating'] == 0:
        content = {'detail': 'Please select a rating'}
        return Response(content, status=status.HTTP_400_BAD_REQUEST)

    # 3 - Create review
    else:
        review = Review.objects.create(
            user=user,
            course=course,
            name=user.first_name,
            rating=data['rating'],
            comment=data['comment'],
        )

        reviews = course.review_set.all()
        course.numReviews = len(reviews)

        total = 0
        for i in reviews:
            total += i.rating

        course.rating = total / len(reviews)
        course.save()

        return Response('Review Added')


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def enrollCourse(request, pk):
    user = request.user
    course = Course.objects.get(_id=pk)

    alreadyEnroll = Enroll.objects.filter(user=user, course=course).exists()
    if alreadyEnroll:
        content = {'detail': 'You were enroll course'}
        return Response(content, status=status.HTTP_400_BAD_REQUEST)

    else:
        enroll = Enroll.objects.create(
            user=user,
            course=course,
            status='Pending',
        )

        serializer = EnrollSerialize(enroll, many=False)
        return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def certificateCourse(request, pk):
    user = request.user
    course = Course.objects.get(_id=pk)

    alreadyCertificate = Certificate.objects.filter(user=user, course=course).exists()
    if alreadyCertificate:
        content = {'detail': 'You were certificate course'}
        return Response(content, status=status.HTTP_400_BAD_REQUEST)

    else:
        textCer = "This certificate is proudly presented to " + user.name + ", for outstanding results of courses" + course.name

        certificate = Certificate.objects.create(
            user=user,
            course=course,
            text=textCer,
        )

        serializer = CertificateSerialize(certificate, many=False)
        return Response(serializer.data)
