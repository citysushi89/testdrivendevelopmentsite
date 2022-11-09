from django.shortcuts import render, redirect
from django.http import HttpResponse
from lists.models import Item, List
from django.views.decorators.csrf import csrf_protect

# Create your views here.
def home_page(request):
    return render(request, 'home.html')

@csrf_protect
def view_list(request, id):
    list_ = List.objects.get(id=id)
    return render(request, 'list.html', {'list': list_})

@csrf_protect
def new_list(request):
    list_ = List.objects.create()
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect(f'/lists/{list_.id}/')
    
@csrf_protect
def add_item(request, id):
    list_ = List.objects.get(id=id)
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect(f'/lists/{list_.id}/')