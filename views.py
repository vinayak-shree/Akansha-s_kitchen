from django.shortcuts import render , redirect , get_object_or_404
from .models import *
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate , login , logout



# Create your views here.
def add_recepies(request):
    data = request.POST
    # request.post is used to get data
    if request.method == "POST":
        data  = request.POST

        Recepie.objects.create(
            recepie_image = request.FILES.get('recepie_image'),
            recepie_description = data.get('recepie_description'),
            recepie_category = data.get('recepie_category' , None),
            recepie_name = data.get('recepie_name'),
            # recepie_category = data.get('recepie_category' , None),
            recepie_link = data.get('recepie_link')
        )
        # print(recepie_name)
        # print(recepie_description)
    # inko print krwane k lie
        return redirect('/add_recepies/')
    
    # queryset = Recepie.objects.all()
    # context = {'recepies':queryset}
    return render(request,'add-recepies.html')


def home(request):
    return render(request,'index.html')

def aboutt(request):
    return render(request,'sticker.html')

def all_recepies(request):
    queryset = Recepie.objects.all()
    context = {'recepies':queryset}
    # return render(request,'add-recepies.html' , context)
    return render(request , "recepie_list.html" , context)

def category_recepie(request , category):
    recepies = Recepie.objects.filter(
        recepie_category=category
    )

    return render(
        request,
        'info.html',
        {'recepies': recepies, 'category': category}
    )

def recepie_ingredients(request , id):
    recepie = Recepie.objects.get(id = id)
    return render(request , 'ingredients.html',{
        'recepie':recepie
    })


def delete_recepie(request, id):
    recepie = get_object_or_404(Recepie, id=id)
    recepie.delete()
    return redirect('/all_recepies/')

def contact(request):
    return render(request,'contact.html')

def adminUser(request):
    return render(request , 'adminUser.html')



def admin_login(request):

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect('/adminUser/')

        else:
            return render(
                request,
                'Login.html',
                {'error': 'Invalid Username or Password'}
            )

    return render(request, 'Login.html')

def update_recepies(request , id):
    queryset = Recepie.objects.get(id = id)

    if request.method == "POST":
        data = request.POST

        recepie_image = request.FILES.get('recepie_image')
        recepie_description = data.get('recepie_description')
        recepie_category = data.get('recepie_category' , None)
        recepie_name = data.get('recepie_name')
            # recepie_category = data.get('recepie_category' , None),
        recepie_link = data.get('recepie_link')

        queryset.recepie_name = recepie_name
        queryset.recepie_category = recepie_category
        queryset.recepie_description = recepie_description
        queryset.recepie_link = recepie_link

        if recepie_image:
            queryset.recepie_image = recepie_image

        queryset.save()
        return redirect('update_recepies' , id = id)
    context = {'recepie':queryset}
    return render(request , 'update_recepies.html' , context)


def user_logout(request):
    logout(request)
    return redirect('login')