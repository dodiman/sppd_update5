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
	path('pegawai', views.pegawai, name='myapp_pegawai'),

	# path('create_order/<str:pk>/', views.createOrder, name="create_order"),
    path('update_data_pegawai/<str:pk>/', views.updatePegawai, name="myapp_update_pegawai"),
    # path('delete_order/<str:pk>/', views.deleteOrder, name="delete_order"),

]