from django.shortcuts import redirect
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

def index(request):
    return redirect('/dashboard/')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('api/', include('api.urls')),
    path('dashboard/', include([
        path("", include('dashboard.urls')),
        path('blog/', include('blog.urls')),
    ])),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
