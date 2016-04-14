from django.db import models
from django.contrib.auth.models import User

class Site(models.Model):

    base_url = models.URLField(max_length=200)
    # visits = models.ForeignKey(Visit, related_name='visits')
    user_id = models.ForeignKey(User, related_name='user')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return '<Site {:d} {}>'.format(self.id, self.base_url)

    def __str__(self):
        return self.base_url


class Visit(models.Model):

    browser = models.CharField(max_length=500)
    date = models.DateTimeField()
    event = models.CharField(max_length=200)
    url = models.URLField(max_length=200)
    ip_address = models.GenericIPAddressField(max_length=200)
    location = models.CharField(max_length=200)
    latitude = models.FloatField()
    longitude = models.FloatField()
    site_id = models.ForeignKey(Site, on_delete = models.CASCADE, related_name='site')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        r = '<Visit for site ID {:d}: {} - {:%Y-%m-%d %H:%M:%S}>'
        return r.format(self.site_id, self.url, self.date)