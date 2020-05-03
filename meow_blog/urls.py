from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static
from .views import IndexView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', include('posts.urls', namespace='posts')),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('', IndexView.as_view(), name='index'),
    path('summernote/', include('django_summernote.urls')),
    path('i18n/', include('django.conf.urls.i18n')),
    path('comment/', include('comment.urls')),
    path('api/', include('comment.api.urls')),
    path('', include('django.contrib.auth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
