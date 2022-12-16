from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TopicSerializer
from blog_app.models import Topic


@api_view(['GET'])
def get_routes(request):

    routes = [
        {'GET': 'api/topics'},
        {'GET': 'api/topics/id'},
    ]

    return Response(routes)


@api_view(['GET'])
def get_topics(request):
    topics = Topic.objects.all()
    serializer = TopicSerializer(topics, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def get_topic(request, pk):
    topic = Topic.objects.get(id=pk)
    serializer = TopicSerializer(topic, many=False)

    return Response(serializer.data)
