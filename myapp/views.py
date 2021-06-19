from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from accounts.decorators import unauthenticated_user, allowed_users, admin_only
from .models import *
from .forms import *
from django.http import HttpResponse, HttpResponseRedirect

from django.db.models import Sum, Avg
from django.core.exceptions import ObjectDoesNotExist

# json
# from django.http import JsonResponse

# manipulasi date
from datetime import date
# from django.db.models.functions import TruncMonth, TruncDate, TruncDay, TruncHour, TruncMinute, TruncSecond
from django.db.models import Count

@login_required(login_url='login')
def index(request):
	context = {}
	return render(request, 'myapp/umum/dashboard.html', context)

@login_required(login_url='login')
@admin_only
def surat_perintah(request):
	suratperintah = Surat_perintah.objects.all()

	context = {
		'suratperintah': suratperintah
	}
	return render(request, 'myapp/surat_perintah.html', context)

@login_required(login_url='login')
@admin_only
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
@admin_only
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
@admin_only
def createRincianAdmin(request):
	form = RincianForm()
	if request.method == 'POST':
		form = RincianForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('myapp_rincian_admin')

	context = {
		'form': form,
	}
	return render(request, 'myapp/myadmin/create_rincian_form.html', context)

@login_required(login_url='login')
@admin_only
def createSppdAdmin(request, pk):
	data_terakhir = Sppd.objects.latest('created_at')
	suratperintah = Surat_perintah.objects.get(nomor=pk)

	form = SppdForm()

	if request.method == 'POST':
		# mutable = request.POST._mutable
		# request.POST._mutable = True
		# request.POST['surat_perintah'] = suratperintah.nomor
		# request.POST._mutable = mutable


		# membuat manipasi value post
		post = request.POST.copy() 			# make it mutable  # typedata post = queryset
		post_d = post.dict()
		tanggalnya = post_d.get('tanggal')
		
		
		# mengubah angka ke romawi
		num_map = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'),
		           (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]

		def num2roman(num):

		    roman = ''

		    while num > 0:
		        for i, r in num_map:
		            while num >= i:
		                roman += r
		                num -= i

		    return roman


		tahun = int(tanggalnya[:4])
		bulan = int(tanggalnya[5:7])
		bulan = num2roman(bulan)

		nomor_str = '001'
		if data_terakhir.exists():
			gabung = data_terakhir.nomor
			nomor = int(gabung[:3]) + 1
			nomor_str = '%03d' % nomor

		no_sppd = nomor_str + "/SPPD/DISKOMINFO-PB/" + bulan + "/" + str(tahun)

		post['nomor'] = no_sppd

		request.POST = post

		# print(request.POST)

		form = SppdForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('myapp_sppd_admin')
	context = {
		'form': form,
		'suratperintah': suratperintah
	}
	return render(request, 'myapp/myadmin/create_sppd_form.html', context)

@login_required(login_url='login')
@admin_only
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
@admin_only
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
@admin_only
def createSuratPerintahAdmin(request):
	cek_data = Surat_perintah.objects.exists()

	try:
		data_terakhir = Surat_perintah.objects.latest('created_at')
	except ObjectDoesNotExist:
		data_terakhir = None


	form = SuratPerintahForm()


	a = ''

	if request.method == 'POST':
		

		# membuat manipasi value post
		post = request.POST.copy() 			# make it mutable  # typedata post = queryset
		post_d = post.dict()
		tanggalnya = post_d.get('tanggal')
		
		
		# mengubah angka ke romawi
		num_map = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'),
		           (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]

		def num2roman(num):

		    roman = ''

		    while num > 0:
		        for i, r in num_map:
		            while num >= i:
		                roman += r
		                num -= i

		    return roman


		tahun = int(tanggalnya[:4])
		bulan = int(tanggalnya[5:7])
		bulan = num2roman(bulan)

		nomor_str = '001'
		if cek_data:
			gabung = data_terakhir.nomor
			nomor = int(gabung[:3]) + 1
			nomor_str = '%03d' % nomor

		

		no_spt = nomor_str + "/SPT/DISKOMINFO-PB/" + bulan + "/" + str(tahun)

		post['nomor'] = no_spt

		request.POST = post


		form = SuratPerintahForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('myapp_surat_perintah_admin')

		# return redirect('myapp_create_surat_perintah_admin')   # contoh
	
	context = {
		'form': form
	}
	return render(request, 'myapp/myadmin/create_surat_perintah_form.html', context)

