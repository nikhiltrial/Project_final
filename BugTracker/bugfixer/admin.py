from django.contrib import admin
from .models import Ticket


class TicketAdmin(admin.ModelAdmin):
    list_display = ['id', 'assignee', 'created', 'date', 'status']


# Register your models here.
admin.site.register(Ticket, TicketAdmin)
