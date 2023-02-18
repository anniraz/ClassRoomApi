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

urlpatterns = router.urls