# Generated by Django 3.0.3 on 2020-08-27 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p2', '0013_auto_20200827_1029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postimage',
            name='images',
            field=models.FileField(upload_to=''),
        ),
    ]
