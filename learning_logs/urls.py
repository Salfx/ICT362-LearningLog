
"""Defines URL patterns for learning_logs."""

from django.urls import path

from . import views

app_name = 'learning_logs'

urlpatterns = [
    # Home page
    path('', views.index, name='index'),

    # Page for an individual learning topic
    path('topics/<str:topic_name>/', views.topic_detail, name='topic_detail'),
]
