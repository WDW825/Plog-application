# Generated by Django 5.1.1 on 2024-11-05 11:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post_feed', '0004_post_post_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Post',
        ),
    ]
