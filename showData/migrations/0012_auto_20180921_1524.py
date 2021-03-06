# Generated by Django 2.0.7 on 2018-09-21 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('showData', '0011_auto_20180921_1401'),
    ]

    operations = [
        migrations.AddField(
            model_name='linetxt',
            name='c_imei',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='linetxt',
            name='c_isp',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='linetxt',
            name='c_mac',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='linetxt',
            name='c_rsrp',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='linetxt',
            name='machine_type',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='linetxt',
            name='t_ip',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='linetxt',
            name='t_mac',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
    ]