@login_required(login_url='login')
@admin_only
def showSuratePerintah(request, pk):
	instansi = Instansi.objects.first()
	suratperintah = Surat_perintah.objects.get(id=pk)
	suratperintah_pegawai = suratperintah.penanggung_jawab
	pelaksana = suratperintah.pengikut.all()
	koordinator = suratperintah.koordinator

	try:
		sppd = Sppd.objects.get(surat_perintah=suratperintah)
		# pelaksana = sppd.pengikut.all()
		# sppd.suratperintah
	except ObjectDoesNotExist:
		sppd = None
		# pelaksana = None
	
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
		'koordinator': koordinator,
		'pelaksana': pelaksana,
		'suratperintah_pegawai': suratperintah_pegawai,
	}
	# return HttpResponse(sppd)
	return render(request, 'myapp/show_surat_perintah.html', context)

@login_required(login_url='login')
@admin_only
def showSppd(request, pk):
	sppd = Sppd.objects.get(id=pk)
	pelaksana = sppd.surat_perintah.pengikut.all()
	# pelakana2 = pelaksana.order_by("-created_at")[1:]
	instansi = Instansi.objects.first()

	waktu = sppd.surat_perintah.tanggal

	lama_perjalanan = sppd.tanggal_kembali - sppd.tanggal_kembali
	# print("===========================================")
	# print(type(sppd.tanggal_kembali))
	# print(type(lama_perjalanan))
	# suratperintah = Surat_perintah.objects.get(id=pk)
	# suratperintah_pegawai = suratperintah.penanggung_jawab
	# sppd = Sppd.objects.get(surat_perintah=suratperintah)

	context = {
		'sppd': sppd,
		'instansi': instansi,
		'lama_perjalanan' : lama_perjalanan,
		'pelaksana': pelaksana,
		'waktu': waktu,
		# 'pelaksana2': pelaksana2,
		# 'suratperintah': suratperintah,
		# 'suratperintah_pegawai': suratperintah_pegawai,
	}
	return render(request, 'myapp/show_sppd.html', context)

@login_required(login_url='login')
@admin_only
def showPengeluaran(request, pk):
	instansi = Instansi.objects.first()
	pengeluaran = Pengeluaran.objects.get(id=pk)
	rincian = pengeluaran.rincian.all()
	total_rincian = pengeluaran.rincian.aggregate(Sum('jumlahnya'))

	# total_rincian = pengeluaran.aggregate(sum('harga'))

	try:
		bendahara = Pegawai.objects.filter(jabatan__iexact="Bendahara").first()
	except ObjectDoesNotExist:
		bendahara = None

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
		'bendahara': bendahara,
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
@admin_only
def showPengeluaranAdmin(request, pk):
	instansi = Instansi.objects.first()
	pengeluaran = Pengeluaran.objects.get(id=pk)
	rincian = pengeluaran.rincian.all()
	total_rincian = pengeluaran.rincian.aggregate(Sum('jumlahnya'))
	
	try:
		bendahara = Pegawai.objects.filter(jabatan__iexact="Bendahara").first()
	except ObjectDoesNotExist:
		bendahara = None



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
		'bendahara': bendahara,
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
@admin_only
def showRincian(request, pk):
	pengeluaran = Pengeluaran.objects.get(id=pk)
	rincian = pengeluaran.rincian.all()
	total_rincian = pengeluaran.rincian.aggregate(Sum('jumlahnya'))

	try:
		bendahara = Pegawai.objects.filter(jabatan__iexact="Bendahara").first()
	except ObjectDoesNotExist:
		bendahara = None

	# try:
	# 	sppd2 = pengeluaran.sppd
	# except ObjectDoesNotExist:
	# 	sppd2 = None

	context = {
		'pengeluaran': pengeluaran,
		'bendahara': bendahara,
		'rincian': rincian,
		'total_rincian': total_rincian['jumlahnya__sum'],
	}
	return render(request, 'myapp/show_rincian.html', context)

