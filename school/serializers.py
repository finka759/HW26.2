from rest_framework.serializers import ModelSerializer, SerializerMethodField

from school.models import Course, Lesson


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class CourseSerializer(ModelSerializer):
    # lessons_date = LessonSerializer(many=True, source='course')

    class Meta:
        model = Course
        fields = '__all__'


class CourseDetailSerializer(ModelSerializer):
    lessons_count = SerializerMethodField()
    # information_all_lessons = LessonSerializer(many=True, source='course') , 'information_all_lessons'

    class Meta:
        model = Course
        fields = ('name', 'description', 'owner', 'lessons_count')

    def get_lessons_count(self, course):
        return Lesson.objects.filter(course=course).count()


