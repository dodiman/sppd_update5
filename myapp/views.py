from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from accounts.decorators import unauthenticated_user, allowed_users, admin_only
from .models import *
from .forms import *
from django.http import HttpResponse, HttpResponseRedirect

from django.db.models import Sum, Avg
from django.core.exceptions import ObjectDoesNotExist

# manipulasi date
from datetime import date
# from django.db.models.functions import TruncMonth, TruncDate, TruncDay, TruncHour, TruncMinute, TruncSecond
from django.db.models import Count

@login_required(login_url='login')
def index(request):
	context = {}
	return render(request, 'myapp/dashboard.html', context)

@login_required(login_url='login')
def surat_perintah(request):
	suratperintah = Surat_perintah.objects.all()

	context = {
		'suratperintah': suratperintah
	}
	return render(request, 'myapp/surat_perintah.html', context)

@login_required(login_url='login')
def createSuratPerintah(request):
	form = SuratPerintahForm()

	if request.method == 'POST':
		form = SuratPerintahForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('myapp_surat_perintah')
	context = {
		'form': form
	}
	return render(request, 'myapp/create_surat_perintah_form.html', context)

@login_required(login_url='login')
def createPegewaiAdmin(request):
	form = PegawaiForm()

	if request.method == 'POST':
		form = PegawaiForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('myapp_pegawai_admin')
	context = {
		'form': form
	}
	return render(request, 'myapp/myadmin/create_pegawai_form.html', context)

@login_required(login_url='login')
def createRincianAdmin(request):
	form = RincianForm()
	if request.method == 'POST':
		form = RincianForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('myapp_rincian_admin')

	context = {
		'form': form,
		'next': next
	}
	return render(request, 'myapp/myadmin/create_pegawai_form.html', context)

@login_required(login_url='login')
def createSppdAdmin(request):
	form = SppdForm()

	if request.method == 'POST':
		form = SppdForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('myapp_sppd_admin')
	context = {
		'form': form
	}
	return render(request, 'myapp/myadmin/create_sppd_form.html', context)

@login_required(login_url='login')
def createPengeluaranAdmin(request):
	form = PengeluaranForm()

	if request.method == 'POST':
		form = PengeluaranForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('myapp_pengeluaran_admin')
	context = {
		'form': form
	}
	return render(request, 'myapp/myadmin/create_pengeluaran_form.html', context)


@login_required(login_url='login')
def createInstansiAdmin(request):
	form = InstansiForm()

	if request.method == 'POST':
		form = InstansiForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('myapp_instansi_admin')
	context = {
		'form': form
	}
	return render(request, 'myapp/myadmin/create_surat_perintah_form.html', context)

@login_required(login_url='login')
def createSuratPerintahAdmin(request):
	form = SuratPerintahForm()

	if request.method == 'POST':
		form = SuratPerintahForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('myapp_surat_perintah_admin')
	context = {
		'form': form
	}
	return render(request, 'myapp/myadmin/create_surat_perintah_form.html', context)

@login_required(login_url='login')
def showSuratePerintah(request, pk):
	instansi = Instansi.objects.first()
	suratperintah = Surat_perintah.objects.get(id=pk)
	suratperintah_pegawai = suratperintah.penanggung_jawab

	try:
		sppd = Sppd.objects.get(surat_perintah=suratperintah)
		pelaksana = sppd.pengikut.all()
		# sppd.suratperintah
	except ObjectDoesNotExist:
		sppd = None
		pelaksana = None
	
	# try:
	# 	sppd = Sppd.objects.get(surat_perintah=suratperintah)
	# 	# pelaksana = sppd.pengikut.all()
	# except Sppd.DoesNotExist:
	# 	spdd = None
	# 	# pelaksana = None

	# instansi = Instansi.objects.get(id=0)

	context = {
		'suratperintah': suratperintah,
		'sppd': sppd,
		'instansi': instansi,
		'pelaksana': pelaksana,
		'suratperintah_pegawai': suratperintah_pegawai,
	}
	# return HttpResponse(sppd)
	return render(request, 'myapp/show_surat_perintah.html', context)

