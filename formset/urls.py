"""formset URL Configuration

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
from django.urls import path
from myapp.views import index, inline_example, book_list, create_book_normal
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inline/<programmer_id>/', inline_example, name='inline_example'),
    path('book-list/', book_list, name='book-list'),
    path('create-normal/', create_book_normal, name='create-normal'),
    path('', index, name='index'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
