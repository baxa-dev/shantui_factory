from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=100, verbose_name="заглавие")

    def __str__(self) -> str:
        return str(self.title)


class Blog(models.Model):
    article = models.ForeignKey('Article', on_delete=models.PROTECT, verbose_name="статья")
    title = models.CharField(max_length=60, verbose_name="заглавие")
    create_at = models.DateTimeField(auto_now_add=True, verbose_name="создать в")
    Video = models.URLField(max_length=200, null=True, unique=True, verbose_name="видео")

    def __str__(self) -> str:
        return str(self.title)
