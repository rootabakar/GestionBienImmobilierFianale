# Generated by Django 4.1.7 on 2023-02-24 11:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_user_managers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proprietaire',
            name='username',
        ),
    ]