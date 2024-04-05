"""
URL configuration for redesocial project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include,path
from rest_framework import routers
from rest_framework.response import Response
from rest_framework import status
from user.views import UserRegistrationAPIView, UserLoginAPIView, PostAPIView, CommentAPIView, LikeAPIView
from django.views.generic import TemplateView
from django.http import HttpResponse

router= routers.DefaultRouter()
router.register(r'user_registration', UserRegistrationAPIView, basename='registration')
router.register(r'user_login', UserLoginAPIView, basename='login')
router.register(r'post', PostAPIView, basename='post')
router.register(r'comment', CommentAPIView, basename='comment')
router.register(r'like', LikeAPIView, basename='like')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    path('api-auth/logout'),
    path('api-auth/password/change'),
    path('api-auth/password/reset'),
    path('api/user_registration', UserRegistrationAPIView.as_view({'get':'list'}), name='hello'),
    path('api-auth/login/', UserLoginAPIView.as_view({'get':'list'}), name='login'),
    path('api/post', PostAPIView.as_view({'get':'list'}), name='post'),
    path('api/comment', CommentAPIView.as_view({'get':'list'}), name='comment'),
    path('api/like', LikeAPIView.as_view({'get':'list'}), name='like')
]



