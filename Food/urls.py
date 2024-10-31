from django.urls import path
from .views import (
    PizzaListView, PizzaDetailView, PizzaCreateView, PizzaUpdateView, PizzaDeleteView,
    BurgerListView, BurgerDetailView, BurgerCreateView, BurgerUpdateView, BurgerDeleteView,
    MacaronaListView, MacaronaDetailView, Home
)

urlpatterns = [
    path('',Home.as_view(),name='home'),
    path('pizzas/', PizzaListView.as_view(), name='pizza_list'),
    path('pizzas/<int:pk>/', PizzaDetailView.as_view(), name='pizza_detail'),
    path('pizzas/add/', PizzaCreateView.as_view(), name='pizza_create'),
    path('pizzas/<int:pk>/edit/', PizzaUpdateView.as_view(), name='pizza_update'),
    path('pizzas/<int:pk>/delete/', PizzaDeleteView.as_view(), name='pizza_delete'),
    path('burgers/', BurgerListView.as_view(), name='burger_list'),
    path('burgers/<int:pk>/', BurgerDetailView.as_view(), name='burger_detail'),
    path('burgers/add/', BurgerCreateView.as_view(), name='burger_create'),
    path('burgers/<int:pk>/edit/', BurgerUpdateView.as_view(), name='burger_update'),
    path('burgers/<int:pk>/delete/', BurgerDeleteView.as_view(), name='burger_delete'),
    path('macaronas/', MacaronaListView.as_view(), name='pizza_list'),
    path('macaronas/<int:pk>/', MacaronaDetailView.as_view(), name='pizza_detail'),
]