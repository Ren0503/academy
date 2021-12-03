from django.shortcuts import render

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from core.models import Course, Review, Lesson, Quiz, Answer
from core.serializers import CourseSerialize, CourseSerializeWithLesson

from rest_framework import status


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
