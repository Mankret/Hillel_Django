from django.urls import path

from mathapp import views

app_name = 'mathapp'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('person/<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('person/create', views.person_create, name="person_create"),
    path('person/update/<int:pk>', views.person_update, name="person_update"),

]
