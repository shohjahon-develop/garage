from django.urls import path
from .views import index,contact,cardetailView

urlpatterns=[
  path('index/',index,name='index'),
  path('contact/',contact,name='contact'),
  path("<int:id>/",cardetailView,name='cardetail')
]
