# Generated by Django 4.0.4 on 2022-08-27 05:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('electro', '0005_customer_request_connect'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer_request',
            name='connect',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]