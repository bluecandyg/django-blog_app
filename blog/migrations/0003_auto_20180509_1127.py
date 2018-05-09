# Generated by Django 2.0.5 on 2018-05-09 02:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20180508_1133'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='test',
            field=models.TextField(default='anonymous'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
