from rest_framework.routers import DefaultRouter
from .views import *


router = DefaultRouter()

router.register(
    prefix="course",
    viewset=CourseApiView
)

router.register(
    prefix='members',
    viewset=CourseMembersApiView
    )

urlpatterns = router.urls
