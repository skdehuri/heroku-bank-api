from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import SearchViewSet

router = DefaultRouter()
router.register(r'branches', SearchViewSet, basename='search')

urlpatterns = [
    path('', include(router.urls)),
]
