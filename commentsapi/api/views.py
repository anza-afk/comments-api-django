from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ArticleSerializer, CommentSerializer
from .models import Article, Comment


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer