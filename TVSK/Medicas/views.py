from io import TextIOBase
from typing import Text
from django.core.checks.messages import INFO
from django.db.models.fields.related import ForeignKey, ForeignObject
from django.shortcuts import render ,  redirect
from django.http import JsonResponse,HttpResponse, request
from django.views.generic import View, TemplateView
from django.template.loader import render_to_string
from .models import INFOSP, Advisor_Profile , Specialty
from .filters import FilterAdName, FilterAdSpe, FilterDSSP
from .models import DANH_SACH_SP,MOTA,INFOSP

def Home(request):
    return render(request,'pages/index.html')

def Medicine(request):
    return render(request,'pages/banthuoc.html')


def advisorlist(request):
    total_data=Advisor_Profile.objects.count()
    data=Advisor_Profile.objects.all()[:6]
    test=Advisor_Profile.objects.all()
    spec=Specialty.objects.all()
    opts=request.GET.get('opts','-2')
    specFilter= Advisor_Profile.objects.filter(specialty__icontains=opts)
    nameFilter = FilterAdName(request.GET, queryset=test)
    data=nameFilter.qs[:6]
    context={"data":data, "total_data":total_data, 'nameFilter':test, 'spec':spec, 'specFilter':specFilter}
    return render(request, 'pages/advisor.html',context)

def tuvan(request, phanloai):
    sp = DANH_SACH_SP.objects.filter(PHANLOAI=phanloai)
    cd = DANH_SACH_SP.objects.values('CONGDUNG').distinct()
    return render(request,'pages/TuVan.html',{'sp':sp,'pl':phanloai,'cd':cd})

def congdung(request, congdung):
    sp = DANH_SACH_SP.objects.filter(CONGDUNG=congdung)
    cd = DANH_SACH_SP.objects.values('CONGDUNG').distinct()
    return render(request,'pages/TuVan.html',{'sp':sp,'cd':cd,'pl':congdung})

def search(request):
    if request.method == "POST":
        search = request.POST['search']
        sp = DANH_SACH_SP.objects.filter(TENSP__contains=search)
        cd = DANH_SACH_SP.objects.values('CONGDUNG').distinct()
        return render(request,'pages/TuVan.html',{'sp':sp,'cd':cd,'pl':'Tìm kiếm sản phẩm'}) 
    else:
        cd = DANH_SACH_SP.objects.values('CONGDUNG').distinct()
        return render(request,'pages/TuVan.html',{'cd':cd,'pl':'Không tìm thấy sản phẩm'})


def Detailsp(request, id):
    ds=DANH_SACH_SP.objects.filter(id=id)
    pD = MOTA.objects.filter(MASP_id=id)
    info = INFOSP.objects.filter(MASP_id=id)
    return render(request,'pages/chitiet.html',{'pD':pD,'info':info,'ds':ds})

##############################
def load_more_data(request):
	offset=int(request.GET['offset'])
	limit=int(request.GET['limit'])
	data=Advisor_Profile.objects.all()[offset:limit+offset]
	t=render_to_string('ajax/advisor.html',{'data':data})
	return JsonResponse({'data':t}
)
