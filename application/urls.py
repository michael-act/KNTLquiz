from django.views.generic.base import RedirectView
from django.urls import path, re_path
from . import views

urlpatterns = [
	path('', RedirectView.as_view(url='/1', permanent=False), name='index'), 
	path('<int:word_id>', views.quiz, name='quiz'), 
	re_path(r'^.*$', RedirectView.as_view(url='/1', permanent=False), name='other')
]