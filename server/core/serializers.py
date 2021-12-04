from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Course, Lesson, Review, Quiz, Certificate, Enroll, Answer


class UserSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(read_only=True)
    _id = serializers.SerializerMethodField(read_only=True)
    isAdmin = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ['id', '_id', 'username', 'email', 'name', 'isAdmin']

    def get__id(self, obj):
        return obj.id

    def get_isAdmin(self, obj):
        return obj.is_staff

    def get_name(self, obj):
        name = obj.first_name
        if name == '':
            name = obj.email

        return name


class UserSerializerWithToken(UserSerializer):
    token = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ['id', '_id', 'username', 'email', 'name', 'isAdmin', 'token']

    def get_token(self, obj):
        token = RefreshToken.for_user(obj)
        return str(token.access_token)


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class CourseSerialize(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class AnswerSerialize(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'


class QuizSerialize(serializers.ModelSerializer):
    answers = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Quiz
        fields = '__all__'

    def get_answers(self, obj):
        answers = obj.answer_set.all()
        serializer = AnswerSerialize(answers, many=True)
        return serializer.data


class CertificateSerialize(serializers.ModelSerializer):
    user = serializers.SerializerMethodField(read_only=True)
    course = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Certificate
        fields = '__all__'

    def get_user(self, obj):
        user = obj.user
        serializer = UserSerializer(user, many=False)
        return serializer.data

    def get_course(self, obj):
        course = obj.course
        serializer = CourseSerialize(course, many=False)
        return serializer.data


class EnrollSerialize(serializers.ModelSerializer):
    user = serializers.SerializerMethodField(read_only=True)
    course = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Enroll
        fields = '__all__'

    def get_user(self, obj):
        user = obj.user
        serializer = UserSerializer(user, many=False)
        return serializer.data

    def get_course(self, obj):
        course = obj.course
        serializer = CourseSerialize(course, many=False)
        return serializer.data


class LessonDetailSerializer(serializers.ModelSerializer):
    quiz = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Lesson
        fields = '__all__'

    def get_quiz(self, obj):
        quiz = obj.quiz_set.all()
        serializer = QuizSerialize(quiz, many=True)
        return serializer.data

class LessonSerialize(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class CourseDetailSerialize(serializers.ModelSerializer):
    lessons = serializers.SerializerMethodField(read_only=True)
    reviews = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Course
        fields = '__all__'

    def get_lessons(self, obj):
        lesson = obj.lesson_set.all()
        serializer = LessonSerialize(lesson, many=True)
        return serializer.data

    def get_reviews(self, obj):
        reviews = obj.review_set.all()
        serializer = ReviewSerializer(reviews, many=True)
        return serializer.data
