from django.urls import path
from . import views
from .documenthandler import DocumentExportView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

#URLConf
urlpatterns=[
    path('register/',views.signup,name='register'),
    path('login/',views.signin,name='signin'),
    path('home/',views.home, name='home'),
    path('logout/', views.logout_view, name='logout'),
    path('sampledesign/',views.sampledesign,name='sampledesign'),
    path('sample/',views.testing,name='testing'),
    path('analytical',views.analytical,name='analytical'),
    path('search/',views.reportlib,name='reportlib'),
    path('mapview/',views.mapview,name='mapview'),
    path('exportimport',views.exportimport,name='exportimport'),
    path('upload/',views.upload_document,name='upload_document'),
    path('export/',DocumentExportView.as_view(),name='export_document'),
    path('chart/',views.accident_types,name='accident_types'),
    path('popup/',views.testpopup2,name="popup"),
    path('maptest/',views.map_view,name="maptest"),
    path('create/',views.createcase_view,name='create')
]

urlpatterns+=staticfiles_urlpatterns()