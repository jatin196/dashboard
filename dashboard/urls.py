"""dashboard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf import settings
from  django.conf.urls.static import static
from news.views import scrape, news_list
from twitter_embed.views import video_view
# from send_email.views import send
import debug_toolbar
from chat_app import views
from todo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('__debug__/', include(debug_toolbar.urls)),
    path('notes/', include('notepad.urls')),
    # path('tinymce/', include('tinymce.urls')),
    # path('api-auth/', include('rest_framework.urls')),
    path('scrape/', scrape, name='scrape'),
    path('home/', news_list, name='home' ),
    path('video-home/', video_view, name='vid-view'),
    # path('send-email/', send, name='send'),
    # path('restapi/', include('restapi.urls')),
    path('chat/', include('chat_app.urls', namespace='chat')),
    path('todo/', include('todo.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


