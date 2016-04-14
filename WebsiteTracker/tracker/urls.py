from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'WebsiteTracker.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'tracker.views.home', name='home'),
    url(r'^login/$', 'tracker.views.login_view', name='login'),
    url(r'^logout/$', 'tracker.views.logout_view', name='logout'),
    url(r'^register/$', 'tracker.views.register_view', name='regiser'),
    url(r'^auth/$', 'tracker.views.auth_view', name='authorise'),
    url(r'^loggedin/$', 'tracker.views.loggedin_view', name='loggedin'),
    url(r'^invalid/$', 'tracker.views.invalid_view', name='invalid'),
    url(r'^register_success/$', 'tracker.views.register_success_view', name='register_success'),
    url(r'^add_website/$', 'tracker.views.add_webiste_view', name='add_website'),
    url(r'^add_website_successfully/(?P<id>[0-9]+$)', 'tracker.views.add_website_successful_view', name='add_website'),
    url(r'^sites/$', 'tracker.views.sites_view', name='sites_view'),
    url(r'^visits/$', 'tracker.views.visits_view', name='visits_view'),


    url(r'^sites/(?P<sid>[0-9]+)/visit', 'tracker.views.add_visit', name='add_visit'),


]
