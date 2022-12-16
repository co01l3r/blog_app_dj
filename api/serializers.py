from rest_framework import serializers
from blog_app.models import Topic, Tag


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = '__all__'


class TopicSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)

    class Meta:
        model = Topic
        fields = '__all__'
