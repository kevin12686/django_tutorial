from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import index, blogViewSet, BlogList, BlogCreate

router = DefaultRouter()
router.register('blog', blogViewSet)

urlpatterns = [
    path('', index, name='Index'),
    path('blog/', BlogList.as_view(), name='BlogList'),
    path('blog/create/', BlogCreate.as_view(), name='BlogCreate'),
    path('api/', include(router.urls)),
]
