# Generated by Django 3.2.6 on 2021-08-25 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='cover_picture',
            field=models.ImageField(default='default_cp.png', upload_to='cover_pics'),
        ),
        migrations.AddField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(default='default_pp.png', upload_to='profile_pics'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
