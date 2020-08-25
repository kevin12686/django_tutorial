from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import index, blogViewSet, BlogList

router = DefaultRouter()
router.register('blog', blogViewSet)

urlpatterns = [
    path('', index, name='Index'),
    path('blog/', BlogList.as_view(), name='BlogList'),
    path('api/', include(router.urls)),
]
