from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from tracker.forms import RegistrationForm, SiteForm, VisitForm
from .models import Site,Visit
from datetime import datetime


def home(request):
    return render_to_response('index.html')

def login_view(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('login.html', c)

def auth_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)

    if user is not None:
        login(request, user)
        return HttpResponseRedirect('/loggedin')
    else:
        return HttpResponseRedirect('/invalid')

@login_required
def loggedin_view(request):

    user_id = request.user.id
    query_results = Site.objects.all().filter(user_id_id=user_id)
    return render_to_response('loggedin.html', {'query_results':query_results,'username':request.user.username})

def invalid_login(request):
    return render_to_response('invalid_login.html')

def logout_view(request):
    logout(request)
    return render_to_response('logout.html')

def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            print("Successful")
            return HttpResponseRedirect('/register_success/')

    args ={}
    args.update(csrf(request))

    args['form'] = RegistrationForm()
    return render_to_response('register.html', args)

def register_success_view(request):
    return render_to_response('register_success.html')

@login_required
def add_webiste_view(request):
    if request.method == 'POST':
        form = SiteForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            url = data['base_url']
            form.save()
            query_result = Site.objects.values('id').filter(base_url=url)
            for i in query_result:
                id= i['id']
            redirect_url = "/add_website_successfully/"+str(id)
            return HttpResponseRedirect(redirect_url)

    args ={}
    args.update(csrf(request))

    args['form'] = SiteForm()
    return render_to_response('add_website.html', args)

@login_required
def add_website_successful_view(request, id):
    print("ENTER")
    site_id =id
    return render_to_response("add_website_successful.html",{'site_id': site_id})

@login_required
def sites_view(request):
    user_id = request.user.id
    query_results = Site.objects.all().filter(user_id_id=user_id)
    return render_to_response('sites.html', {'query_results':query_results,'username':request.user.username})

@login_required
def visits_view(request):

    user_id = request.user.id
    visits = Visit.objects.filter(site_id__user_id=user_id)
    sites = Site.objects.filter(user_id_id=user_id)
    return render_to_response('visits.html', {'visits':visits, 'sites': sites})


def add_visit(request, sid):

    site = int(sid)

    browser = request.META['HTTP_USER_AGENT']
    date = datetime.now()
    event = "PageLoad"
    ip_address = request.META['REMOTE_ADDR']

    site_query = Site.objects.values('base_url').filter(id=site)
    base_url = site_query[0]['base_url']
    latitude = 1.414
    longitude = 1.732
    location = "Mumbai"

    site_object = Site(id=sid, base_url=base_url)

    visit = Visit(browser=browser, date=date, event=event, url=base_url, latitude=latitude, longitude=longitude, location=location, ip_address=ip_address, site_id=site_object)
    visit.save()

    return  HttpResponseRedirect('/loggedin')