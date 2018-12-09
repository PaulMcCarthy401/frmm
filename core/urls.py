from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.urls import path, include

from . import views

app_name = 'core'
urlpatterns = [
    # url(r'^login/$', auth_views.LoginView.as_view(), name='login'),
    # url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    path('', include('django.contrib.auth.urls')),
    path('', views.TicketCreate.as_view(), name='index'),
    # path('tickets/<int:pk>/', views.DetailView.as_view(), name='detail'),
]
