# Generated by Django 4.1.4 on 2022-12-12 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0003_rename_topics_topic'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='featured_image',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to=''),
        ),
    ]