from django.urls import path

from .views import *

from rest_framework import routers

#from .views import index


router = routers.DefaultRouter()
router.register('students', StudentsViewSet)


urlpatterns = router.urls
