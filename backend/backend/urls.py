from rest_framework import routers
from django.urls import include, path
from django.contrib import admin
from .views import UserViewSet, GroupViewSet
from core.views import ListViewSet


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'list', ListViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
