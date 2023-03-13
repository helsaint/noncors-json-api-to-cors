from django.urls import path
from .views import fpl_page, fpl_api, FPLAPI


urlpatterns = [
    path('', fpl_page, name="fpl_page"),
    path('fpl_api', fpl_api, name='fpl_api'),

]