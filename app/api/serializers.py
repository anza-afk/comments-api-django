from rest_framework import serializers
from .models import Article, Comment
from django.contrib.auth.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'articles', 'comments')

class NestedCommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = ['child_comment']

class CommentSerializer(serializers.HyperlinkedModelSerializer):
    child_comment = NestedCommentSerializer(many=True)
    class Meta:
        model = Comment
        fields = ('url', 'content', 'created_date', 'article', 'user', 'parent', 'child_comment')


class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Article
        fields = ('url', 'name', 'title', 'content', 'created_date', 'user', 'comments')



