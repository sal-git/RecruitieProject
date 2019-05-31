# Generated by Django 2.1.1 on 2019-05-30 05:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recruitie', '0004_auto_20190529_1700'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidatenote',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='leadnote',
            name='user_id',
        ),
        migrations.AddField(
            model_name='candidatenote',
            name='user',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='candidate_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='leadnote',
            name='user',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='lead_user', to=settings.AUTH_USER_MODEL),
        ),
    ]