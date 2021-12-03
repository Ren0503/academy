from django.urls import path
from core.views import course_views as views

urlpatterns = [
    path('', views.getCourses, name="courses"),
]