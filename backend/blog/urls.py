from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import index, blogViewSet

router = DefaultRouter()
router.register('blog', blogViewSet)

urlpatterns = [
    path('', index, name='Index'),
    path('api/', include(router.urls)),
]
