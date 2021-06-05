from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='myapp_index'),
	path('surat_perintah', views.surat_perintah, name='myapp_surat_perintah'),
	path('sppd', views.sppd, name='myapp_sppd'),
	path('laporan', views.laporan, name='myapp_laporan'),
	path('pegawai', views.pegawai, name='myapp_pegawai'),
]