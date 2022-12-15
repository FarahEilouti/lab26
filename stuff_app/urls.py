from django.urls import path
from .views import StuffListView,StuffDetailView,PostDetailView,PostDetailView


urlpatterns = [
   path('', StuffListView.as_view(), name='stuff_list'),
   path('<int:pk>', StuffDetailView.as_view(),name='stuff_detail'),
   path('post/', PostDetailView.as_view(), name='stuff_list'),
   path('post/<int:pk>', PostDetailView.as_view(),name='coffee_detail')


]