@login_required(login_url='login')
def showSppd(request, pk):
	sppd = Sppd.objects.get(id=pk)
	pelaksana = sppd.pengikut.all()
	instansi = Instansi.objects.first()


	lama_perjalanan = sppd.tanggal_kembali - sppd.tanggal_kembali
	print("===========================================")
	print(type(sppd.tanggal_kembali))
	print(type(lama_perjalanan))
	# suratperintah = Surat_perintah.objects.get(id=pk)
	# suratperintah_pegawai = suratperintah.penanggung_jawab
	# sppd = Sppd.objects.get(surat_perintah=suratperintah)

	context = {
		'sppd': sppd,
		'instansi': instansi,
		'lama_perjalanan' : lama_perjalanan,
		'pelaksana': pelaksana,
		# 'suratperintah': suratperintah,
		# 'suratperintah_pegawai': suratperintah_pegawai,
	}
	return render(request, 'myapp/show_sppd.html', context)

@login_required(login_url='login')
def showPengeluaran(request, pk):
	instansi = Instansi.objects.first()
	pengeluaran = Pengeluaran.objects.get(id=pk)
	rincian = pengeluaran.rincian.all()
	total_rincian = pengeluaran.rincian.aggregate(Sum('jumlahnya'))
	# total_rincian = pengeluaran.aggregate(sum('harga'))

	# sppd = Sppd.objects.get(id=pk)
	# pelaksana = sppd.pengikut.all()

	# lama_perjalanan = sppd.tanggal_kembali - sppd.tanggal_kembali
	# print("===========================================")
	# print(type(sppd.tanggal_kembali))
	# print(type(lama_perjalanan))
	# suratperintah = Surat_perintah.objects.get(id=pk)
	# suratperintah_pegawai = suratperintah.penanggung_jawab
	# sppd = Sppd.objects.get(surat_perintah=suratperintah)

	context = {
		'pengeluaran': pengeluaran,
		'instansi': instansi,
		'rincian': rincian,
		'total_rincian': total_rincian['jumlahnya__sum'],
		# 'lama_perjalanan' : lama_perjalanan,
		# 'pelaksana': pelaksana,
		# 'suratperintah': suratperintah,
		# 'suratperintah_pegawai': suratperintah_pegawai,
	}
	return render(request, 'myapp/show_pengeluaran.html', context)

@login_required(login_url='login')
def showPengeluaranAdmin(request, pk):
	instansi = Instansi.objects.first()
	pengeluaran = Pengeluaran.objects.get(id=pk)
	rincian = pengeluaran.rincian.all()
	total_rincian = pengeluaran.rincian.aggregate(Sum('jumlahnya'))
	# total_rincian = pengeluaran.aggregate(sum('harga'))

	# sppd = Sppd.objects.get(id=pk)
	# pelaksana = sppd.pengikut.all()

	# lama_perjalanan = sppd.tanggal_kembali - sppd.tanggal_kembali
	# print("===========================================")
	# print(type(sppd.tanggal_kembali))
	# print(type(lama_perjalanan))
	# suratperintah = Surat_perintah.objects.get(id=pk)
	# suratperintah_pegawai = suratperintah.penanggung_jawab
	# sppd = Sppd.objects.get(surat_perintah=suratperintah)

	context = {
		'pengeluaran': pengeluaran,
		'rincian': rincian,
		'instansi': instansi,
		'total_rincian': total_rincian['jumlahnya__sum'],
		# 'lama_perjalanan' : lama_perjalanan,
		# 'pelaksana': pelaksana,
		# 'suratperintah': suratperintah,
		# 'suratperintah_pegawai': suratperintah_pegawai,
	}
	return render(request, 'myapp/myadmin/show_pengeluaran.html', context)

@login_required(login_url='login')
def showRincian(request, pk):
	pengeluaran = Pengeluaran.objects.get(id=pk)
	rincian = pengeluaran.rincian.all()
	total_rincian = pengeluaran.rincian.aggregate(Sum('jumlahnya'))

	# try:
	# 	sppd2 = pengeluaran.sppd
	# except ObjectDoesNotExist:
	# 	sppd2 = None

	context = {
		'pengeluaran': pengeluaran,
		'rincian': rincian,
		'total_rincian': total_rincian['jumlahnya__sum'],
	}
	return render(request, 'myapp/show_rincian.html', context)

