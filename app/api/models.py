from django.db import models


class Article(models.Model):
    name = models.CharField(max_length=60)
    title = models.CharField(max_length=120, default='', blank=True)
    content = models.TextField(max_length=60)
    created_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='articles')

    def __str__(self):
        return self.content


class Comment(models.Model):
  content = models.TextField('Содержание', max_length = 300, default = '')
  created_date = models.DateTimeField(auto_now_add=True)
  article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
  user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='comments')
  parent = models.ForeignKey(
    'self',
    default=None,
    blank=True, null=True,
    on_delete=models.CASCADE,
    related_name='parent_%(class)s',
    verbose_name='parent comment'
  )

  def __str__(self):	
    return self.content

  class Meta:
    ordering = ['-created_date']