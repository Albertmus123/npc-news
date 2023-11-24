from django.contrib import admin
from django.urls import path
from news.views import home,post_details,global_news

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home),
    path('post/<int:id>',post_details),
    path('global-news',global_news,name='global_news'),
]
