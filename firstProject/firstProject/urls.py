

from django.contrib import admin
from django.urls import path
from . import views
from firstProject.views import index,predict
#from .views import index
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('about.html/', views.about, name='about'),
    path('feedback.html/', views.feedback, name='feedback'),
    path('analyze', views.analyze, name='analyze'),
    url(r'^posts/(?P<slug>.+?)/$',predict,name="predict"),

]

