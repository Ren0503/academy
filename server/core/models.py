from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.


class Course(models.Model):
    _id = models.UUIDField(default=uuid.uuid4,  unique=True,
                           primary_key=True, editable=False)
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(null=True, blank=True,
                              default='/placeholder.png')
    category = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    rating = models.DecimalField(
        max_digits=7, decimal_places=2, null=True, blank=True)
    numReviews = models.IntegerField(null=True, blank=True, default=0)
    participants = models.IntegerField(null=True, blank=True, default=0)
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Review(models.Model):
    _id = models.UUIDField(default=uuid.uuid4,  unique=True,
                           primary_key=True, editable=False)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    rating = models.IntegerField(null=True, blank=True, default=0)
    comment = models.TextField(null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.rating)


class Lesson(models.Model):
    _id = models.UUIDField(default=uuid.uuid4,  unique=True,
                           primary_key=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    unit = models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    content = models.TextField(null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Enroll(models.Model):
    _id = models.UUIDField(default=uuid.uuid4,  unique=True,
                           primary_key=True, editable=False)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(max_length=200, blank=True, null=True)
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.status


class Certificate(models.Model):
    _id = models.UUIDField(default=uuid.uuid4,  unique=True,
                           primary_key=True, editable=False)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True)
    text = models.CharField(max_length=200, blank=True, null=True)
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text


class Quiz(models.Model):
    _id = models.UUIDField(default=uuid.uuid4,  unique=True,
                           primary_key=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    lesson = models.ForeignKey(Lesson, on_delete=models.SET_NULL, null=True)
    question = models.CharField(max_length=200, blank=True, null=True)
    numAnswer = models.IntegerField(blank=True, null=True, default=0)
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question


class Answer(models.Model):
    _id = models.UUIDField(default=uuid.uuid4,  unique=True,
                           primary_key=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    quiz = models.ForeignKey(Quiz, on_delete=models.SET_NULL, null=True)
    text = models.CharField(max_length=200, blank=True, null=True)
    isCorrect = models.BooleanField(blank=True, null=True)
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