@login_required(login_url='login')
def showRincianAdmin(request, pk):
	pengeluaran = Pengeluaran.objects.get(id=pk)
	rincian = pengeluaran.rincian.all()
	total_rincian = pengeluaran.rincian.aggregate(Sum('jumlahnya'))

	# try:
	# 	sppd2 = pengeluaran.sppd
	# except ObjectDoesNotExist:
	# 	sppd2 = None

	context = {
		'pengeluaran': pengeluaran,
		'rincian': rincian,
		'total_rincian': total_rincian['jumlahnya__sum'],
	}
	return render(request, 'myapp/myadmin/show_rincian.html', context)

@login_required(login_url='login')
def showLaporan(request, pk):
	pengeluaran = Pengeluaran.objects.get(id=pk)
	rincian = pengeluaran.rincian.all()
	total_rincian = pengeluaran.rincian.aggregate(Sum('jumlahnya'))
	# total_rincian = pengeluaran.aggregate(sum('harga'))

	# sppd = Sppd.objects.get(id=pk)
	# pelaksana = sppd.pengikut.all()

	# lama_perjalanan = sppd.tanggal_kembali - sppd.tanggal_kembali
	# print("===========================================")
	# print(type(sppd.tanggal_kembali))
	# print(type(lama_perjalanan))
	# suratperintah = Surat_perintah.objects.get(id=pk)
	# suratperintah_pegawai = suratperintah.penanggung_jawab
	# sppd = Sppd.objects.get(surat_perintah=suratperintah)

	context = {
		'pengeluaran': pengeluaran,
		'rincian': rincian,
		'total_rincian': total_rincian['jumlahnya__sum'],
		# 'lama_perjalanan' : lama_perjalanan,
		# 'pelaksana': pelaksana,
		# 'suratperintah': suratperintah,
		# 'suratperintah_pegawai': suratperintah_pegawai,
	}
	return render(request, 'myapp/show_laporan.html', context)

@login_required(login_url='login')
def upadateSuratePerintah(request, pk):
	suratperintah = Surat_perintah.objects.get(id=pk)
	form = SuratPerintahForm(instance=suratperintah)

	if request.method == 'POST':
		form = SuratPerintahForm(request.POST, instance=suratperintah)
		if form.is_valid():
			form.save()
			return redirect('myapp_surat_perintah')

	context = {'form':form}
	return render(request, 'myapp/edit_surat_perintah_form.html', context)

@login_required(login_url='login')
def deleteSuratePerintah(request, pk):
	order = Surat_perintah.objects.get(id=pk)
	order.delete()
	return redirect('myapp_surat_perintah_admin')

@login_required(login_url='login')
def deleteRincianAdmin(request, pk):
	order = Rincian.objects.get(id=pk)
	order.delete()
	return redirect('myapp_rincian_admin')

@login_required(login_url='login')
def deletePegawaiAdmin(request, pk):
	order = Pegawai.objects.get(id=pk)
	order.delete()
	return redirect('myapp_pegawai_admin')

@login_required(login_url='login')
def deletePengeluaranAdmin(request, pk):
	order = Pengeluaran.objects.get(id=pk)
	order.delete()
	return redirect('myapp_pengeluaran_admin')

@login_required(login_url='login')
def deleteSppdAdmin(request, pk):
	order = Sppd.objects.get(id=pk)
	order.delete()
	return redirect('myapp_sppd_admin')

@login_required(login_url='login')
def upadateSuratePerintahAdmin(request, pk):
	suratperintah = Surat_perintah.objects.get(id=pk)
	form = SuratPerintahForm(instance=suratperintah)

	if request.method == 'POST':
		form = SuratPerintahForm(request.POST, instance=suratperintah)
		if form.is_valid():
			form.save()
			return redirect('myapp_surat_perintah_admin')

	context = {'form':form}
	return render(request, 'myapp/myadmin/edit_surat_perintah_form.html', context)


@login_required(login_url='login')
def deleteSuratPerintah(request, pk):
	suratperintah = Surat_perintah.objects.get(id=pk)
	if request.method == "POST":
		suratperintah.delete()
		return redirect('myapp_surat_perintah')

	suratperintah.delete()
	return redirect('myapp_surat_perintah')

@login_required(login_url='login')
def rincianAdmin(request):
	rincian = Rincian.objects.all()

	context = {
		'rincian': rincian,
	}
	return render(request, 'myapp/myadmin/rincian_admin.html', context)

@login_required(login_url='login')
def sppd(request):
	sppd = Sppd.objects.all()

	context = {
		'sppd': sppd,
	}
	return render(request, 'myapp/sppd.html', context)

