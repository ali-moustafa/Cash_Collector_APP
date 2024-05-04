from django.db import models
from django.contrib.auth.models import User


class Employee(models.Model):
    ROLE_CHOICES = [
        ('CC', 'CashCollector'),
        ('MG', 'Manager'),
    ]

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    role = models.CharField(max_length=100, choices=ROLE_CHOICES)


class Task(models.Model):
    collector = models.ForeignKey(
        'Employee',
        on_delete=models.CASCADE,
        related_name='tasks_assigned',
        related_query_name='task',
        limit_choices_to={'role': 'CC'}
    )
    manager = models.ForeignKey(
        'Employee',
        on_delete=models.CASCADE,
        related_name='tasks_managed',
        related_query_name='task',
        limit_choices_to={'role': 'MG'}
    )
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    amount_due = models.DecimalField(max_digits=10, decimal_places=2)
    amount_due_at = models.DateTimeField()
    collected = models.BooleanField(default=False)
    delivered = models.BooleanField(default=False)
