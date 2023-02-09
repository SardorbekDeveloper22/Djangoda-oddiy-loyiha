from django.urls import path
from .views import HomePageView,PageView,Page1View,Page2View,Page3View



urlpatterns=[
	path('',HomePageView.as_view(),name='home'),
	path('uzb/',PageView.as_view(),name='uzb'),
	path('kg/',Page1View.as_view(),name='kg'),
	path('ru/',Page2View.as_view(),name='ru'),
	path('arabic/',Page3View.as_view(),name='arabic'),
]