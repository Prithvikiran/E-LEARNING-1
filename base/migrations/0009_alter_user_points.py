# Generated by Django 4.0.1 on 2022-11-27 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_alter_message_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='points',
            field=models.IntegerField(default=10),
        ),
    ]
