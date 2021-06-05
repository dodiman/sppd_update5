from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def index(request):
	context = {}
	return render(request, 'myapp/index.html', context)

@login_required(login_url='login')
def surat_perintah(request):
	context = {}
	return render(request, 'myapp/surat_perintah.html', context)

@login_required(login_url='login')
def sppd(request):
	context = {}
	return render(request, 'myapp/sppd.html', context)

@login_required(login_url='login')
def laporan(request):
	context = {}
	return render(request, 'myapp/laporan.html', context)

@login_required(login_url='login')
def pegawai(request):
	context = {}
	return render(request, 'myapp/pegawai.html', context)