@login_required(login_url='login')
@admin_only
def showRincianAdmin(request, pk):
	pengeluaran = Pengeluaran.objects.get(id=pk)
	rincian = pengeluaran.rincian.all()
	total_rincian = pengeluaran.rincian.aggregate(Sum('jumlahnya'))

	try:
		bendahara = Pegawai.objects.filter(jabatan__iexact="Bendahara").first()
	except ObjectDoesNotExist:
		bendahara = None

	# try:
	# 	sppd2 = pengeluaran.sppd
	# except ObjectDoesNotExist:
	# 	sppd2 = None

	context = {
		'pengeluaran': pengeluaran,
		'bendahara': bendahara,
		'rincian': rincian,
		'total_rincian': total_rincian['jumlahnya__sum'],
	}
	return render(request, 'myapp/myadmin/show_rincian.html', context)

@login_required(login_url='login')
@admin_only
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
@admin_only
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
@admin_only
def deleteSuratePerintah(request, pk):
	order = Surat_perintah.objects.get(id=pk)
	order.delete()
	return redirect('myapp_surat_perintah_admin')

@login_required(login_url='login')
@admin_only
def deleteSuratePerintah_(request, pk):
	order = Surat_perintah.objects.get(id=pk)
	order.delete()
	return redirect('myapp_sppd_admin')

@login_required(login_url='login')
@admin_only
def deleteRincianAdmin(request, pk):
	order = Rincian.objects.get(id=pk)
	order.delete()
	return redirect('myapp_rincian_admin')

@login_required(login_url='login')
@admin_only
def deletePegawaiAdmin(request, pk):
	order = Pegawai.objects.get(id=pk)
	order.delete()
	return redirect('myapp_pegawai_admin')

@login_required(login_url='login')
@admin_only
def deletePengeluaranAdmin(request, pk):
	order = Pengeluaran.objects.get(id=pk)
	order.delete()
	return redirect('myapp_pengeluaran_admin')

@login_required(login_url='login')
@admin_only
def deleteSppdAdmin(request, pk):
	order = Sppd.objects.get(id=pk)
	order.delete()
	return redirect('myapp_sppd_admin')

@login_required(login_url='login')
@admin_only
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
@admin_only
def deleteSuratPerintah(request, pk):
	suratperintah = Surat_perintah.objects.get(id=pk)
	if request.method == "POST":
		suratperintah.delete()
		return redirect('myapp_surat_perintah')

	suratperintah.delete()
	return redirect('myapp_surat_perintah')

@login_required(login_url='login')
@admin_only
def rincianAdmin(request):
	rincian = Rincian.objects.all()

	context = {
		'rincian': rincian,
	}
	return render(request, 'myapp/myadmin/rincian_admin.html', context)

@login_required(login_url='login')
@admin_only
def sppd(request):
	sppd = Sppd.objects.all()

	context = {
		'sppd': sppd,
	}
	return render(request, 'myapp/sppd.html', context)

@login_required(login_url='login')
@admin_only
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
@admin_only
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
@admin_only
def pengeluaran(request):
	pengeluaran = Pengeluaran.objects.all()

	context = {
		'pengeluaran': pengeluaran
	}
	return render(request, 'myapp/pengeluaran.html', context)



@login_required(login_url='login')
@admin_only
def pengeluaranAdmin(request):
	pengeluaran = Pengeluaran.objects.all()

	context = {
		'pengeluaran': pengeluaran
	}
	return render(request, 'myapp/myadmin/pengeluaran.html', context)
	# return render(request, 'myapp/myadmin/pengeluaran.html', context)


@login_required(login_url='login')
@admin_only
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
@admin_only
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
@admin_only
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
	suratperintah = sppd.surat_perintah 
	form = SppdForm(instance=sppd)

	if request.method == 'POST':

		# membuat manipasi value post
		post = request.POST.copy() 			# make it mutable  # typedata post = queryset
		no_spt = suratperintah.nomor

		no_sppd = no_spt.replace('SPT', 'SPPD')
		post['nomor'] = no_sppd

		request.POST = post
		
		form = SppdForm(request.POST, instance=sppd)
		if form.is_valid():
			form.save()
			return redirect('myapp_sppd_admin')

	context = {'form':form, 'suratperintah': suratperintah}
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

	context = {'form':form, 'instansi': instansi}
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
	sppd = Sppd.objects.filter(nomor = None)
	suratperintah = Surat_perintah.objects.all().order_by('-created_at')
	jumlah_none = sppd.count()

	context = {
		'suratperintah': suratperintah,
		'jumlah_none': jumlah_none
	}
	return render(request, 'myapp/myadmin/surat_perintah.html', context)

