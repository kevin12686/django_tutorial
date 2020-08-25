from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.contrib.auth.views import LoginView, LogoutView
from .views import index, blogViewSet, BlogList, BlogCreate, BlogUpdate

router = DefaultRouter()
router.register('blog', blogViewSet)

urlpatterns = [
    path('', index, name='Index'),
    path('login/', LoginView.as_view(template_name='form.html'), name='Login'),
    path('logout/', LogoutView.as_view(), name='Logout'),
    path('blog/', BlogList.as_view(), name='BlogList'),
    path('blog/create/', BlogCreate.as_view(), name='BlogCreate'),
    path('blog/update/<pk>/', BlogUpdate.as_view(), name='BlogUpdate'),
    path('api/', include(router.urls)),
]
