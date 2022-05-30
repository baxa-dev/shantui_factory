from django.urls import path, include
from .views import STGenericAPIView, STCAPIView, FactoryAPIView, ContactCreateAPIView, FactoryApplicationAPIView
urlpatterns = [
    path('st/', STGenericAPIView.as_view(), name='st'),
    path('st/<int:id>/', STGenericAPIView.as_view(), name='st-detail'),
    path('stc/', STCAPIView.as_view(), name='stc'),
    path('stc/<int:id>/', STCAPIView.as_view(), name='stc-detail'),
    path('f/', FactoryAPIView.as_view(), name='f'),
    path('f/<int:id>/', FactoryAPIView.as_view(), name='f-detail'),
    path('f_a/', FactoryApplicationAPIView.as_view(), name='f_a'),
    path('f_a/<int:id>/', FactoryApplicationAPIView.as_view(), name='f_a-detail'),
    path('contact/', ContactCreateAPIView.as_view(), name='contact'),
    path('', include("blog.urls")),
]