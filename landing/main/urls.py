from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='homepage'),
    path('about', views.about, name='about-us'),
    path('shop', views.shop, name='shop-example'),
    path('create-test-cases', views.create_tcs, name='create-test-cases'),
    path('create-new-el-indb', views.test, name='create-new'),
]
