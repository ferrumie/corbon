# Generated by Django 3.0.8 on 2020-07-04 21:36

import corbonmain.storage_backends
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corbonapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrivateDocument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('upload', models.FileField(storage=corbonmain.storage_backends.PrivateMediaStorage(), upload_to='')),
            ],
        ),
    ]
