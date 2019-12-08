# Generated by Django 3.0 on 2019-12-06 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=500)),
                ('content', models.TextField()),
                ('blog_image', models.FileField(upload_to='uploads')),
                ('author', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='published date')),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=250)),
                ('body', models.TextField()),
                ('course_image', models.FileField(upload_to='uploads')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('event_image', models.FileField(upload_to='uploads')),
                ('event_date', models.DateTimeField(verbose_name='Event Date')),
                ('created_at', models.DateTimeField(verbose_name='published date')),
            ],
        ),
    ]