# Generated by Django 5.0.1 on 2024-03-02 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='room_gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_number', models.IntegerField()),
                ('room_image', models.ImageField(upload_to='')),
            ],
        ),
    ]
