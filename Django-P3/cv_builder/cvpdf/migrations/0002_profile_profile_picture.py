# Generated by Django 5.1.1 on 2025-02-10 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cvpdf', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(blank=True, default='profile_pics/cv_default.jpg', null=True, upload_to='profile_pics/'),
        ),
    ]
