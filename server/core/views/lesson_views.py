from django.shortcuts import render

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from core.models import Lesson, Course, Quiz, Answer
from core.serializers import CourseDetailSerialize, LessonDetailSerializer, LessonSerialize

from rest_framework import status

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getLessonByCourse(request, pk):
    lessons = Lesson.objects.filter(course=pk)

    serializer = LessonSerialize(lessons, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getDetailLesson(request, pk):
    lesson = Lesson.objects.get(_id=pk)

    serializer = LessonDetailSerializer(lesson, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def answerForQuiz(request, pk):
    answer = Answer.objects.get(_id=pk)

    if answer.isCorrect == False:
        return Response('Answer wrong')
    else:
        return Response('Answer right')

# Admin