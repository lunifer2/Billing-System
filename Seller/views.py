from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth.models import User
from .forms import ItemCreateForm
from system.models import Item, Bill, CustomUser

# Create your views here.
def seller_dashboard(request):
    """ Returns the list of items """
    item_list = Item.objects.all().order_by('id')
    context = {"data": item_list}
    if request.method == "POST":
        search = request.POST.get('search')
        items = Item.objects.filter(item_name__icontains=search)
        context = {"data": items}
        return render(request, 'sellerPanel/seller_dashboard.html', context)
    return render(request,'sellerPanel/seller_dashboard.html',context)

class Item_add_view(View):
    """ This class adds the buyer """

    def get(self, request):
        if request.user.is_authenticated:
            user_role = request.user.role
            if user_role == "Seller":
                item_create_form = ItemCreateForm()
                context = {"form": item_create_form}
                return render(request, 'sellerPanel/items/items_add.html', context)
        return redirect('/login/')

    def post(self, request):
        if request.user.is_authenticated:
         user_role = request.user.role
         if user_role == "Seller":
            item = Item()
            item.item_name = request.POST.get('item_name')
            item.item_price = request.POST.get('item_price')
            item.item_description = request.POST.get('item_description')
            item.item_image = request.FILES.get('item_image')
            item.customusers = request.user
            item.save()
            return redirect('seller-dashboard')

        return redirect('/login/')
    
def item_index(request):
    """ Returns the list of items """
    item_list = Item.objects.all().order_by('id')
    context = {"data": item_list}
    if request.method == "POST":
        search = request.POST.get('search')
        items = Item.objects.filter(item_name__icontains=search)
        context = {"data": items}
        return render(request, 'sellerPanel/items/items_index.html', context)
    return render(request,'sellerPanel/items/items_index.html',context)

def item_delete(request, id):
    """ Deletes the items """
    data = Item.objects.get(id=id)
    data.delete()
    return redirect("seller-dashboard")


def item_view(request, id):
    """ Shows the profile of a item """
    data = Item.objects.get(id=id)
    context = {"data": data}
    return render(request, 'sellerPanel/items/items_view.html', context)


def item_edit(request, id):
    """ Edits the profile of a item """
    data = Item.objects.get(id=id)
    context = {"data": data}

    return render(request, 'sellerPanel/items/items_edit.html', context)


def item_update(request):
    if request.method == "POST":
        item = Item.objects.get(id=request.POST.get('id'))
        item.item_name = request.POST.get('item_name')
        item.item_price = request.POST.get('item_price')
        item.item_description = request.POST.get('item_description')
        item.item_image = request.FILES.get('item_image')
        item.customusers = request.user
        item.save()

    return redirect('index-seller')
