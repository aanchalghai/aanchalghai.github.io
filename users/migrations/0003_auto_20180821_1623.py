# Generated by Django 2.1 on 2018-08-21 10:53

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_listings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listings',
            name='pictures',
            field=models.ImageField(blank=True, upload_to=users.models.user_directory_path),
        ),
    ]
