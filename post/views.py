from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import CommentForm
# Create your views here.
from .models import Boutique, Maison, Poster, Commentaire, Terrain
from member.models import Profile


# Create your views here.
def home(request):
    carroussel = Maison.objects.filter()
    form = Poster.objects.filter()
    context = {'form': form, 'carroussel': carroussel }
    return render(request, 'Home.html', context)


@login_required(login_url='login')
def comment(request, id, *args, **kwargs):
    profile = Profile.user.username
    post = Poster.objects.get(id=id)
    form = CommentForm(request.POST)
    if request.method == 'POST':
        Commentaire.id_user = profile
        form.save()
        return redirect('home')
    form = CommentForm()
    context = {'form': form}
    return render(request, 'home.html', context)

def maison(request, *args, **kwargs):
    all = Maison.objects.all().order_by(id)
    post = Poster.objects.filter(id_MA=all)
    form = post
    context ={'form': form}
    return render(request, 'Produits_et_service.html', context)

def terrain(request, *args, **kwargs):
    all = Terrain.objects.all()
    post = Poster.objects.filter(id_TE=all.id)
    form = post
    context ={'form': form}
    return render(request, 'Produits_et_service.html', context)

def boutique(request, *args, **kwargs):
    all = Boutique.objects.all()
    post = Poster.objects.filter(id_BO=all.id)
    form = post
    context ={'form': form}
    return render(request, 'Produits_et_service.html', context)

