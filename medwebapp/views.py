from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template.context import RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from .models import watchervalues,profiles,Userprofile
from .serializers import watcherserializer
from .forms import Userprofileform,Userform
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User


import cloudinary
import cloudinary.uploader
import cloudinary.api

cloudinary.config(
  cloud_name = "dee0u22kn",
  api_key = "268259648143926",
  api_secret = "3EfStH6RsPn4C1cqGcytRP7IOxQ"
)


# Create your views here.

class JSONResponse(HttpResponse):
    def __init__(self,data,**kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type']='application/json'
        super(JSONResponse,self).__init__(content,**kwargs)


@csrf_exempt
def watcher_restapi(request,watcher_id):

    ##http http://127.0.0.1:8000/watcher/watcher_id/
    if request.method == 'GET':
        try:
            watcher= watchervalues.objects.get(watcherid=watcher_id)
        except watchervalues.DoesNotExist:
            return HttpResponse(status=404)
        serialized_watcher = watcherserializer(watcher)
        return JSONResponse(serialized_watcher.data)

    ##http --json post http://127.0.0.1:8000/watcher/watcher_id/ name=value name2=value2
    if request.method == 'POST':
        data = JSONParser().parse(request)
        watcher_serialized = watcherserializer(data=data)

        if watcher_serialized.is_valid():
            watcher_serialized.save()
            return HttpResponse(status=200)

    ##http --json put http://127.0.0.1:8000/watcher/watcher_id/ name=value name2=value2
    if request.method == 'PUT':
        try:
            watcher= watchervalues.objects.get(watcherid=watcher_id)
        except watchervalues.DoesNotExist:
            return HttpResponse(status=404)
        data = JSONParser().parse(request)
        watcher_serialized = watcherserializer(watcher,data=data)
        if watcher_serialized.is_valid():
            watcher_serialized.save()
            return HttpResponse(status=200)

    ##http delete http://127.0.0.1:8000/watcher/watcher_id/
    if request.method == 'DELETE':
        try:
            watcher= watchervalues.objects.get(watcherid=watcher_id)
        except watchervalues.DoesNotExist:
            return HttpResponse(status=404)
        watcher.delete()
        return HttpResponse(status=204)


@csrf_exempt
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

            profile_url = cloudinary.uploader.upload(request.FILES['Profile-pic'])

            profile=profile_form.save(commit=False)
            profile.user=user
            profile.image_url=profile_url['url']
            profile.save()

            registered = True
        else:
            print user_form.errors,profile_form.errors
    else:
        user_form = Userform()
        profile_form=Userprofileform()
    return render(request,'medwebapp/register.html',{'registered':registered,'user_form':user_form,
                                                'profile_form':profile_form},context)

@csrf_exempt
def user_login(request):
    context = RequestContext(request)
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            profile = Userprofile.objects.get(user=user)
            return redirect(watcher_dashboard,watcher_id=profile.watcherid)

        else:
            return HttpResponse('invalid login details')

    else:
        return render(request,'medwebapp/login.html',context)

@login_required
def user_logout(request):
    logout(request)
    return redirect(user_login)

@login_required
def profile_update(request,watcher_id):
    context=RequestContext(request)
    updated=False

    watcher_profile = Userprofile.objects.get(watcherid=watcher_id)
    user_instance = User.objects.get(username=watcher_profile.user)
    if request.method == 'POST':
        user_form = Userform(data=request.POST,instance=user_instance)
        profile_form=Userprofileform(data=request.POST,instance=watcher_profile)


        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile=profile_form.save(commit=False)
            profile.user=user

            #if request.FILES['Profile-pic']:
             #   profile_url = cloudinary.uploader.upload(request.FILES['Profile-pic'])
             #   profile.image_url=profile_url['url']

            profile.save()

            updated = True
            return redirect(user_login)
        else:
            print user_form.errors,profile_form.errors
    else:
        user_form = Userform(instance=user_instance)
        profile_form=Userprofileform(instance=watcher_profile)
        return render(request,'medwebapp/updateprofile.html',{'updated':updated,'user_form':user_form,
                                                'profile_form':profile_form, 'watcher_profile': watcher_profile},context)


@login_required
def watcher_dashboard(request, watcher_id):
    try:
        profile = Userprofile.objects.get(watcherid=watcher_id)
        watcher= watchervalues.objects.get(watcherid=watcher_id)
        ecg = watcher.ECG_pattern
        ecglist = map(int,ecg.split(" "))
        return render(request,'medwebapp/dashboard.html',{'watcher':watcher, 'ecg':ecglist, 'profile':profile})

    except watchervalues.DoesNotExist:
        return HttpResponse('your IOT device is not active')


def watcher_dashboard_notactive(request, watcher_id):
    try:
        profile = Userprofile.objects.get(watcherid=watcher_id)
        watcher= watchervalues.objects.get(watcherid=watcher_id)
        ecg = watcher.ECG_pattern
        ecglist = map(int,ecg.split(" "))
        return render(request,'medwebapp/dashboardnotactive.html',{'watcher':watcher, 'ecg':ecglist, 'profile':profile})

    except watchervalues.DoesNotExist:
        return HttpResponse('your IOT device is not active')

@login_required
def watcher_info(request, watcher_id):
    try:
        profile = Userprofile.objects.get(watcherid=watcher_id)
        watcher= watchervalues.objects.get(watcherid=watcher_id)
        ecg = watcher.ECG_pattern
        ecglist = map(int,ecg.split(" "))
        return render(request,'medwebapp/watcherinfo.html',{'watcher':watcher, 'ecg':ecglist, 'profile':profile})

    except watchervalues.DoesNotExist:
        return HttpResponse('your IOT device is not active')


@login_required
def watcher_share(request, watcher_id):
    try:
        profile = Userprofile.objects.get(watcherid=watcher_id)
        watcher= watchervalues.objects.get(watcherid=watcher_id)
        ecg = watcher.ECG_pattern
        ecglist = map(int,ecg.split(" "))
        return render(request,'medwebapp/share.html',{'watcher':watcher, 'ecg':ecglist, 'profile':profile})

    except watchervalues.DoesNotExist:
        return HttpResponse('your IOT device is not active')