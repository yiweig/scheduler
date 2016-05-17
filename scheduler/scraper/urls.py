from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /scraper/
    url(r'^$', views.index, name='index'),
    # ex: /scraper/5/
    url(r'^(?P<scraper_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /scraper/5/results/
    url(r'^(?P<scraper_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /scraper/5/vote/
    url(r'^(?P<scraper_id>[0-9]+)/vote/$', views.vote, name='vote'),

]
