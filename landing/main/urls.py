from django.urls import path
from . import views

"""There you can change url path and its name."""
urlpatterns = [
    path('', views.index, name='homepage'),
    path('about', views.about, name='about-us'),
    path('skills', views.shop, name='shop-example'),
    path('create-test-cases', views.create_tcs, name='create-test-cases'),
    path('create-new-el-indb', views.test, name='create-new'),
]