@login_required(login_url='login')
@admin_only
def showSuratePerintahAdmin(request, pk):
	instansi = Instansi.objects.first()
	suratperintah = Surat_perintah.objects.get(id=pk)
	suratperintah_pegawai = suratperintah.penanggung_jawab
	koordinator = suratperintah.koordinator

	pelaksana = suratperintah.pengikut.all()

	try:
		sppd = Sppd.objects.get(surat_perintah=suratperintah)
		# pelaksana = sppd.pengikut.all()
		# sppd.suratperintah
	except ObjectDoesNotExist:
		sppd = None
		# pelaksana = None
	
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
		'koordinator': koordinator,
	}
	# return HttpResponse(sppd)
	return render(request, 'myapp/myadmin/show_surat_perintah.html', context)

@login_required(login_url='login')
@admin_only
def sppdAdmin(request):
	sppd = Sppd.objects.exclude(nomor = None).order_by('-created_at')
	jumlah_none = Sppd.objects.filter(nomor = None).count()

	context = {
		'sppd': sppd,
		'jumlah_none': jumlah_none
	}
	return render(request, 'myapp/myadmin/sppd.html', context)


@login_required(login_url='login')
@admin_only
def showSppdAdmin(request, pk):
	instansi = Instansi.objects.first()	
	sppd = Sppd.objects.get(id=pk)

	try:
		pelaksana = sppd.surat_perintah.pengikut.all()
		waktu = sppd.surat_perintah.tanggal
		lama_perjalanan = sppd.tanggal_kembali - sppd.tanggal_kembali
	except TypeError:
		pelaksana = None
		waktu = None
		lama_perjalanan = None
	
	context = {
		'instansi': instansi,
		'sppd': sppd,
		'lama_perjalanan' : lama_perjalanan,
		'pelaksana': pelaksana,
		'waktu': waktu,
	}
	return render(request, 'myapp/myadmin/show_sppd.html', context)


# ========================================================================umum======================

@login_required(login_url='login')
def surat_perintah_umum(request):
	suratperintah = Surat_perintah.objects.all().order_by('-created_at')
		
	context = {
		'suratperintah': suratperintah
	}
	return render(request, 'myapp/umum/surat_perintah.html', context)

@login_required(login_url='login')
def createSuratPerintah_umum(request):
	form = SuratPerintahForm()

	if request.method == 'POST':
		form = SuratPerintahForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('myapp_surat_perintah_umum')
	context = {
		'form': form
	}
	return render(request, 'myapp/umum/create_surat_perintah_form.html', context)

@login_required(login_url='login')
def showSuratePerintah_umum(request, pk):
	instansi = Instansi.objects.first()
	suratperintah = Surat_perintah.objects.get(id=pk)
	suratperintah_pegawai = suratperintah.penanggung_jawab
	koordinator = suratperintah.koordinator

	pelaksana = suratperintah.pengikut.all()

	try:
		sppd = Sppd.objects.get(surat_perintah=suratperintah)
	except ObjectDoesNotExist:
		sppd = None

	context = {
		'suratperintah': suratperintah,
		'sppd': sppd,
		'instansi': instansi,
		'pelaksana': pelaksana,
		'suratperintah_pegawai': suratperintah_pegawai,
		'koordinator': koordinator,
	}
	# return HttpResponse(sppd)
	return render(request, 'myapp/umum/show_surat_perintah.html', context)

@login_required(login_url='login')
def upadateSuratePerintah_umum(request, pk):
	suratperintah = Surat_perintah.objects.get(id=pk)
	form = SuratPerintahForm(instance=suratperintah)

	if request.method == 'POST':
		form = SuratPerintahForm(request.POST, instance=suratperintah)
		if form.is_valid():
			form.save()
			return redirect('myapp_surat_perintah_umum')

	context = {'form':form}
	return render(request, 'myapp/umum/edit_surat_perintah_form.html', context)


@login_required(login_url='login')
def deleteSuratPerintah_umum(request, pk):
	suratperintah = Surat_perintah.objects.get(id=pk)
	if request.method == "POST":
		suratperintah.delete()
		return redirect('myapp_surat_perintah_umum')

	suratperintah.delete()
	return redirect('myapp_surat_perintah_umum')