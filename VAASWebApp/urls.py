from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .documenthandler import DocumentExportView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

#URLConf
urlpatterns=[
    #Signin and Signup Page
    path('signup/',views.signup,name='signup'),
    path('',views.signin,name='signin'),
    #Home / Default Page
    path('home/',views.home, name='home'),
    path('logout/', views.logout_view, name='logout'),
    #Mapview Page
    path('mapview/',views.mapview,name='mapview'),
    #Document Libraries Page
    path('search/',views.reportlib,name='reportlib'),
    path('create/',views.createcase_view,name='create'),
    #Analytics Page
    path('analytical',views.analytical,name='analytical'),
    #Testing
    path('sampledesign/',views.sampledesign,name='sampledesign'),
    path('sample/',views.testing,name='testing'),
    #Other Experiment 
    path('exportimport',views.exportimport,name='exportimport'),
    path('upload/',views.upload_document,name='upload_document'),
    path('export/',DocumentExportView.as_view(),name='export_document'),
    path('chart/',views.accident_types,name='accident_types'),
    path('popup/',views.testpopup2,name="popup"),
    path('maptest/',views.map_view,name="maptest"),
    #Map Data 
    path('map-data',views.map_data_view,name='map_data'),
    #Document Template
    path('document_preview/',views.document_preview,name='document_preview'),
    path('analyticrep_preview/',views.analytic_report_preview,name='analyticrep_preview'),
    #Analytics Report for Daily,Weekly,Monthly and Yearly
    path('analytic-data/',views.AnalyticDoc,name='analytic_data'),
    path('get_analyticform/',views.get_analyticForm,name='analyticform'),
    path('daily-data/',views.daily_data,name='export_daily'),
    path('weekly-data/',views.weekly_data,name='export_weekly'),
    path('monthly-data/',views.monthly_data,name='export_monthly'),
    path('yearly-data/',views.yearly_data,name='export_yearly')
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
urlpatterns+=staticfiles_urlpatterns()