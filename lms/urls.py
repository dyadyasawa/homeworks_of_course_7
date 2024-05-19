from django.urls import path
from rest_framework.routers import SimpleRouter

from lms.apps import LmsConfig
from lms.views import CourseViewSet, LessonCreateApiView, LessonListApiView, LessonRetrieveApiView, LessonUpdateApiView, LessonDestroyApiView

app_name = LmsConfig.name

router = SimpleRouter()
router.register("", CourseViewSet)

urlpatterns = [
    path("lesson/", LessonListApiView.as_view(), name="lesson_list"),
    path("lesson/<int:pk>/detail/", LessonRetrieveApiView.as_view(), name="lesson_detail"),
    path("lesson/create/", LessonCreateApiView.as_view(), name="lesson_create"),
    path("lesson/<int:pk>/update/", LessonUpdateApiView.as_view(), name="lesson_update"),
    path("lesson/<int:pk>/delete/", LessonDestroyApiView.as_view(), name="lesson_delete"),
]

urlpatterns += router.urls
