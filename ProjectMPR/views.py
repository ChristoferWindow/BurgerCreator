from django.shortcuts import render,redirect
from .models import Burger, Ingredient
import sys

def index(request):
    burgers = Burger.objects.all()
    ingredients = Ingredient.objects.all()

    if request.method == "POST":
        if "burgerAdd" in request.POST:
            burgerName = request.GET['burgerName']

            if 'ingredientsList' in request.GET:
                ingredientsList = request.GET.getlist('ingredientsList')
                createdBy = 1
                newBurger = Burger(title=burgerName, ingredients=ingredientsList, createdBy=createdBy)
                newBurger.save()

            return redirect("/") #reloading the page
        if "burgerDelete" in request.GET:
            checkedlist = request.GET["checkedbox"]

            for burger_id in checkedlist:
                burger = Burger.objects.get(id=int(burger_id))
                burger.delete()
    return render(request, "index.html", {"burgers": burgers, "ingredients":ingredients})

def add(request):
    burgerName = request.GET['burgerName']

    if 'ingredientsList' in request.GET:
        ingredientsList = request.GET.getlist('ingredientsList')
        createdBy = 1
        newBurger = Burger(title = burgerName, ingredients = ingredientsList, createdBy = createdBy)
        newBurger.save()

    return redirect('/')  # reloading the page

def convert(a):
    it = iter(a)
    res_dct = dict(zip("ingredient", it))
    return res_dct