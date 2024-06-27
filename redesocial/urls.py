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
from django.urls import include, path
from rest_framework import routers
from rest_framework.response import Response
from rest_framework import status
from user.views import (
    UserViews,
    UserLoginAPIView,
    PostAPIView,
    CommentAPIView,
    LikeAPIView,
)
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register(r"user", UserViews, basename="registration")
router.register(r"user_login", UserLoginAPIView, basename="login")
router.register(r"post", PostAPIView, basename="post")
router.register(r"comment", CommentAPIView, basename="comment")
router.register(r"like", LikeAPIView, basename="like")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth", include("rest_framework.urls")),
    path("api/", include(router.urls)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
