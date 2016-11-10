# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-29 20:21
from __future__ import unicode_literals

import costumes.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Component',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('notes', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Costume',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('character', models.CharField(max_length=200)),
                ('series', models.CharField(max_length=200)),
                ('variant', models.CharField(max_length=200)),
                ('notes', models.TextField()),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='CostumePhoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=costumes.models.costume_photo_path)),
                ('costume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='costumes.Costume')),
            ],
        ),
        migrations.CreateModel(
            name='ReferencePhoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=costumes.models.reference_photo_path)),
                ('costume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='costumes.Costume')),
            ],
        ),
        migrations.AddField(
            model_name='component',
            name='costume',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='costumes.Costume'),
        ),
    ]
