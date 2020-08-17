from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def index(request):
    treasures = Treasure.objects.all()
    form = TreasureForm()
    return render(request, "index.html", {"treasures": treasures, "form": form})


def detail(request, treasure_id):
    treasure = Treasure.objects.get(id=treasure_id)
    return render(request, "detail.html", {"treasure": treasure})


def post_treasure(request, username):
    form = TreasureForm(request.POST, request.FILES)
    if form.is_valid():
        treasure = form.save(commit=False)
        treasure.user = request.user
        treasure.save()
    return HttpResponseRedirect("/user/{}/".format(request.user))


def profile(request, username):
    form = TreasureForm()
    user = User.objects.get(username=username)
    treasures = Treasure.objects.filter(user=user)
    return render(
        request,
        "profile.html",
        {"username": username, "treasures": treasures, "form": form},
    )


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            u = form.cleaned_data["username"]
            p = form.cleaned_data["password"]
            user = authenticate(username=u, password=p)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect("/")
                else:
                    print("The Account has been disabled!")
            else:
                messages.warning(
                    request, "Username and Password are incorrect", extra_tags="alert"
                )
                return HttpResponseRedirect("/")
    else:
        form = LoginForm()
        return render(request, "auth/login.html", {"form": form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/")


def like_treasure(request):
    treasure_id = request.POST.get("treasure_id", None)

    likes = 0
    if treasure_id:
        treasure = Treasure.objects.get(id=int(treasure_id))
        if treasure is not None:
            likes = treasure.likes + 1
            treasure.likes = likes
            treasure.save()
    return HttpResponse(likes)


def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect("/user/{}".format(request.user))
    else:
        form = SignUpForm()
    return render(request, "auth/signup.html", {"form": form})


# Create your views here.
