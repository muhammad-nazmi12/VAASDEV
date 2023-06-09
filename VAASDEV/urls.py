"""VAASDEV URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
#from VAASWebApp.views import home,logout_view
import debug_toolbar
#from editor.views import EditorChartView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('__debug__/', include('debug_toolbar.urls')),
    path('', include('VAASWebApp.urls')),
    #path('documents/',include('documents.urls')),
    #path('login/',CustomLoginView.as_view(),name='login'),
    #path('logout/',logout_view,name='logout'),
    #path('home/',home,name='home'),
    #path('', EditorChartView.as.view(),name='index'),
]
