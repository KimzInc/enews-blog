
from django.contrib import admin
from django.urls import path

from blog.views import index,contact, post_detail

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('contact/',contact, name='contact'),
    path('<int:id>/',post_detail, name='post_detail')
]
