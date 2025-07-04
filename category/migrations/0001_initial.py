# Generated by Django 5.1.7 on 2025-06-30 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=15, unique=True)),
                ('slug', models.SlugField(blank=True, max_length=100, null=True, unique=True)),
                ('description', models.TextField(blank=True, max_length=255)),
                ('cat_img', models.ImageField(blank=True, upload_to='photos/categories')),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
            },
        ),
    ]
