from django.urls import path
from core.views import lesson_views as views

urlpatterns = [
    path('by_course/<str:pk>/', views.getLessonsByCourse, name="lesson"),
    path('<str:pk>/', views.getDetailLesson, name="lesson-detail")
]