@login_required(login_url='login')
def laporan(request):
	pengeluaran = Pengeluaran.objects.all()
	# # total_rincian = pengeluaran.rincian.aggregate(Sum('harga'))
	# mylist = list(pengeluaran)
	# kk = ()
	# for i in range(len(mylist)):
	# 	kk[i] = mylist[i]
	# 	# kk += i
	# 	print(kk)

	# # print(kk)
	# # print(type(mylist))

	context = {
		'pengeluaran': pengeluaran,
		# 'mylist': mylist
	}
	return render(request, 'myapp/laporan.html', context)


@login_required(login_url='login')
def laporanAdmin(request):
	pengeluaran = Pengeluaran.objects.all()
	# # total_rincian = pengeluaran.rincian.aggregate(Sum('harga'))
	# mylist = list(pengeluaran)
	# kk = ()
	# for i in range(len(mylist)):
	# 	kk[i] = mylist[i]
	# 	# kk += i
	# 	print(kk)

	# # print(kk)
	# # print(type(mylist))

	context = {
		'pengeluaran': pengeluaran,
		# 'mylist': mylist
	}
	return render(request, 'myapp/myadmin/laporan.html', context)


@login_required(login_url='login')
def pengeluaran(request):
	pengeluaran = Pengeluaran.objects.all()

	context = {
		'pengeluaran': pengeluaran
	}
	return render(request, 'myapp/pengeluaran.html', context)



@login_required(login_url='login')
def pengeluaranAdmin(request):
	pengeluaran = Pengeluaran.objects.all()

	context = {
		'pengeluaran': pengeluaran
	}
	return render(request, 'myapp/myadmin/pengeluaran.html', context)


@login_required(login_url='login')
def instansiAdmin(request):
	instansi = Instansi.objects.all()

	context = {
		'instansi': instansi
	}
	return render(request, 'myapp/myadmin/instansi.html', context)

@login_required(login_url='login')
@admin_only
def pegawaiAdmin(request):
	pegawai = Pegawai.objects.all()
	form = PegawaiForm()

	if request.method == 'POST':
		#print('Printing POST:', request.POST)
		form = PegawaiForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('myapp_pegawai')

	context = {
		'pegawai': pegawai,
		'form': form
	}
	return render(request, 'myapp/myadmin/pegawai.html', context)

@login_required(login_url='login')
def pegawai(request):
	pegawai = Pegawai.objects.all()
	form = PegawaiForm()

	if request.method == 'POST':
		#print('Printing POST:', request.POST)
		form = PegawaiForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('myapp_pegawai')

	context = {
		'pegawai': pegawai,
		'form': form
	}
	return render(request, 'myapp/pegawai.html', context)


@login_required(login_url='login')
def updatePegawai(request, pk):
	pegawai = Pegawai.objects.get(id=pk)
	form = PegawaiForm(instance=pegawai)

	if request.method == 'POST':
		form = PegawaiForm(request.POST, instance=pegawai)
		if form.is_valid():
			form.save()
			return redirect('myapp_pegawai')

	context = {'form':form}
	return render(request, 'myapp/edit_pegawai_form.html', context)

@login_required(login_url='login')
@admin_only
def updateRincianAdmin(request, pk):
	rincian = Rincian.objects.get(id=pk)
	form = RincianForm(instance=rincian)

	if request.method == 'POST':
		form = RincianForm(request.POST, instance=rincian)
		if form.is_valid():
			form.save()
			return redirect('myapp_rincian_admin')

	context = {'form':form}
	return render(request, 'myapp/myadmin/edit_rincian_form.html', context)


@login_required(login_url='login')
@admin_only
def updatePengeluaranAdmin(request, pk):
	pengeluaran = Pengeluaran.objects.get(id=pk)
	form = PengeluaranForm(instance=pengeluaran)

	if request.method == 'POST':
		form = PengeluaranForm(request.POST, instance=pengeluaran)
		if form.is_valid():
			form.save()
			return redirect('myapp_pengeluaran_admin')

	context = {'form':form}
	return render(request, 'myapp/myadmin/edit_pengeluaran_form.html', context)


@login_required(login_url='login')
@admin_only
def upadateSppdAdmin(request, pk):
	pegawai = Pegawai.objects.get(id=pk)
	form = PegawaiForm(instance=sppd)

	if request.method == 'POST':
		form = PegawaiForm(request.POST, instance=pegawai)
		if form.is_valid():
			form.save()
			return redirect('pegawai_admin')

	context = {'form':form}
	return render(request, 'myapp/myadmin/edit_pegawai_form.html', context)

