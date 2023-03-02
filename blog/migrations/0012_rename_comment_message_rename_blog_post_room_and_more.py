# Generated by Django 4.0.1 on 2022-11-27 16:17

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0011_alter_blog_post_participants'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comment',
            new_name='Message',
        ),
        migrations.RenameModel(
            old_name='Blog_Post',
            new_name='Room',
        ),
        migrations.RenameModel(
            old_name='Blog_Topic',
            new_name='Topic',
        ),
    ]