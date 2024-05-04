# Generated by Django 5.0.4 on 2024-05-04 10:09

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('CC', 'CashCollector'), ('MG', 'Manager')], max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('amount_due', models.DecimalField(decimal_places=2, max_digits=10)),
                ('amount_due_at', models.DateTimeField()),
                ('collected', models.BooleanField(default=False)),
                ('delivered', models.BooleanField(default=False)),
                ('collector', models.ForeignKey(limit_choices_to={'role': 'CC'}, on_delete=django.db.models.deletion.CASCADE, related_name='tasks_assigned', related_query_name='task', to='myapp.employee')),
                ('manager', models.ForeignKey(limit_choices_to={'role': 'MG'}, on_delete=django.db.models.deletion.CASCADE, related_name='tasks_managed', related_query_name='task', to='myapp.employee')),
            ],
        ),
    ]
