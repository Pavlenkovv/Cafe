# Generated by Django 3.1.4 on 2021-01-04 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_info', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermessage',
            name='message',
            field=models.TextField(max_length=200),
        ),
    ]