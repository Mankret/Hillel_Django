from django.urls import path

from docsapp import views

app_name = 'docsapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('book/', views.BookView.as_view(), name='book'),
    path('author/', views.AuthorView.as_view(), name='author'),
    path('publisher/', views.PublisherView.as_view(), name='publisher'),
    path('store/', views.StoreView.as_view(), name='store'),
    ]

urlpatterns += [
    path('book/<int:pk>/', views.BookDetailView.as_view(), name='book_detail'),
    path('author/<int:pk>/', views.AuthorDetailView.as_view(), name='author_detail'),
    path('publisher/<int:pk>/', views.PublisherDetailView.as_view(), name='publisher_detail'),
    path('store/<int:pk>/', views.StoreDetailView.as_view(), name='store_detail'),
    ]
