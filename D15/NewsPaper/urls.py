"""NewsPaper URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from django.views.generic import TemplateView
urlpatterns = [
  
    path('i18n/', include('django.conf.urls.i18n')), # подключаем встроенные эндопинты для работы с локализацией

    path('sign/', include('sign.urls')),
    path('', include('protect.urls')),
    path('admin/', admin.site.urls),
    path('news/', include('news.urls')),  # делаем так, чтобы все адреса из нашего приложения (simpleapp/urls.py) сами автоматически подключались когда мы их добавим.
    path('accounts/', include('allauth.urls')),

    path('swagger-ui/', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url':'openapi-schema'}
    ), name='swagger-ui'),

]