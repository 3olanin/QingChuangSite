# Generated by Django 2.0.7 on 2018-08-04 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('showData', '0008_auto_20180802_1826'),
    ]

    operations = [
        migrations.AddField(
            model_name='filepns',
            name='t_date_stamp',
            field=models.BigIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='filetxt',
            name='t_time_stamp',
            field=models.BigIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='linepns',
            name='c_date_stamp',
            field=models.BigIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='linepns',
            name='t_date_stamp',
            field=models.BigIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='linetxt',
            name='c_time_stamp',
            field=models.BigIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='linetxt',
            name='t_time_stamp',
            field=models.BigIntegerField(default=0),
            preserve_default=False,
        ),
    ]