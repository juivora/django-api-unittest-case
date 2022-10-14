# Generated by Django 3.1.7 on 2021-04-09 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(editable=False, primary_key=True, serialize=False)),
                ('uploader', models.UUIDField()),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200)),
                ('origin_name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=200)),
                ('status', models.CharField(choices=[('active', 'Active'), ('deactivated', 'Deactivated')], max_length=250)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]