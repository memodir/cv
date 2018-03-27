# Generated by Django 2.0.3 on 2018-03-27 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0002_auto_20180327_0416'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='birthday',
            field=models.DateField(blank=True, null=True, verbose_name='Birthday'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='photo_crop',
            field=models.ImageField(blank=True, null=True, upload_to='thumbnails/profile_photo/%Y/%m'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='photo',
            field=models.ImageField(blank=True, help_text='A 256x256 image for your profile.', null=True, upload_to='profile_photo/%Y/%m'),
        ),
    ]
