# Generated by Django 3.1.4 on 2021-03-30 21:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('voting', '0005_auto_20210330_1754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eleitor',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='eleitor', to=settings.AUTH_USER_MODEL),
        ),
    ]