from django.urls import include, path
from rest_framework import routers

from .views import PostViewSet


router_v1 = routers.DefaultRouter()
router_v1.register(r'posts', PostViewSet)

urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/', include('djoser.urls.jwt')),
]
