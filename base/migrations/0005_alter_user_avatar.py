# Generated by Django 4.0.1 on 2022-11-23 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_alter_user_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(default='/feynman/static/images/avatar.svg', null=True, upload_to=''),
        ),
    ]
