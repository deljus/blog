# Generated by Django 3.0.5 on 2020-05-11 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='img/default_user.jpg', upload_to='uploads/%Y/%m/%d'),
        ),
    ]
