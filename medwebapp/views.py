from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from .models import klopvalues,profiles
from .serializers import klopserializer


# Create your views here.

class JSONResponse(HttpResponse):
    def __init__(self,data,**kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type']='application/json'
        super(JSONResponse,self).__init__(content,**kwargs)


@csrf_exempt
def klop_detail(request,kid):

    ##http http://127.0.0.1:8000/klop/detail/kid/
    if request.method == 'GET':
        try:
            klop= klopvalues.objects.get(klopid=kid)
        except klopvalues.DoesNotExist:
            return HttpResponse(status=404)
        serialized_klop = klopserializer(klop)
        return JSONResponse(serialized_klop.data)

    ##http --json post http://127.0.0.1:8000/klop/detail/kid/ name=value name2=value2
    if request.method == 'POST':
        data = JSONParser().parse(request)
        klop_serialized = klopserializer(data=data)

        if klop_serialized.is_valid():
            klop_serialized.save()
            return HttpResponse(status=200)

    ##http --json put http://127.0.0.1:8000/klop/detail/kid/ name=value name2=value2
    if request.method == 'PUT':
        try:
            klop= klopvalues.objects.get(klopid=kid)
        except klopvalues.DoesNotExist:
            return HttpResponse(status=404)
        data = JSONParser().parse(request)
        klop_serialized = klopserializer(klop,data=data)
        if klop_serialized.is_valid():
            klop_serialized.save()
            return HttpResponse(status=200)

    ##http delete http://127.0.0.1:8000/klop/detail/kid/
    if request.method == 'DELETE':
        try:
            klop= klopvalues.objects.get(klopid=kid)
        except klopvalues.DoesNotExist:
            return HttpResponse(status=404)
        klop.delete()
        return HttpResponse(status=204)

@csrf_exempt
def detail_search(request):
    return render(request,'medwebapp/search.html')

@csrf_exempt
def display_details(request):
    try:
        klop= klopvalues.objects.get(klopid=request.POST['klopid'])
    except klopvalues.DoesNotExist:
        return HttpResponse(status=404)
    ecg = klop.ECG_pattern
    ecglist = map(int,ecg.split(" "))
    return render(request,'medwebapp/dispvalues.html',{'klop':klop,'ecg':ecglist})
    #serialized_klop = klopserializer(klop)
    #return JSONResponse(serialized_klop.data)

@csrf_exempt
def login(request):
    return render(request,'medwebapp/login.html')

@csrf_exempt
def validate(request):
    kid = request.POST['klopid']
    password = request.POST['password']
    try:
        prof = profiles.objects.get(klopid=kid)
    except profiles.DoesNotExist:
        return render(request,'medwebapp/signup.html')
    if password == prof.password:
        try:
            klop= klopvalues.objects.get(klopid=request.POST['klopid'])
        except klopvalues.DoesNotExist:
            return HttpResponse(status=404)
        ecg = klop.ECG_pattern
        ecglist = map(int,ecg.split(" "))
        return render(request,'medwebapp/dispvalues.html',{'klop':klop, 'ecg':ecglist})
    else:
        return render(request,'medwebapp/signup.html')

@csrf_exempt
def signup(request):
    kid = request.POST['klopid']
    password = request.POST['password']
    name = request.POST['name']
    age = int(request.POST['age'])
    sg = request.POST['sg']
    bp = request.POST['bp']
    p = profiles(klopid = kid, password=password,name=name,age=age,sg=sg,bp=bp)
    p.save()
    try:
        klop= klopvalues.objects.get(klopid=kid)
    except klopvalues.DoesNotExist:
        return HttpResponse(status=404)
    ecg = klop.ECG_pattern
    ecglist = map(int,ecg.split(" "))
    return render(request,'medwebapp/dispvalues.html',{'klop':klop, 'ecg':ecglist})

@csrf_exempt
def signup_show(request):
    return render(request,'medwebapp/signup.html')
