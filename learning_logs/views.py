
"""View functions for the Learning Log application."""

from django.shortcuts import render, get_object_or_404

from .models import Topic


def index(request):
    """Display the Learning Log home page."""
    return render(request, 'learning_logs/index.html')


def topics(request):
    """Display all learning topics."""
    topics_list = Topic.objects.order_by('date_added')
    context = {'topics': topics_list}
    return render(request, 'learning_logs/topics.html', context)


def topic_detail(request, topic_id):
    """Display a topic and its entries."""
    topic = get_object_or_404(Topic, id=topic_id)
    entries = topic.entry_set.order_by('-date_added')

    context = {
        'topic': topic,
        'entries': entries,
    }

    return render(request, 'learning_logs/topic_detail.html', context)
