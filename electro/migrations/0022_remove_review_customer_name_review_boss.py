# Generated by Django 4.0.4 on 2022-11-05 01:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('electro', '0021_remove_review_boss_review_customer_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='customer_name',
        ),
        migrations.AddField(
            model_name='review',
            name='boss',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
