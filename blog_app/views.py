from django.shortcuts import render, redirect
from .models import Topic, Tag
from . forms import TopicForm
from django.db.models import Q


def topics(request):
    """
    Display a list of topics based on a search query.

    Parameters:
    request (HttpRequest): The incoming HTTP request.

    Returns:
    HttpResponse: The rendered HTTP response.
    """
    search = request.GET.get('search')

    if request.GET.get('search'):
        tags = Tag.objects.filter(name__iexact=search)
        topics = Topic.objects.filter(Q(tags__in=tags))
    else:
        topics = Topic.objects.all().order_by('-created')[0:3]

    context = {'topics': topics}
    return render(request, 'blog_app/topics.html', context)


def topic(request, pk):
    """
    Display a single topic and its associated tags.

    Parameters:
    request (HttpRequest): The incoming HTTP request.
    pk (int): The primary key of the topic to display.

    Returns:
    HttpResponse: The rendered HTTP response.
    """
    topic = Topic.objects.get(id=pk)
    tags = topic.tags.all()

    context = {'topic': topic, 'tags': tags}
    return render(request, 'blog_app/topic.html', context)


def topic_create_or_update(request, pk=None):
    """
    Create or update a topic and its associated tags.

    Parameters:
    request (HttpRequest): The incoming HTTP request.
    pk (int, optional): The primary key of the topic to update. If not provided, a new topic will be created.

    Returns:
    HttpResponse: The rendered HTTP response, or a redirect to the topics list.
    """
    if pk:
        topic = Topic.objects.get(id=pk)
    else:
        topic = None

    if request.method == 'POST':
        form = TopicForm(request.POST, request.FILES, instance=topic)
        new_tags = request.POST.get('new_tags') or ""
        new_tags = new_tags.replace(',', " ").split()

        if form.is_valid():
            topic = form.save()

            for tag in new_tags:
                tag, created = Tag.objects.get_or_create(name=tag)
                topic.tags.add(tag)

            return redirect('topics')
    else:
        form = TopicForm(instance=topic)

    context = {'form': form}
    return render(request, 'blog_app/topic_form.html', context)


def topic_delete(request, pk):
    """
    Delete a topic and its associated tags.

    Parameters:
    request (HttpRequest): The incoming HTTP request.
    pk (int): The primary key of the topic to delete.

    Returns:
    HttpResponse: The rendered HTTP response, or a redirect to the topics list.
    """
    topic = Topic.objects.get(id=pk)

    if request.method == 'POST':
        topic.delete()
        return redirect('topics')

    context = {'object': topic}
    return render(request, 'delete_confirm.html', context)
