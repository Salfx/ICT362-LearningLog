
from django.shortcuts import render


def index(request):
    """The home page for Learning Log."""
    return render(request, 'learning_logs/index.html')


def topic_detail(request, topic_name):
    """Show a page for a specific learning topic."""
    context = {'topic_name': topic_name}
    return render(request, 'learning_logs/topic_detail.html', context)
