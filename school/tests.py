from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from school.models import Lesson, Course, Subscription
from users.models import User


class CourseTestCase(APITestCase):

    def setUp(self) -> None:
        super().setUp()
        self.user = User.objects.create(
            email='user@test.com',
            password='123'
        )
        self.course = Course.objects.create(
            name='имя_тестового_курса_1',
            description='описание_тестового_курса_1',
            owner=self.user
        )
        self.lesson = Lesson.objects.create(
            name='имя_тестовой_лекции_1',
            description='описание_тестовой_лекции_1',
            course=self.course,
            owner=self.user
        )
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_course_retrive(self):
        url = reverse('school:course-detail', args=(self.course.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        # print(response.json())
        self.assertEqual(
            data, {'id': self.course.pk, 'name': 'имя_тестового_курса_1', 'lessons_count': 1,
                   'description': 'описание_тестового_курса_1', 'image': None, 'owner': self.user.pk,
                   'lessons': [{'id': self.lesson.pk, 'name': 'имя_тестовой_лекции_1',
                                'description': 'описание_тестовой_лекции_1',
                                'image': None, 'video_track': None, 'course': self.course.pk, 'owner': self.user.pk}],
                   'subscription': False}
        )

    def test_course_create(self):
        url = reverse('school:course-list')
        data = {
            'name': 'тестовое_имя_2',
            'description': 'тестовое_описание_2'
        }
        response = self.client.post(url, data)
        self.assertEqual(
            response.status_code, status.HTTP_201_CREATED
        )
        self.assertEqual(
            Course.objects.all().count(), 2
        )

    def test_course_update(self):
        url = reverse('school:course-detail', args=(self.course.pk,))
        data = {
            'name': 'тестовое_имя_update'
        }
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get('name'), 'тестовое_имя_update'
        )

    def test_course_delete(self):
        url = reverse('school:course-detail', args=(self.course.pk,))
        response = self.client.delete(url)
        self.assertEqual(
            response.status_code, status.HTTP_204_NO_CONTENT
        )
        self.assertEqual(
            Course.objects.all().count(), 0
        )

    def test_course_list(self):
        url = reverse('school:course-list')
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        result = {'count': 1, 'next': None, 'previous': None,
                  'results': [{'id': self.course.pk,
                               'lessons': [{'id': self.lesson.pk,
                                            'name': 'имя_тестовой_лекции_1',
                                            'description': 'описание_тестовой_лекции_1',
                                            'image': None,
                                            'video_track': None,
                                            'course': self.course.pk, 'owner': self.user.pk}],
                               'name': 'имя_тестового_курса_1',
                               'description': 'описание_тестового_курса_1',
                               'image': None, 'owner': self.user.pk}]}
        self.assertEqual(data, result)


class SubscriptionTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email='testcase@test.com', password='123')
        self.course = Course.objects.create(name='тест_имя_курса', description='тест_описание_курса')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_subscription_activate(self):
        url = reverse('school:subscription')
        data = {'user': self.user.id,
                'course': self.course.id}

        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {'message': 'подписка добавлена'})

    def test_subscription_deactivate(self):
        url = reverse('school:subscription')
        Subscription.objects.create(user=self.user, course=self.course)
        data = {'user': self.user.id,
                'course': self.course.id}

        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {'message': 'подписка удалена'})
