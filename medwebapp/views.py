from django.shortcuts import render
from django.http import HttpResponse
from django.template.context import RequestContext
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from .models import klopvalues,profiles,Userprofile
from .serializers import klopserializer
from .forms import Userprofileform,Userform
from django.contrib.auth import authenticate,login


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


def register(request):
    context=RequestContext(request)
    registered=False
    if request.method == 'POST':
        user_form = Userform(data=request.POST)
        profile_form=Userprofileform(data=request.POST)


        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile=profile_form.save(commit=False)
            profile.user=user
            profile.save()

            registered = True
        else:
            print user_form.errors,profile_form.errors
    else:
        user_form = Userform()
        profile_form=Userprofileform()
    return render(request,'medwebapp/register.html',{'registered':registered,'user_form':user_form,
                                                'profile_form':profile_form},context)

def user_login(request):
    context = RequestContext(request)
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            try:

                profile = Userprofile.objects.get(user=user)
                klop= klopvalues.objects.get(klopid=profile.klopid)

            except klopvalues.DoesNotExist:
                return HttpResponse(status=404)

            ecg = klop.ECG_pattern
            ecglist = map(int,ecg.split(" "))
            return render(request,'medwebapp/dispvalues.html',{'klop':klop, 'ecg':ecglist})

        else:
            return HttpResponse('invalid login details')
    else:
        return render(request,'medwebapp/login.html',context)

