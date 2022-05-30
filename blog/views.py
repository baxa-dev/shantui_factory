from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from blog.models import Article, Blog
from .serializer import ArticleSerializer, BlogSerializer
from config.responses import ResponseSuccess


class ArticleGenericAPIView(GenericAPIView, ListModelMixin, RetrieveModelMixin):
    serializer_class = ArticleSerializer
    queryset = Article.objects.order_by("-pk")

    def get(self, request, pk=None):
        if pk:
            return self.retrieve(request)
        return self.list(request)

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        return ResponseSuccess(response)

    def retrieve(self, request, *args, **kwargs):
        response = super().retrieve(request, *args, **kwargs)
        return ResponseSuccess(response)


class BlogGenericAPIView(GenericAPIView, ListModelMixin, RetrieveModelMixin):
    serializer_class = BlogSerializer
    queryset = Blog.objects.order_by("-pk")

    def get(self, request, pk=None):
        if pk:
            return self.retrieve(request)
        return self.list(request)

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        return ResponseSuccess(response)

    def retrieve(self, request, *args, **kwargs):
        response = super().retrieve(request, *args, **kwargs)
        return ResponseSuccess(response)
