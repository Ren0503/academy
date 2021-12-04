from django.shortcuts import render

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from core.models import Lesson, Course, Quiz, Answer
from core.serializers import AnswerSerialize, LessonDetailSerializer, LessonSerialize, QuizSerialize

from rest_framework import status

# ----------------------------
# User
# ----------------------------


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getLessonsByCourse(request, pk):
    try:
        lessons = Lesson.objects.filter(course=pk)

        serializer = LessonSerialize(lessons, many=True)
        return Response(serializer.data)
    except Exception as e:
        return Response({'details': f"{e}"}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getDetailLesson(request, pk):
    try:
        lesson = Lesson.objects.get(_id=pk)

        serializer = LessonDetailSerializer(lesson, many=False)
        return Response(serializer.data)
    except Exception as e:
        return Response({'details': f"{e}"}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def answerForQuiz(request, pk):
    try:
        answer = Answer.objects.get(_id=pk)

        if answer.isCorrect == False:
            return Response('Answer wrong')
        else:
            return Response('Answer right')
    except Exception as e:
        return Response({'details': f"{e}"}, status=status.HTTP_204_NO_CONTENT)


# ----------------------------
# Admin - Lesson
# ----------------------------


@api_view(['POST'])
@permission_classes([IsAdminUser])
def createLesson(request, pk):
    user = request.user
    course = Course.objects.get(_id=pk)

    lesson = Lesson.objects.create(
        user=user,
        course=course,
        name='Sample Name',
        unit=0,
        content='Sample Content',
    )

    serializer = LessonSerialize(lesson, many=False)
    return Response(serializer.data)


@api_view(['PUT'])
@permission_classes([IsAdminUser])
def updateLesson(request, pk):
    try:
        data = request.data
        lesson = Lesson.objects.get(_id=pk)

        lesson.course = data['course']
        lesson.name = data['name']
        lesson.unit = data['unit']
        lesson.content = data['content']

        lesson.save()

        serializer = LessonSerialize(lesson, many=False)
        return Response(serializer.data)
    except Exception as e:
        return Response({'details': f"{e}"}, status=status.HTTP_204_NO_CONTENT)


@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def deleteLesson(request, pk):
    try:
        lesson = Lesson.objects.get(_id=pk)
        lesson.delete()
        return Response('Lesson Deleted')
    except Exception as e:
        return Response({'details': f"{e}"}, status=status.HTTP_204_NO_CONTENT)


# ----------------------------
# Admin - Quiz
# ----------------------------


@api_view(['POST'])
@permission_classes([IsAdminUser])
def createQuiz(request, pk):
    user = request.user
    lesson = Lesson.objects.get(_id=pk)

    quiz = Quiz.objects.create(
        user=user,
        lesson=lesson,
        question='Sample question',
        numAnswer=0,
    )

    serializer = QuizSerialize(quiz, many=False)
    return Response(serializer.data)


@api_view(['PUT'])
@permission_classes([IsAdminUser])
def updateQuiz(request, pk):
    try:
        data = request.data
        quiz = Quiz.objects.get(_id=pk)

        quiz.lesson = data['lesson']
        quiz.question = data['question']
        quiz.numAnswer = data['numAnswer']

        quiz.save()

        serializer = QuizSerialize(quiz, many=False)
        return Response(serializer.data)
    except Exception as e:
        return Response({'details': f"{e}"}, status=status.HTTP_204_NO_CONTENT)


@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def deleteQuiz(request, pk):
    try:
        quiz = Quiz.objects.get(_id=pk)
        quiz.delete()
        return Response('Quiz Deleted')
    except Exception as e:
        return Response({'details': f"{e}"}, status=status.HTTP_204_NO_CONTENT)


# ----------------------------
# Admin - Answer
# ----------------------------


@api_view(['POST'])
@permission_classes([IsAdminUser])
def createAnswer(request, pk):
    user = request.user
    quiz = Quiz.objects.get(_id=pk)

    answer = Answer.objects.create(
        user=user,
        quiz=quiz,
        text='Sample answer',
        isCorrect=False,
    )

    serializer = AnswerSerialize(answer, many=False)
    return Response(serializer.data)


@api_view(['PUT'])
@permission_classes([IsAdminUser])
def updateAnswer(request, pk):
    try:
        data = request.data
        answer = Answer.objects.get(_id=pk)

        answer.quiz = data['quiz']
        answer.text = data['text']
        answer.isCorrect = data['isCorrect']

        answer.save()

        serializer = AnswerSerialize(answer, many=False)
        return Response(serializer.data)
    except Exception as e:
        return Response({'details': f"{e}"}, status=status.HTTP_204_NO_CONTENT)


@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def deleteAnswer(request, pk):
    try:
        answer = Answer.objects.get(_id=pk)
        answer.delete()
        return Response('Answer Deleted')
    except Exception as e:
        return Response({'details': f"{e}"}, status=status.HTTP_204_NO_CONTENT)
