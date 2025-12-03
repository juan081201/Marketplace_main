from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
<<<<<<< HEAD

from .models import Item, Category

from .forms import SignupForm, NewItemForm
=======
<<<<<<< HEAD
from django.contrib.auth.decorators import login_required
from .models import Item, Category

from .forms import SignupForm, NewItemForm
 
=======

from .models import Item, Category

from .forms import SignupForm, NewItemForm
>>>>>>> 02c616b2ffaa34c481adc325e929f0ae3b80dfb9
>>>>>>> cafb8291092cf80568e4e4fad28f361b900fb328

# Create your views here.
def home(request):
    items = Item.objects.filter(is_sold=False)
    categories = Category.objects.all()

    context = {
        'items': items,
        'categories': categories
    }
    return render(request, 'store/home.html', context)

def contact(request):
    context = {
        'msg': 'Quieres otros productos contactame!'
    }
    return render(request, 'store/contact.html', context)

def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
<<<<<<< HEAD
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[0:3]
=======
<<<<<<< HEAD
    related_items = Item.objects.filter(Category=item.Category, is_sold=False).exclude(pk=pk)[0:3]

=======
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[0:3]
>>>>>>> 02c616b2ffaa34c481adc325e929f0ae3b80dfb9
>>>>>>> cafb8291092cf80568e4e4fad28f361b900fb328
    context={
        'item': item,
        'related_items': related_items
    }

    return render(request, 'store/item.html', context)

def register(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignupForm()

    context = {
        'form': form
    }

    return render(request, 'store/signup.html', context)

def logout_user(request):
    logout(request)

    return redirect('home')

<<<<<<< HEAD
=======
<<<<<<< HEAD

=======
>>>>>>> 02c616b2ffaa34c481adc325e929f0ae3b80dfb9
>>>>>>> cafb8291092cf80568e4e4fad28f361b900fb328
@login_required
def add_item(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)

        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()

            return redirect('detail', pk=item.id)
    else:
        form = NewItemForm()
        context = {
            'form': form,
            'title': 'New Item'
        }
<<<<<<< HEAD

    return render(request, 'store/form.html', context)
=======
<<<<<<< HEAD
        
=======

>>>>>>> 02c616b2ffaa34c481adc325e929f0ae3b80dfb9
    return render(request, 'store/form.html', context)
>>>>>>> cafb8291092cf80568e4e4fad28f361b900fb328
