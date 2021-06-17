from django.forms import ModelForm
from .models import *
from django.db.models import Q

class PegawaiForm(ModelForm):
	
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['nama'].widget.attrs.update({'class': 'form-control'})
		self.fields['nip'].widget.attrs.update({'class': 'form-control'})
		self.fields['pangkat'].widget.attrs.update({'class': 'form-control'})
		self.fields['golongan'].widget.attrs.update({'class': 'form-control'})
		self.fields['jabatan'].widget.attrs.update({'class': 'form-control'})
		self.fields['status_pegawai'].widget.attrs.update({'class': 'form-control'})

	class Meta:
		model = Pegawai
		fields = '__all__'

class SuratPerintahForm(ModelForm):

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['nomor'].widget.attrs.update({'class': 'form-control'})
		self.fields['uraian'].widget.attrs.update({'class': 'form-control'})
		self.fields['tanggal'].widget.attrs.update({
				'class': 'form-control',
				'readonly': 'readonly'
			})
		self.fields['penanggung_jawab'].widget.attrs.update({'class': 'form-control'})
		self.fields['penanggung_jawab'].queryset = Pegawai.objects.filter(Q(jabatan='Kepala Dinas Kominfo Persandian dan Statistik') | Q(jabatan='Sekretaris'))
		self.fields['koordinator'].widget.attrs.update({'class': 'form-control'})
		self.fields['pengikut'].widget.attrs.update({'class': 'form-control'})

	class Meta:
		model = Surat_perintah
		fields = '__all__'

class SppdForm(ModelForm):

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['nomor'].widget.attrs.update({'class': 'form-control'})
		self.fields['maksud_perjalanan'].widget.attrs.update({'class': 'form-control'})
		self.fields['tempat_berangkat'].widget.attrs.update({'class': 'form-control'})
		self.fields['tempat_tujuan'].widget.attrs.update({'class': 'form-control'})
		self.fields['tanggal_berangkat'].widget.attrs.update({
				'class': 'form-control',
				'readonly': 'readonly'
			})

		self.fields['tanggal_kembali'].widget.attrs.update({
				'class': 'form-control',
				'readonly': 'readonly'
			})
		self.fields['keterangan'].widget.attrs.update({'class': 'form-control'})
		self.fields['surat_perintah'].widget.attrs.update({'class': 'form-control'})
		self.fields['surat_perintah'].error_messages.update({'unique': 'Nomor Surat Perintah Telah Digunakan '})

	class Meta:
		model = Sppd
		fields = '__all__'

class PengeluaranForm(ModelForm):

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['nomor_bukti_pengeluaran'].widget.attrs.update({'class': 'form-control'})
		self.fields['sumber_dana'].widget.attrs.update({'class': 'form-control'})
		self.fields['keperluan'].widget.attrs.update({'class': 'form-control'})
		
		self.fields['tanggal'].widget.attrs.update({
				'class': 'form-control',
				'readonly': 'readonly'
			})

		self.fields['keterangan'].widget.attrs.update({'class': 'form-control'})
		self.fields['pegawai'].widget.attrs.update({'class': 'form-control'})
		self.fields['sppd'].widget.attrs.update({'class': 'form-control'})
		self.fields['sppd'].error_messages.update({'unique': 'Nomor SPPD Telah Digunakan '})
		self.fields['rincian'].widget.attrs.update({'class': 'form-control'})

	class Meta:
		model = Pengeluaran
		fields = '__all__'

class InstansiForm(ModelForm):

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['nama'].widget.attrs.update({'class': 'form-control'})
		self.fields['alamat'].widget.attrs.update({'class': 'form-control'})
		self.fields['telepon'].widget.attrs.update({'class': 'form-control'})
		
		self.fields['email'].widget.attrs.update({'class': 'form-control'})
		self.fields['situs'].widget.attrs.update({'class': 'form-control'})
		self.fields['logo'].widget.attrs.update({'class': 'form-control'})

	class Meta:
		model = Instansi
		fields = '__all__'

class RincianForm(ModelForm):

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['uraian'].widget.attrs.update({'class': 'form-control'})
		self.fields['kuantitas'].widget.attrs.update({'class': 'form-control'})
		self.fields['satuan'].widget.attrs.update({'class': 'form-control'})

		self.fields['harga'].widget.attrs.update({'class': 'form-control'})
		
	class Meta:
		model = Rincian
		fields = ['uraian', 'kuantitas', 'satuan','harga']