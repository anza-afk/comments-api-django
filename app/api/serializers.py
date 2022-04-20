from rest_framework import serializers
from .models import Article, Comment
from django.contrib.auth.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'articles', 'comments')


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = ('url', 'content', 'created_date', 'article', 'user', 'parent', 'child_comment')
    def to_representation(self, instance):
        self.fields['child_comment'] = CommentSerializer(read_only=True, many=True)
        return super(CommentSerializer, self).to_representation(instance)


class ArticleCommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = ('url', 'user', 'content', 'created_date', 'child_comment')
    def to_representation(self, instance):
        self.fields['child_comment'] = ArticleCommentSerializer(read_only=True, many=True)
        return super(ArticleCommentSerializer, self).to_representation(instance)


class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    comments = ArticleCommentSerializer(many=True, read_only=True)

    class Meta:
        model = Article
        fields = ('url', 'name', 'title', 'content', 'created_date', 'user', 'comments')


