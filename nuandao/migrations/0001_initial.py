# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-11 09:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publish_date', models.DateTimeField(null=True)),
                ('last_edit_date', models.DateTimeField(null=True)),
                ('article_title', models.CharField(max_length=48)),
                ('article_subtitle', models.CharField(blank=True, max_length=80)),
                ('article_describe', models.TextField(blank=True, max_length=200)),
                ('article_data', models.TextField(blank=True)),
                ('article_show', models.BooleanField(default=True, verbose_name='是否公开显示')),
                ('article_read_count', models.IntegerField(blank=True, null=True, verbose_name='浏览次数')),
            ],
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(max_length=28)),
                ('author_email', models.EmailField(blank=True, max_length=254)),
                ('author_introduction', models.CharField(blank=True, max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=63)),
                ('article_count', models.IntegerField(editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='article_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Category', to='nuandao.Category'),
        ),
        migrations.AddField(
            model_name='article',
            name='article_tags',
            field=models.ManyToManyField(blank=True, to='nuandao.Tag'),
        ),
        migrations.AddField(
            model_name='article',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='nuandao.Author'),
        ),
    ]
