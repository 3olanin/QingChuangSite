# Generated by Django 2.0.7 on 2018-08-01 08:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('showData', '0006_linetxt_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='FilePns',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fileName', models.CharField(max_length=255)),
                ('store_time', models.BigIntegerField()),
                ('t_mac', models.CharField(max_length=255)),
                ('t_ip', models.CharField(max_length=255)),
                ('t_date', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='LinePns',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store_time', models.BigIntegerField()),
                ('t_mac', models.CharField(max_length=255)),
                ('t_ip', models.CharField(max_length=255)),
                ('t_date', models.CharField(max_length=255)),
                ('c_mac', models.CharField(max_length=255)),
                ('c_imei', models.CharField(max_length=255)),
                ('c_imsi', models.CharField(max_length=255)),
                ('c_date', models.CharField(max_length=255)),
                ('c_rsrp', models.CharField(max_length=255)),
                ('c_lon', models.CharField(max_length=255)),
                ('c_lat', models.CharField(max_length=255)),
                ('c_isp', models.CharField(max_length=255)),
                ('file', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='showData.FilePns')),
            ],
        ),
    ]
