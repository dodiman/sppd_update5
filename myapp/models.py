from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import Sum, Avg


class Biaya(models.Model):
	nama = models.CharField(max_length=200, null=True)
	status = models.CharField(max_length=200, null=True)
	created_at = models.DateTimeField(auto_now_add=True, null=True)
	updated_at = models.DateTimeField(auto_now=True, null=True)

	# class Meta:
	# 	ordering = ['nama']

	def __str__(self):
		return '%s' % (self.nama)

class Pegawai(models.Model):
	GOLONGAN = (
			('2A', '2A'),
			('2B', '2B'),
			('2C', '2C'),
			('2D', '2D'),
			('3A', '3A'),
			('3B', '3B'),
			('3C', '3C'),
			('3D', '3D'),
			('4A', '4A'),
			)

	nip = models.CharField(max_length=200, null=True)
	nama = models.CharField(max_length=200, null=True)
	skpd = models.CharField(max_length=200, null=True)
	pangkat = models.CharField(max_length=200, null=True)
	golongan = models.CharField(max_length=200, null=True, choices=GOLONGAN)
	jabatan = models.CharField(max_length=200, null=True)
	status = models.CharField(max_length=200, null=True)
	created_at = models.DateTimeField(auto_now_add=True, null=True)
	updated_at = models.DateTimeField(auto_now=True, null=True)

	def __str__(self):
		return self.nama

class Instansi(models.Model):
	nama = models.CharField(max_length=200, null=True)
	alamat = models.CharField(max_length=200, null=True)
	telepon = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)
	situs = models.CharField(max_length=200, null=True)
	logo = models.CharField(max_length=200, null=True)
	status = models.CharField(max_length=200, null=True)
	created_at = models.DateTimeField(auto_now_add=True, null=True)
	updated_at = models.DateTimeField(auto_now=True, null=True)

	class Meta:
		ordering = ['nama']

	def __str__(self):
		return self.nama


class Surat_perintah(models.Model):
	nomor = models.CharField(max_length=200, null=True)
	uraian = models.CharField(max_length=200, null=True)
	tanggal = models.DateField(null=True)
	penanggung_jawab = models.ForeignKey(Pegawai, on_delete=models.CASCADE)
	# status = models.CharField(max_length=200, null=True)
	created_at = models.DateTimeField(auto_now_add=True, null=True)
	updated_at = models.DateTimeField(auto_now=True, null=True)

	class Meta:
		ordering = ['nomor']

	def __str__(self):
		return self.nomor


class Sppd(models.Model):
	nomor = models.CharField(max_length=200, null=True)
	perjalanan = models.CharField(max_length=200, null=True)
	tempat_berangkat = models.CharField(max_length=200, null=True)
	tempat_tujuan = models.CharField(max_length=200, null=True)
	tanggal_berangkat = models.DateField(null=True)
	tanggal_kembali = models.DateField(null=True)
	pengikut = models.ManyToManyField(Pegawai)
	keterangan = models.CharField(max_length=200, null=True)
	instansi = models.ForeignKey(Instansi, on_delete=models.CASCADE)
	surat_perintah = models.OneToOneField(Surat_perintah, null=True, on_delete=models.CASCADE)

	created_at = models.DateTimeField(auto_now_add=True, null=True)
	updated_at = models.DateTimeField(auto_now=True, null=True)

	class Meta:
		ordering = ['nomor']

	def __str__(self):
		return '%s' % (self.nomor)

class Rincian(models.Model):
	uraian = models.CharField(max_length=200, null=True)
	biaya = models.OneToOneField(Biaya, null=True, on_delete=models.CASCADE)
	qty = models.PositiveIntegerField()
	satuan = models.CharField(max_length=200, null=True)
	harga = models.IntegerField()
	created_at = models.DateTimeField(auto_now_add=True, null=True)
	updated_at = models.DateTimeField(auto_now=True, null=True)

	# class Meta:
	# 	ordering = ['uraian']

	def __str__(self):
		return self.uraian


class Pengeluaran(models.Model):
	nomor_bukti_pengeluaran = models.CharField(max_length=200, null=True)
	sumber_dana = models.CharField(max_length=200, null=True)
	keperluan = models.CharField(max_length=200, null=True)
	tanggal = models.DateField(null=True)
	keterangan = models.CharField(max_length=200, null=True)
	sppd = models.OneToOneField(Sppd, null=True, on_delete=models.CASCADE)
	rincian = models.ManyToManyField(Rincian)
	created_at = models.DateTimeField(auto_now_add=True, null=True)
	updated_at = models.DateTimeField(auto_now=True, null=True)

	# class Meta:
	# 	ordering = ['nomor_bukti_pengeluaran']

	def __str__(self):
		return '%s' % (self.nomor_bukti_pengeluaran)

	@property
	def total_nya(self):
		return self.rincian.aggregate(Sum('harga'))

class Anggaran(models.Model):
	
	PERIODE = (
			('Murni', 'Murni'),
			('Perubahan', 'Perubahan'),)
			

	tahun = models.CharField(max_length=200, null=True)
	dana = models.CharField(max_length=200, null=True)
	periode = models.CharField(max_length=200, null=True, choices=PERIODE)
	created_at = models.DateTimeField(auto_now_add=True, null=True)
	updated_at = models.DateTimeField(auto_now=True, null=True)

	# class Meta:
	# 	ordering = ['nama']

	def __str__(self):
		return '%s' % (self.tahun)

# simpan otomatis one to one
# @receiver(post_save, sender=Surat_perintah)
# def create_sppd(sender, instance, created, **kwargs):
# 	if created:
# 		# group = Group.objects.get(name='customer')
# 		# instance.groups.add(group)
# 		Sppd.objects.create(
# 			surat_perintah=instance,
# 			# name=instance.username,
# 			)
# 		print('sppd create!')

# @receiver(post_save, sender=Surat_perintah)
# def update_sppd(sender, instance, created, **kwargs):
# 	if created == False:
# 		instance.sppd.save()
# 		print('sppd update')