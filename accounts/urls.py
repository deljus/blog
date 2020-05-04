from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'accounts'

urlpatterns = [
    url('signup/', views.signup, name='registration'),
    url(r'^activate/(?P<uid64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('profile/info/<int:id>', views.ProfileInfoView.as_view(), name='info'),
    url('users/', views.UsersView.as_view(), name='users'),
]
