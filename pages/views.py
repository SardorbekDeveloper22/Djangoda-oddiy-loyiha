from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
class HomePageView(TemplateView):
	template_name='home.html'
class PageView(TemplateView):
	template_name='uzb.html'
class Page1View(TemplateView):
	template_name='kg.html'
class Page2View(TemplateView):
	template_name='ru.html'
class Page3View(TemplateView):
	template_name='arabic.html'