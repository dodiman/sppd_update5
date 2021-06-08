from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='myapp_index'),
	path('surat_perintah', views.surat_perintah, name='myapp_surat_perintah'),
	path('create_surat_perintah/', views.createSuratPerintah, name="myapp_create_surat_perintah"),
	path('show_surat_perintah/<str:pk>/', views.showSuratePerintah, name="myapp_show_surat_perintah"),
	path('update_surat_perintah/<str:pk>/', views.upadateSuratePerintah, name="myapp_update_surat_perintah"),
	path('delete_surat_perintah/<str:pk>/', views.deleteSuratPerintah, name="myapp_delete_surat_perintah"),

	path('sppd', views.sppd, name='myapp_sppd'),
	path('show_sppd/<str:pk>/', views.showSppd, name="myapp_show_sppd"),

	path('laporan', views.laporan, name='myapp_laporan'),
	path('show_laporan/<str:pk>/', views.showLaporan, name="myapp_show_laporan"),

	path('pengeluaran', views.pengeluaran, name='myapp_pengeluaran'),
	path('show_pengeluaran/<str:pk>/', views.showPengeluaran, name="myapp_show_pengeluaran"),
	path('show_rincian/<str:pk>/', views.showRincian, name="show_rincian"),

	path('pegawai', views.pegawai, name='myapp_pegawai'),
	# path('pegawai', views.pegawai, name='myapp_pegawai'),

	# path('create_order/<str:pk>/', views.createOrder, name="create_order"),
    path('update_data_pegawai/<str:pk>/', views.updatePegawai, name="myapp_update_pegawai"),
    # path('delete_order/<str:pk>/', views.deleteOrder, name="delete_order"),


    path('myadmin', views.index_admin, name='myapp_index_admin'),
	path('surat_perintah_admin', views.surat_perintah_admin, name='myapp_surat_perintah_admin'),
	path('create_surat_perintah_admin', views.createSuratPerintahAdmin, name="myapp_create_surat_perintah_admin"),
	path('show_surat_perintah_admin/<str:pk>/', views.showSuratePerintahAdmin, name="myapp_show_surat_perintah_admin"),
	path('update_surat_perintah_admin/<str:pk>/change', views.upadateSuratePerintahAdmin, name="myapp_update_surat_perintah_admin"),
	path('delete_surat_perintah_admin/<str:pk>/', views.deleteSuratePerintah, name="myapp_delete_surat_perintah_admin"),


	path('sppd_admin', views.sppdAdmin, name='myapp_sppd_admin'),
	path('create_sppd_admin', views.createSppdAdmin, name="myapp_create_sppd_admin"),
	path('update_sppd_admin/<str:pk>/change', views.upadateSppdAdmin, name="myapp_update_sppd_admin"),
	path('show_sppd_admin/<str:pk>/', views.showSppdAdmin, name="myapp_show_sppd_admin"),
	path('delete_sppd_admin/<str:pk>/', views.deleteSppdAdmin, name="myapp_delete_sppd_admin"),

	path('laporan_admin', views.laporanAdmin, name='myapp_laporan_admin'),
	# path('show_laporan_admin/<str:pk>/', views.showLaporanAdmin, name="myapp_show_laporan_admin"),

	path('pengeluaran_admin', views.pengeluaranAdmin, name='myapp_pengeluaran_admin'),
	path('create_pengeluaran_admin', views.createPengeluaranAdmin, name="myapp_create_pengeluaran_admin"),
	path('show_pengeluaran_admin/<str:pk>/', views.showPengeluaranAdmin, name="myapp_show_pengeluaran_admin"),
	path('update_pengeluaran_admin/<str:pk>/change', views.updatePengeluaranAdmin, name="myapp_update_pengeluaran_admin"),
	path('show_rincian_admin/<str:pk>/', views.showRincianAdmin, name="show_rincian_admin"),
	path('delete_pengeluaran_admin/<str:pk>/', views.deletePengeluaranAdmin, name="myapp_delete_pengeluaran_admin"),

	path('pegawai_admin', views.pegawaiAdmin, name='myapp_pegawai_admin'),
	path('create_pegawai_admin', views.createPegewaiAdmin, name="myapp_create_pegawai_admin"),
	path('update_pegawai_admin/<str:pk>/', views.updatePegawaiAdmin, name="myapp_update_pegawai_admin"),
	path('delete_pegawai_admin/<str:pk>/', views.deletePegawaiAdmin, name="myapp_delete_pegawai_admin"),
	

	path('instansi_admin', views.instansiAdmin, name='myapp_instansi_admin'),
	path('create_instansi_admin', views.createInstansiAdmin, name="myapp_create_instansi_admin"),
	path('update_instansi_admin/<str:pk>/', views.updateInstansiAdmin, name="myapp_update_instansi_admin"),
	
	path('rincian_admin', views.rincianAdmin, name='myapp_rincian_admin'),
	path('create_rincian_admin', views.createRincianAdmin, name="myapp_create_rincian_admin"),
	path('update_rincian_admin/<str:pk>/', views.updateRincianAdmin, name="myapp_update_rincian_admin"),
	path('delete_rincian_admin/<str:pk>/', views.deleteRincianAdmin, name="myapp_delete_rincian_admin"),
]
