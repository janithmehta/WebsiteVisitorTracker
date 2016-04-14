from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'WebsiteTracker.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^tracker/', include('tracker.urls')),
    # url(r'^$', 'WebsiteTracker.views.home', name='home'),
    # url(r'^login/$', 'WebsiteTracker.views.login_view', name='login'),
    # url(r'^logout/$', 'WebsiteTracker.views.logout_view', name='logout'),
    # url(r'^register/$', 'WebsiteTracker.views.register_view', name='regiser'),
    # url(r'^auth/$', 'WebsiteTracker.views.auth_view', name='authorise'),
    # url(r'^loggedin/$', 'WebsiteTracker.views.loggedin_view', name='loggedin'),
    # url(r'^invalid/$', 'WebsiteTracker.views.invalid_view', name='invalid'),
    # url(r'^register_success/$', 'WebsiteTracker.views.register_success_view', name='register_success'),


]
