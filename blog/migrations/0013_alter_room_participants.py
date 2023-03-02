# Generated by Django 4.0.1 on 2022-11-27 16:22

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0012_rename_comment_message_rename_blog_post_room_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='participants',
            field=models.ManyToManyField(blank='True', related_name='visitors', to=settings.AUTH_USER_MODEL),
        ),
    ]
