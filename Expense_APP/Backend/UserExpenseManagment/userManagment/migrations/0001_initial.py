# Generated by Django 4.1.7 on 2024-10-22 06:12

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email_add', models.EmailField(max_length=254, unique=True)),
                ('mobile_no', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('password', models.CharField(max_length=150)),
                ('user_name', models.CharField(max_length=30)),
            ],
        ),
    ]
