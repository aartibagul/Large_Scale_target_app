from django.conf.urls import url
from . import view_counters

urlpatterns = [
            url(r'^$', view_counters.display_counters, name='counters'),
            
]
