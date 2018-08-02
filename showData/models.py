from django.db import models

# Create your models here.
class FileTxt(models.Model):
	fileName = models.CharField(max_length=255)
	t_identifier = models.CharField(max_length=255)
	t_time = models.CharField(max_length=255)
	def __str__(self):
		return self.fileName


class LineTxt(models.Model):
	file = models.ForeignKey(FileTxt, on_delete=models.CASCADE)
	t_identifier = models.CharField(max_length=255)
	t_time = models.CharField(max_length=255)
	c_imsi = models.CharField(max_length=255)
	c_tmsi = models.CharField(max_length=255)
	c_fcn = models.CharField(max_length=255)
	c_time = models.CharField(max_length=255)
	c_lon = models.CharField(max_length=255)
	c_lat = models.CharField(max_length=255)


class FilePns(models.Model):
	fileName = models.CharField(max_length=255)
	store_time = models.BigIntegerField()
	t_mac = models.CharField(max_length=255)
	t_ip = models.CharField(max_length=255)
	t_date = models.CharField(max_length=255)
	def __str__(self):
		return self.fileName

class LinePns(models.Model):
	file = models.ForeignKey(FilePns, on_delete=models.CASCADE)
	store_time = models.BigIntegerField()
	t_mac = models.CharField(max_length=255)
	t_ip = models.CharField(max_length=255)
	t_date = models.CharField(max_length=255)
	c_mac = models.CharField(max_length=255)
	c_imei = models.CharField(max_length=255)
	c_imsi = models.CharField(max_length=255)
	c_date = models.CharField(max_length=255)
	c_rsrp = models.CharField(max_length=255)
	c_lon = models.CharField(max_length=255)
	c_lat = models.CharField(max_length=255)
	c_isp = models.CharField(max_length=255)