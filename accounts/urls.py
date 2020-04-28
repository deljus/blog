from django.urls import path
from django.conf.urls import url
from django.conf.urls import include
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    url('signup/', views.signup, name='registration'),
    url(r'^activate/(?P<uid64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
    url('profile/', views.ProfileView.as_view(), name='profile'),
]
