from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import ArticleSerializer, CommentSerializer, UserSerializer
from .models import Article, Comment


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer