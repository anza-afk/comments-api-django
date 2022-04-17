from rest_framework import serializers
from .models import Article, Comment
from django.contrib.auth.models import User

class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Article
        fields = ('name', 'title', 'content', 'created_date', 'user')


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = ('content', 'created_date', 'article', 'user', 'parent')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="api:user-detail")

    class Meta:
        model = User
        fields = ('url', 'username')