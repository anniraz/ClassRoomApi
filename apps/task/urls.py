from rest_framework.routers import DefaultRouter
from .views import *


router = DefaultRouter()

router.register(
    prefix="task",
    viewset=TaskApiViewSet
)

router.register(
    prefix='attach/to/task',
    viewset=AttachToTaskApiViewSet
    )

router.register(
    prefix ='homework',
    viewset=HomeworksApiView
    )


router.register(
    prefix ='homework/check',
    viewset=HomeWorkCheckTeacher
    )


urlpatterns = router.urls