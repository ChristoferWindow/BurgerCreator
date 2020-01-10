from django.shortcuts import render,redirect
from .models import Burger, Ingredient

def index(request):
    burgers = Burger.objects.all()
    ingredients = Ingredient.objects.all()

    if request.method == "POST":
        if "burgerAdd" in request.POST:
            title = request.POST["title"]
            ingredientsList = request.POST["ingredientsList"]
            createdBy = request.user.id
            newBurger = Burger(title=title, ingredients=ingredientsList, createdBy = createdBy)
            newBurger.save()

            return redirect("/") #reloading the page
        if "burgerDelete" in request.POST:
            checkedlist = request.POST["checkedbox"]

            for burger_id in checkedlist:
                burger = Burger.objects.get(id=int(burger_id))
                burger.delete()
    return render(request, "index.html", {"burgers": burgers, "ingredients":ingredients})