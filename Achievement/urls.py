from django.urls import path,re_path,include
from . import views

urlpatterns = [

    re_path("display/",views.display,name="display"),
    re_path('verify/',views.verificationListView,name="verify"),
    re_path('achieve/',views.achievementForm,name="achievement"),


]
