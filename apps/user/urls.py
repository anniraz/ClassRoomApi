from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register(
    prefix="user",
    viewset=UsersApiView
)


urlpatterns = router.urls
