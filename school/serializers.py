from rest_framework.serializers import ModelSerializer, SerializerMethodField

from school.models import Course, Lesson


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class CourseSerializer(ModelSerializer):
    lessons = LessonSerializer(source="lesson_set", many=True, read_only=True)
    class Meta:
        model = Course
        fields = '__all__'


class CourseDetailSerializer(ModelSerializer):
    lessons_count = SerializerMethodField(read_only=True)
    lessons = LessonSerializer(source="lesson_set", many=True, read_only=True)

    class Meta:
        model = Course
        fields = ['id', 'name', 'lessons_count', 'description', 'image', 'owner', 'lessons']

    def get_lessons_count(self, course):
        return Lesson.objects.filter(course=course).count()

