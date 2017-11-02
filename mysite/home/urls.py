from django.conf.urls import url
from django.views.generic import TemplateView
from . import views

app_name = 'home'

urlpatterns = [
    # .com/home/
    url(r'^$', TemplateView.as_view(template_name='home/index.html'), name='homepage'),
]
