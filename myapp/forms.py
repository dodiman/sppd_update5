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

class InstansiForm(ModelForm):
	class Meta:
		model = Instansi
		fields = '__all__'