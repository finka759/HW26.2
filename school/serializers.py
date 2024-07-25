from rest_framework.serializers import ModelSerializer, SerializerMethodField

from school.models import Course, Lesson, Subscription
from school.validators import YTValidator


class LessonSerializer(ModelSerializer):
    class Meta:
        validators = [YTValidator(field='video_track'), ]
        model = Lesson
        fields = '__all__'


class CourseSerializer(ModelSerializer):
    lessons = LessonSerializer(source="lesson_set", many=True, read_only=True)

    class Meta:
        model = Course
        fields = '__all__'


class CourseDetailSerializer(ModelSerializer):
    lessons_count = SerializerMethodField(read_only=True)
    subscription = SerializerMethodField(read_only=True)
    lessons = LessonSerializer(source="lesson_set", many=True, read_only=True)

    def get_subscription(self, obj):
        request = self.context.get('request')
        user = None
        if request:
            user = request.user
        return obj.subscription_set.filter(user=user).exists()

    def get_lessons_count(self, course):
        return Lesson.objects.filter(course=course).count()

    class Meta:
        model = Course
        fields = ['id', 'name', 'lessons_count', 'description', 'image', 'owner', 'lessons', 'subscription']


class SubscriptionSerializer(ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'
