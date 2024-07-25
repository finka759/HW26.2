from django.urls import path
from rest_framework.routers import SimpleRouter

from school.apps import SchoolConfig
from school.views import CourseViewSet, LessonCreateApiView, LessonUpdateApiView, LessonDestroyApiView, \
    LessonListApiView, LessonRetrieveApiView, SubscriptionAPIView

app_name = SchoolConfig.name

router = SimpleRouter()
router.register("", CourseViewSet)

urlpatterns = [
    path("lessons/", LessonListApiView.as_view(), name="lessons_list"),
    path("lessons/<int:pk>/", LessonRetrieveApiView.as_view(), name="lessons_retrieve"),
    path("lessons/create/", LessonCreateApiView.as_view(), name="lessons_create"),
    path("lessons/<int:pk>/update/", LessonUpdateApiView.as_view(), name="lessons_update"),
    path("lessons/<int:pk>/delete/", LessonDestroyApiView.as_view(), name="lessons_delete"),
    path('subscription/', SubscriptionAPIView.as_view(), name='subscriptione'),
]

urlpatterns += router.urls
