# Generated by Django 2.1 on 2018-08-20 17:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalInfo',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1, null=True)),
                ('phone', models.CharField(max_length=11, null=True, unique=True)),
                ('address', models.TextField(null=True, unique=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
            ],
        ),
    ]
