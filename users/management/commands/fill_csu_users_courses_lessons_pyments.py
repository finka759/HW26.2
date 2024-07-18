from django.core.management import BaseCommand

from school.models import Course, Lesson
from users.models import User, Payment


class Command(BaseCommand):
    """Команда для заполнения всех данных БД """

    def handle(self, *args, **options):
        Payment.objects.all().delete()
        User.objects.all().delete()
        Lesson.objects.all().delete()
        Course.objects.all().delete()

        user = User.objects.create(
            pk=10,
            email='admin',
            first_name='Admin',
            is_staff=True,
            is_superuser=True
        )

        user.set_password('admin')
        user.save()

        user_list = [
            {'pk': 11, 'fields': {'email': 'user1@sky.com', 'phone': '111111111'}},
            {'pk': 12, 'fields': {'email': 'user2@sky.com', 'phone': '222222222'}},
            {'pk': 13, 'fields': {'email': 'user3@sky.com', 'phone': '333333333'}},
        ]
        users_for_create = []

        for user in user_list:
            users_for_create.append(
                User(pk=user.get('pk'),
                     email=user.get('fields').get('email'),
                     phone=user.get('fields').get('phone')
                     )
            )

        User.objects.bulk_create(users_for_create)

        course_list = [
            {'pk': 1, 'fields': {'name': 'название_курса_1', 'description': 'описание_курса_1'}},
            {'pk': 2, 'fields': {'name': 'название_курса_2', 'description': 'описание_курса_2'}},
            {'pk': 3, 'fields': {'name': 'название_курса_3', 'description': 'описание_курса_3'}},
        ]
        courses_for_create = []

        for course in course_list:
            courses_for_create.append(
                Course(pk=course.get('pk'),
                       name=course.get('fields').get('name'),
                       description=course.get('fields').get('description')
                       )
            )

        Course.objects.bulk_create(courses_for_create)

        lessons_list = [
            {'pk': 11, 'fields': {'name': 'название_лекции_11', 'description': 'описание_лекции_11', 'course': 1}},
            {'pk': 12, 'fields': {'name': 'название_лекции_12', 'description': 'описание_лекции_12', 'course': 1}},
            {'pk': 13, 'fields': {'name': 'название_лекции_13', 'description': 'описание_лекции_13', 'course': 1}},
            {'pk': 21, 'fields': {'name': 'название_лекции_21', 'description': 'описание_лекции_21', 'course': 2}},
            {'pk': 22, 'fields': {'name': 'название_лекции_22', 'description': 'описание_лекции_22', 'course': 2}},
            {'pk': 31, 'fields': {'name': 'название_лекции_31', 'description': 'описание_лекции_31', 'course': 3}},
        ]
        lessons_for_create = []

        for lesson in lessons_list:
            lessons_for_create.append(
                Lesson(pk=lesson.get('pk'),
                       name=lesson.get('fields').get('name'),
                       description=lesson.get('fields').get('description'),
                       course=Course.objects.get(pk=lesson.get('fields').get('course'))
                       )
            )

        Lesson.objects.bulk_create(lessons_for_create)

        payments_list = [
            {'pk': 1, 'fields': {'user': 11, 'payment_date': '2024-07-01', 'course': 1, 'payment_method': 'CARD'}},
            {'pk': 2, 'fields': {'user': 12, 'payment_date': '2024-07-02', 'course': 2, 'payment_method': 'CARD'}},
            {'pk': 3, 'fields': {'user': 13, 'payment_date': '2024-07-03', 'course': 3, 'payment_method': 'CARD'}},
            {'pk': 4, 'fields': {'user': 11, 'payment_date': '2024-07-11', 'lesson': 31, 'payment_method': 'CARD'}},
            {'pk': 5, 'fields': {'user': 13, 'payment_date': '2024-07-11', 'lesson': 22, 'payment_method': 'CASH'}},
        ]
        payments_for_create = []

        for payment in payments_list:
            payments_for_create.append(
                Payment(pk=payment.get('pk'),
                        user=User.objects.get(pk=payment.get('fields').get('user')),
                        payment_date=payment.get('fields').get('payment_date'),
                        course=Course.objects.get(pk=payment.get('fields').get('course')) if (
                            payment.get('fields').get('course')) else None,
                        lesson=Lesson.objects.get(pk=payment.get('fields').get('lesson')) if (
                            payment.get('fields').get('lesson')) else None,
                        payment_method=payment.get('fields').get('payment_method')
                        )
            )
        Payment.objects.bulk_create(payments_for_create)
