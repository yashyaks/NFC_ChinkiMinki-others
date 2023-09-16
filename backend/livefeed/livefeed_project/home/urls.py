from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('live_feed/', views.live_feed, name='live_feed'),
    path('update_sentences/', views.update_sentences, name='update_sentences'),
    path('text_to_speech/', views.text_to_speech, name='text_to_speech'),
    path('new_data/', views.new_data, name='new_data')
]
