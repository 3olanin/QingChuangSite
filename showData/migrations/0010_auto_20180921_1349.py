# Generated by Django 2.0.7 on 2018-09-21 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('showData', '0009_auto_20180804_1712'),
    ]

    operations = [
        migrations.AddField(
            model_name='filetxt',
            name='machine_type',
            field=models.IntegerField(default=0, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='filetxt',
            name='t_ip',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='filetxt',
            name='t_mac',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
    ]
