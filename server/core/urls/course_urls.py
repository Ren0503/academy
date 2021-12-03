from django.urls import path
from core.views import course_views as views

urlpatterns = [
    path('', views.getCourses, name="courses"),

    path('create/', views.createCourse, name="course-create"),
    path('upload/', views.uploadImage, name="image-upload"),

    path('<str:pk>/reviews/', views.createCourseReview, name="create-review"),
    path('top/', views.getTopCourses, name="top-courses"),
    path('<str:pk>/', views.getCourse, name="course"),


    path('<str:pk>/enroll/', views.enrollCourse, name="enroll-course"),
    path('<str:pk>/certificate/', views.certificateCourse, name="certificate-course"),

    path('update/<str:pk>/', views.updateCourse, name="course-update"),
    path('delete/<str:pk>/', views.deleteCourse, name="course-delete"),
]