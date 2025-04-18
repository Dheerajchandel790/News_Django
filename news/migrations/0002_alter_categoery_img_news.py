# Generated by Django 5.1.4 on 2025-01-19 07:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoery',
            name='img',
            field=models.ImageField(upload_to='cate/'),
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('img', models.ImageField(upload_to='News/')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('Categoery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.categoery')),
            ],
            options={
                'verbose_name_plural': 'News',
            },
        ),
    ]
