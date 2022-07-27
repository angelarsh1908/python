"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
# from atexit import register
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
 
    path('',views.home, name='home'),
    path('register/',views.register,name="register"),
    path('login/',views.login,name="login"),
    path('logout/',views.logout,name="logout"),
    path('profile/',views.profile,name="profile"),
    path("doc-profile/",views.doc_profile,name="doc-profile"),
    path("doc-pass-change/",views.doc_pass_change,name="doc-pass-change"),
    path("all-doctors/",views.all_doctors,name="all-doctors"),
    path("view-doc/<int:pk>",views.view_doc,name="view-doc"),
    path("change-password/",views.changepassword,name="change-password"),
    
    path("all-patients/",views.all_patients,name="all-patients"),
    path("p-all-doctors/",views.p_all_doctors,name="p-all-doctors"),
    path("p-doc-spec-profile/<int:pk>/",views.p_doc_spec_profile,name="p-doc-spec-profile"),
    path("book-appointment/<int:pk>/",views.p_book_appointment,name="book-appointment"),
    path("book-a/",views.p_book_a,name="book-a"),
    path("pat-profile/",views.pat_profile,name="pat-profile"),
    path("pt-profile/",views.pt_profile,name="pt-profile"),
    path('approve-a/<int:pk>/',views.approve_a, name='approve-a'),
    path('reject-a/<int:pk>/',views.reject_a, name='reject-a'),
    
]
