# Generated by Django 5.1.4 on 2025-03-05 14:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='news',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='news.news'),
        ),
    ]
