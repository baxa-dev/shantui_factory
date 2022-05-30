from django.urls import path
from .views import ArticleGenericAPIView, BlogGenericAPIView

app_name = "blog"

urlpatterns = [
    path('article/', ArticleGenericAPIView.as_view()),
    path('article/<int:pk>/', ArticleGenericAPIView.as_view()),

    path('blog/', BlogGenericAPIView.as_view()),
    path('blog/<int:pk>/', BlogGenericAPIView.as_view()),

]