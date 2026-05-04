from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from .models import Item, Purchase

def signup_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        if not username or not email or not password:
            return render(request, "signup.html", {
                "error": "Fill out all the fields."
            })

        if User.objects.filter(username=username).exists():
            return render(request, "signup.html", {
                "error": "Username already exists."
            })

        User.objects.create_user(username=username, email=email, password=password)

        return render(request, "signup.html", {
            "success": True  # 👈 important flag
        })

    return render(request, "signup.html")


def shop_view(request):
    items = Item.objects.all()

    if request.method == "POST":
        if request.POST.get("username") and request.POST.get("password"):
            username = request.POST.get("username")
            password = request.POST.get("password")

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                return render(request, "shop.html", {
                    "items": items,
                    "error": "Invalid login."
                })

    return render(request, "shop.html", {"items": items})


def buy_view(request, item_id):
    item = get_object_or_404(Item, id=item_id)

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")

        if not name or not email:
            return render(request, "buy.html", {
                "item": item,
                "error": "Fill out fields."
            })

        try:
            validate_email(email)
        except ValidationError:
            return render(request, "buy.html", {
                "item": item,
                "error": "Enter a valid email."
            })

        Purchase.objects.create(
            name=name,
            email=email,
            item=item
        )

        return render(request, "buy.html", {
            "item": item,
            "success": "Success, being processed." 
        })

    return render(request, "buy.html", {"item": item})

def logout_view(request):
    logout(request)
    return redirect('/')