# Generated by Django 3.0.3 on 2020-03-31 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p2', '0006_auto_20200331_0507'),
    ]

    operations = [
        migrations.DeleteModel(
            name='tot',
        ),
        migrations.AlterField(
            model_name='work',
            name='tot_title',
            field=models.TextField(),
        ),
    ]
