from django.urls import path
from . import views

app_name = "dashboard"

urlpatterns = [
    path('', views.home, name='home'),

    path("st/", views.st, name="st"),
    path('st/create/', views.create_st, name="create_st"),
    path('st/update/<str:pk>/', views.update_st, name="update_st"),
    path("st/delete/<str:pk>/", views.delete_st, name="delete_st"),

    path("stc/", views.specialtechniquecategory, name="stc"),
    path('stc/create/', views.create_stc, name="create_stc"),
    path('stc/update/<str:pk>/', views.update_stc, name="update_stc"),
    path("stc/delete/<str:pk>/", views.delete_stc, name="delete_stc"),

    path("factory/", views.factory, name="factory"),
    path('factory/create/', views.create_factory, name="create_factory"),
    path('factory/update/<str:pk>/', views.update_factory, name="update_factory"),
    path("factory/delete/<str:pk>/", views.delete_factory, name="delete_factory"),

    path("contact/", views.contact, name="contact"),

    path("blog/", views.blogs, name="blog"),
    path('blog/create/', views.create_blog, name="create_blog"),
    path('blog/update/<str:pk>/', views.update_blog, name="update_blog"),
    path("blog/delete/<str:pk>/", views.delete_blog, name="delete_blog"),

    path("article/", views.article, name="article"),
    path('article/create/', views.create_article, name="create_article"),
    path('article/update/<str:pk>/', views.update_article, name="update_article"),
    path("article/delete/<str:pk>/", views.delete_article, name="delete_article"),


    path('login/', views.login_admin, name='login'),
    path('logout/', views.logout_admin, name='logout'),

]
