from django.urls import path
from myapp import views

urlpatterns = [
    path('myapi/', views.ContactList.as_view()),
    path('contactDetail/<int:pk>/', views.ContactDetail.as_view()),
]