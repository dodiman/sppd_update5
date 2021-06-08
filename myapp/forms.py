from django.forms import ModelForm
from .models import *

class PegawaiForm(ModelForm):
	class Meta:
		model = Pegawai
		fields = '__all__'

class SuratPerintahForm(ModelForm):
	class Meta:
		model = Surat_perintah
		fields = '__all__'

class SppdForm(ModelForm):
	class Meta:
		model = Sppd
		fields = '__all__'

class PengeluaranForm(ModelForm):
	class Meta:
		model = Pengeluaran
		fields = '__all__'

class InstansiForm(ModelForm):
	class Meta:
		model = Instansi
		fields = '__all__'

class RincianForm(ModelForm):
	class Meta:
		model = Rincian
		fields = ['uraian', 'kuantitas', 'satuan','harga']