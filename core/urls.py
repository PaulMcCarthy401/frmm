from django.urls import path

from . import views

app_name = 'core'
urlpatterns = [
    path('', views.TicketCreate.as_view(), name='index'),
    # path('tickets/<int:pk>/', views.DetailView.as_view(), name='detail'),
]
