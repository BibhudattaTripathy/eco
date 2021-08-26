from django.shortcuts import render# use for database
from django.views.generic import TemplateView,CreateView # CreateView use for database
from .models import ecodatabase # use for database
from .forms import ProfileForm #used for database

# Create your views here.

class IndexView(TemplateView):
    template_name = "app/index.html"

# class ContactView(TemplateView):
#     template_name = "app/contact.html"

class DonateView(TemplateView):
    template_name = "app/donate.html"

class AboutView(TemplateView):
    template_name = "app/about.html"

class ProtectView(TemplateView):
    template_name = "app/protect.html"

class PondView(TemplateView):
    template_name = "app/pond.html"

class RiverView(TemplateView):
    template_name = "app/river.html"

class RainforestView(TemplateView):
    template_name = "app/rainforests.html"

class TundraView(TemplateView):
    template_name = "app/tundra.html"

class DesertView(TemplateView):
    template_name = "app/desert.html"

class SavannaView(TemplateView):
    template_name = "app/savanna.html"

class ForestView(TemplateView):
    template_name = "app/forest.html"

class GrasslandView(TemplateView):
    template_name = "app/grassland.html"

class ShallowwaterlandView(TemplateView):
    template_name = "app/shallow.html"

class DeepwaterView(TemplateView):
    template_name = "app/deepwater.html"

class WarmwaterView(TemplateView):
    template_name = "app/warmwater.html"

class ColdwaterView(TemplateView):
    template_name = "app/coldwater.html"



#database connection 
class ContactView(CreateView):
    model = ecodatabase
    template_name = "app/contact.html"
    form_class = ProfileForm
    success_url = "/"
