from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from supers import views



urlpatterns = [
    path('', views.SupersList.as_view()),
    path('<int:pk>/', views.SupersDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)