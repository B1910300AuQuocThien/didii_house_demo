# Generated by Django 4.1.1 on 2022-11-13 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('didii', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='img',
            field=models.ImageField(default=2101, upload_to='images'),
            preserve_default=False,
        ),
    ]
