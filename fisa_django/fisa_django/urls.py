"""
URL configuration for fisa_django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
# django_project/urls.py

from django.contrib import admin
from django.urls import path, include
# 이미지 업로드 필드를 위한 추가
from django.conf import settings
from django.conf.urls.static import static

# 도메인주소 뒤에 들어갈 경로를 설정
# 가장 메인 화면은 도메인/ 
# 게시글이나 페이지에 
urlpatterns = [
    path("admin/", admin.site.urls),
    path('blog/', include('blog.urls')), # blog/urls.py가 가지고 있는 모든 경로를 도메인/blog/아래 주소로 호출
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

