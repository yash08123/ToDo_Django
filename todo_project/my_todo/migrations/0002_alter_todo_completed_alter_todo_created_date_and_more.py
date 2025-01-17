# Generated by Django 5.1.4 on 2025-01-05 15:37

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_todo', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='completed',
            field=models.BooleanField(db_index=True, default=False),
        ),
        migrations.AlterField(
            model_name='todo',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, db_index=True),
        ),
        migrations.AlterField(
            model_name='todo',
            name='title',
            field=models.CharField(db_index=True, max_length=200),
        ),
        migrations.AddIndex(
            model_name='todo',
            index=models.Index(fields=['user', 'completed'], name='my_todo_tod_user_id_63857c_idx'),
        ),
        migrations.AddIndex(
            model_name='todo',
            index=models.Index(fields=['user', 'created_date'], name='my_todo_tod_user_id_61d4a0_idx'),
        ),
    ]
