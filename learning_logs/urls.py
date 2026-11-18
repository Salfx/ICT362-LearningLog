
"""Defines URL patterns for learning_logs."""

from django.urls import path

from . import views

app_name = 'learning_logs'

urlpatterns = [
    # Home page
    path('', views.index, name='index'),

    # Page showing all learning topics
    path('topics/', views.topics, name='topics'),

    # Page showing a specific topic and its entries
    path('topics/<int:topic_id>/', views.topic_detail, name='topic_detail'),
]