@login_required(login_url='login')
@admin_only
def upadateSppdAdmin(request, pk):
	sppd = Sppd.objects.get(id=pk)
	form = SppdForm(instance=sppd)

	if request.method == 'POST':
		form = SppdForm(request.POST, instance=sppd)
		if form.is_valid():
			form.save()
			return redirect('myapp_sppd_admin')

	context = {'form':form}
	return render(request, 'myapp/myadmin/edit_sppd_form.html', context)


@login_required(login_url='login')
@admin_only
def updateInstansiAdmin(request, pk):
	instansi = Instansi.objects.get(id=pk)
	form = InstansiForm(instance=instansi)

	if request.method == 'POST':
		form = InstansiForm(request.POST, instance=instansi)
		if form.is_valid():
			form.save()
			return redirect('myapp_instansi_admin')

	context = {'form':form}
	return render(request, 'myapp/myadmin/edit_instansi_form.html', context)



@login_required(login_url='login')
@admin_only
def updatePegawaiAdmin(request, pk):
	pegawai = Pegawai.objects.get(id=pk)
	form = PegawaiForm(instance=pegawai)

	if request.method == 'POST':
		form = PegawaiForm(request.POST, instance=pegawai)
		if form.is_valid():
			form.save()
			return redirect('myapp_pegawai_admin')

	context = {'form':form}
	return render(request, 'myapp/myadmin/edit_pegawai_form.html', context)


# ====================================================admin=================================
@login_required(login_url='login')
@admin_only
def index_admin(request):
	context = {}  
	return render(request, 'myapp/myadmin/dashboard.html', context)


@login_required(login_url='login')
@admin_only
def surat_perintah_admin(request):
	suratperintah = Surat_perintah.objects.all()

	context = {
		'suratperintah': suratperintah
	}
	return render(request, 'myapp/myadmin/surat_perintah.html', context)

@login_required(login_url='login')
@admin_only
def showSuratePerintahAdmin(request, pk):
	instansi = Instansi.objects.first()
	suratperintah = Surat_perintah.objects.get(id=pk)
	suratperintah_pegawai = suratperintah.penanggung_jawab

	try:
		sppd = Sppd.objects.get(surat_perintah=suratperintah)
		pelaksana = sppd.pengikut.all()
		# sppd.suratperintah
	except ObjectDoesNotExist:
		sppd = None
		pelaksana = None
	
	# try:
	# 	sppd = Sppd.objects.get(surat_perintah=suratperintah)
	# 	# pelaksana = sppd.pengikut.all()
	# except Sppd.DoesNotExist:
	# 	spdd = None
	# 	# pelaksana = None

	# instansi = Instansi.objects.get(id=0)

	context = {
		'suratperintah': suratperintah,
		'sppd': sppd,
		'instansi': instansi,
		'pelaksana': pelaksana,
		'suratperintah_pegawai': suratperintah_pegawai,
	}
	# return HttpResponse(sppd)
	return render(request, 'myapp/myadmin/show_surat_perintah.html', context)

@login_required(login_url='login')
@admin_only
def sppdAdmin(request):
	sppd = Sppd.objects.all()

	context = {
		'sppd': sppd,
	}
	return render(request, 'myapp/myadmin/sppd.html', context)


@login_required(login_url='login')
@admin_only
def showSppdAdmin(request, pk):
	instansi = Instansi.objects.first()	
	sppd = Sppd.objects.get(id=pk)
	pelaksana = sppd.pengikut.all()

	lama_perjalanan = sppd.tanggal_kembali - sppd.tanggal_kembali
	print("===========================================")
	print(type(sppd.tanggal_kembali))
	print(type(lama_perjalanan))
	# suratperintah = Surat_perintah.objects.get(id=pk)
	# suratperintah_pegawai = suratperintah.penanggung_jawab
	# sppd = Sppd.objects.get(surat_perintah=suratperintah)

	context = {
		'instansi': instansi,
		'sppd': sppd,
		'lama_perjalanan' : lama_perjalanan,
		'pelaksana': pelaksana,
		# 'suratperintah': suratperintah,
		# 'suratperintah_pegawai': suratperintah_pegawai,
	}
	return render(request, 'myapp/myadmin/show_sppd.html', context)