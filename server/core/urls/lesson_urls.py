from django.urls import path
from core.views import lesson_views as views

urlpatterns = [
    path('by_course/<str:pk>/', views.getLessonsByCourse, name="lesson"),
    path('<str:pk>/', views.getDetailLesson, name="lesson-detail"),
    path('answer/<str:pk>/', views.answerForQuiz, name="answer-detail"),

    path('create/<str:pk>/', views.createLesson, name='create-lesson'),
    path('update/<str:pk>/', views.updateLesson, name="update-lesson"),
    path('delete/<str:pk>/', views.deleteLesson, name="delete-lesson"),

    path('create-quiz/<str:pk>/', views.createQuiz, name='create-quiz'),
    path('update-quiz/<str:pk>/', views.updateQuiz, name="update-quiz"),
    path('delete-quiz/<str:pk>/', views.deleteQuiz, name="delete-quiz"),

    path('create-answer/<str:pk>/', views.createAnswer, name='create-answer'),
    path('update-answer/<str:pk>/', views.updateAnswer, name="update-answer"),
    path('delete-answer/<str:pk>/', views.deleteAnswer, name="delete-answer"),
]