from rest_framework.routers import SimpleRouter

from school.apps import SchoolConfig
from school.views import CourseViewSet

app_name = SchoolConfig.name

router = SimpleRouter()
router.register("", CourseViewSet)

urlpatterns = []

urlpatterns += router.urls
