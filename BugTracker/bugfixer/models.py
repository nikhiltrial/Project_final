from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.core.validators import MinValueValidator


class Ticket(models.Model):
    STATUS_CHOICES = [('OPEN', 'Open'), ('IN PROGRESS', 'In Progress'), ('REVIEW', 'In Review'), ('CLOSED', 'Closed')]
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
    status = models.CharField(choices=STATUS_CHOICES, max_length=30, default='OPEN')
    steps_reproduce = models.TextField(null=True)
    num_of_ppl_affected = models.PositiveIntegerField(null=True, validators=[MinValueValidator(1)])
    url = models.URLField(max_length=200, blank=False)
    assignee = models.ForeignKey(User, related_name='assignee_staff', on_delete=models.PROTECT,
                                 blank=False, null=True)
    created = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, default=1)
