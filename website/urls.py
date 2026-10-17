from django.urls import path,include
from . import views
#domain.com/website/...
urlpatterns=[
    path('',views.home_view, name='home'),
    path('about',views.about_view, name='about'),
    path('meetings/', include('meetings.urls')),

]