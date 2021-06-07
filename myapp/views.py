from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from django.http import HttpResponse

from django.db.models import Sum, Avg
from django.core.exceptions import ObjectDoesNotExist

# manipulasi date
from datetime import date

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
def showSuratePerintah(request, pk):
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
		'pelaksana': pelaksana,
		'suratperintah_pegawai': suratperintah_pegawai,
	}
	# return HttpResponse(sppd)
	return render(request, 'myapp/show_surat_perintah.html', context)

@login_required(login_url='login')
def showSppd(request, pk):
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
		'sppd': sppd,
		'lama_perjalanan' : lama_perjalanan,
		'pelaksana': pelaksana,
		# 'suratperintah': suratperintah,
		# 'suratperintah_pegawai': suratperintah_pegawai,
	}
	return render(request, 'myapp/show_sppd.html', context)

@login_required(login_url='login')
def showPengeluaran(request, pk):
	pengeluaran = Pengeluaran.objects.get(id=pk)
	rincian = pengeluaran.rincian.all()
	total_rincian = pengeluaran.rincian.aggregate(Sum('harga'))
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
		'total_rincian': total_rincian['harga__sum'],
		# 'lama_perjalanan' : lama_perjalanan,
		# 'pelaksana': pelaksana,
		# 'suratperintah': suratperintah,
		# 'suratperintah_pegawai': suratperintah_pegawai,
	}
	return render(request, 'myapp/show_pengeluaran.html', context)

@login_required(login_url='login')
def showRincian(request, pk):
	pengeluaran = Pengeluaran.objects.get(id=pk)
	rincian = pengeluaran.rincian.all()
	total_rincian = pengeluaran.rincian.aggregate(Sum('harga'))
	context = {
		'pengeluaran': pengeluaran,
		'rincian': rincian,
		'total_rincian': total_rincian['harga__sum'],
	}
	return render(request, 'myapp/show_rincian.html', context)


@login_required(login_url='login')
def showLaporan(request, pk):
	pengeluaran = Pengeluaran.objects.get(id=pk)
	rincian = pengeluaran.rincian.all()
	total_rincian = pengeluaran.rincian.aggregate(Sum('harga'))
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
		'total_rincian': total_rincian['harga__sum'],
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
def deleteSuratPerintah(request, pk):
	suratperintah = Surat_perintah.objects.get(id=pk)
	if request.method == "POST":
		suratperintah.delete()
		return redirect('myapp_surat_perintah')

	suratperintah.delete()
	return redirect('myapp_surat_perintah')


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
def pengeluaran(request):
	pengeluaran = Pengeluaran.objects.all()

	context = {
		'pengeluaran': pengeluaran
	}
	return render(request, 'myapp/pengeluaran.html', context)

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

	