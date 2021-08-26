
from django.urls import path
from . import views
#used for database bello 2 lines
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [

    path('',views.IndexView.as_view(), name="index"),
    path('contact/',views.ContactView.as_view(), name="contact"),
    path('donate/',views.DonateView.as_view(), name="donate"),
    path('about/',views.AboutView.as_view(), name="about"),
    path('protect/',views.ProtectView.as_view(), name="protect"),
    path('pond/',views.PondView.as_view(), name="pond"),
    path('river/',views.RiverView.as_view(), name="river"),
    path('rainforests/',views.RainforestView.as_view(), name="rainforests"),
    path('tundra/',views.TundraView.as_view(), name="tundra"),
    path('desert/',views.DesertView.as_view(), name="desert"),
    path('savanna/',views.SavannaView.as_view(), name="savanna"),
    path('forest/',views.ForestView.as_view(), name="forest"),
    path('grassland/',views.GrasslandView.as_view(), name="grassland"),
    path('shallow/',views.ShallowwaterlandView.as_view(), name="shallow"),
    path('deepwater/',views.DeepwaterView.as_view(), name="deepwater"),
    path('warmwater/',views.WarmwaterView.as_view(), name="warmwater"),
    path('coldwater/',views.ColdwaterView.as_view(), name="coldwater")

]

