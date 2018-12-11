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
    path('volunteer/', views.ResourceCreateView.as_view(), name='volunteer_page'),
    path('firstresponder', views.FirstResponderPage.as_view(), name='first_responder_page'),
    path('firstresponderchief', views.FirstResponderChiefPage.as_view(), name='first_responder_chief_page'),
    path('mission/', views.MissionCreate.as_view(), name='mission_create'),
    path('mission/<int:pk>/', views.MissionUpdate.as_view(), name='mission_update'),
    path('ticket/<int:pk>/', views.TicketView.as_view(), name='ticket_view'),
    path('register/', views.register, name='register'),
    # url(r'^volunteer/$', views.register, name='register'),
    # path('tickets/<int:pk>/', views.DetailView.as_view(), name='detail'),
]
