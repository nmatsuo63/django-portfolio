# Generated by Django 2.2.17 on 2020-11-15 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('image', models.ImageField(upload_to='images', verbose_name='Image')),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='images', verbose_name='Thumnail')),
                ('skill', models.CharField(max_length=100, verbose_name='Skill')),
                ('url', models.CharField(blank=True, max_length=100, null=True, verbose_name='URL')),
                ('created', models.DateField(verbose_name='Date')),
                ('description', models.TextField(verbose_name='Description')),
            ],
        ),
    ]
