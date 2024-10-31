# myproject/Food/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy
from .models import Pizza, Burger, Macarona
from .forms import PizzaForm, BurgerForm

class Home(TemplateView):
    template_name = 'Food/index.html'

class PizzaListView(ListView):
    model = Pizza
    template_name = 'Food/pizza_list.html'

class PizzaDetailView(DetailView):
    model = Pizza
    template_name = 'Food/pizza_detail.html'

class PizzaCreateView(CreateView):
    model = Pizza
    form_class = PizzaForm
    template_name = 'Food/pizza_form.html'
    success_url = reverse_lazy('pizza_list')

class PizzaUpdateView(UpdateView):
    model = Pizza
    form_class = PizzaForm
    template_name = 'Food/pizza_form.html'
    success_url = reverse_lazy('pizza_list')

class PizzaDeleteView(DeleteView):
    model = Pizza
    template_name = 'Food/pizza_delete.html'
    success_url = reverse_lazy('pizza_list')

class BurgerListView(ListView):
    model = Burger
    template_name = 'Food/burger_list.html'

class BurgerDetailView(DetailView):
    model = Burger
    template_name = 'Food/burger_detail.html'

class BurgerCreateView(CreateView):
    model = Burger
    form_class = BurgerForm
    template_name = 'Food/burger_form.html'
    success_url = reverse_lazy('burger_list')

class BurgerUpdateView(UpdateView):
    model = Burger
    form_class = BurgerForm
    template_name = 'Food/burger_form.html'
    success_url = reverse_lazy('burger_list')

class BurgerDeleteView(DeleteView):
    model = Burger
    template_name = 'Food/burger_confirm_delete.html'
    success_url = reverse_lazy('burger_list')


class MacaronaListView(ListView):
    model= Macarona
    template_name='Food/pizza_list.html'

class MacaronaDetailView(DetailView):
        model= Macarona
        template_name='Food/pizza_detail.html'