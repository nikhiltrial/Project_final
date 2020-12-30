from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('ticket_view/<int:ticket_number>', views.ticket_view, name="ticket_view"),
    path('ticket_edit/<int:ticket_number>', views.ticket_edit, name="ticket_edit"),
    path('ticket_create/', views.ticket_create, name="ticket_create"),
    path('logout/', views.logout_view, name='logout_view'),
    path('count_tickets/', views.count_tickets, name='count_tickets'),

  ]
