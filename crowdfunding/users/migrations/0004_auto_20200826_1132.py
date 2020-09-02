# Generated by Django 3.0.8 on 2020-08-26 11:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_supporter'),
    ]

    operations = [
        migrations.CreateModel(
            name='SupporterProfile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='supporter', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('bio', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Supporter',
        ),
    ]
