from django.shortcuts import render, redirect
from .models import Topic, Tag
from . forms import TopicForm
from django.db.models import Q


def topics(request):
    search = request.GET.get('search')

    if request.GET.get('search'):
        tags = Tag.objects.filter(name__iexact=search)
        topics = Topic.objects.filter(Q(tags__in=tags))
    else:
        topics = Topic.objects.all().order_by('-created')[0:3]

    context = {'topics': topics}
    return render(request, 'blog_app/topics.html', context)


def topic(request, pk):
    topic = Topic.objects.get(id=pk)
    tags = topic.tags.all()

    context = {'topic': topic, 'tags': tags}
    return render(request, 'blog_app/topic.html', context)


def topic_create_or_update(request, pk=None):
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
    topic = Topic.objects.get(id=pk)

    if request.method == 'POST':
        topic.delete()
        return redirect('topics')

    context = {'object': topic}
    return render(request, 'delete_confirm.html', context)
