from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from super_types import views

urlpatterns = [
    path('', views.SuperTypeList.as_view()),
    path('<int:pk>/', views.SuperTypeDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)