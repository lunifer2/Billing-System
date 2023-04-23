from django.http import HttpResponse
from django.shortcuts import render, redirect
from authentication.views import RegisterView
from .forms import BillCreateForm, BuyerCreateForm, ItemCreateForm, OrderCreateForm, PaymentInfoCreateForm, SellerCreateForm
from .models import Bill, Buyer, Seller, Item, Order
from django.views import View
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import CustomUser
# Create your views here.
# for admin panel 
@login_required(login_url='login')
def index(request):
    user = request.user
    context = {"data":user}
    return render(request, 'adminPanel/buyers_index.html', context)

class Buyer_add_view(View):
    """ This class adds the buyer """

    def get(self, request):
        if request.user.is_authenticated:
            buyer_create_form = BuyerCreateForm()
            context = {"form": buyer_create_form}
            return render(request, 'adminPanel/buyers/buyers_add.html', context)
        return redirect('/login/')

    def post(self, request):
        if request.user.is_authenticated:
         buyer_view = RegisterView()
         response =buyer_view.post(request)
         # check if account was created successfully
         if response.status_code == 302:
            # stay on the same page
            return render(request, 'adminPanel/buyers/buyers_index.html')
         # if account creation failed, return the response
         return response
        return redirect('/login/')
    
@login_required(login_url='login')
def buyer_index(request):
    """ Returns the list of buyer """
    buyer_list = CustomUser.objects.filter(role="Buyer").order_by('id')
    context = {"data": buyer_list}
    if request.method == "POST":
        search = request.POST.get('search')
        buyers = CustomUser.objects.filter(role="Buyer",first_name__icontains=search)
        context = {"data": buyers}
        return render(request, 'adminPanel/buyers/buyers_index.html', context)
    return render(request, 'adminPanel/buyers/buyers_index.html', context)

@login_required(login_url='login')
def buyer_delete(request, id):
    """ Deletes the buyers """
    data = CustomUser.objects.get(id=id)
    data.delete()
    return redirect("index-buyer")


@login_required(login_url='login')
def buyer_view(request, id):
    """ Shows the profile of a Buyer """
    data = CustomUser.objects.get(id=id)
    context = {"data": data}
    return render(request, 'adminPanel/buyers/buyers_view.html', context)


@login_required(login_url='login')
def buyer_edit(request, id):
    """ Edits the profile of a buyer """
    data = CustomUser.objects.get(id=id)
    context = {"data": data}

    return render(request, 'adminPanel/buyers/buyers_edit.html', context)


@login_required(login_url='login')
def buyer_update(request):
    if request.method == "POST":
        buyer = CustomUser.objects.get(id=request.POST.get('id'))
        buyer.first_name = request.POST.get('first_name')
        buyer.last_name = request.POST.get('last_name')
        buyer.username = request.POST.get('username')
        buyer.password = request.POST.get('password')
        buyer.email = request.POST.get('email')
        buyer.address = request.POST.get('address')
        buyer.contact = request.POST.get('contact')
        buyer.gender = request.POST.get('gender')
        buyer.role = request.POST.get('role')
        buyer.save()

    return redirect('index-buyer')

class Seller_add_view(View):
    """ This class adds the seller """

    def get(self, request):
        if request.user.is_authenticated:
            seller_create_form = SellerCreateForm()
            context = {"form": seller_create_form}
            return render(request, 'adminPanel/sellers/sellers_add.html', context)
        return redirect('/login/')

    def post(self, request):
        if request.user.is_authenticated:
         seller_view = RegisterView()
         response =seller_view.post(request)
         # check if account was created successfully
         if response.status_code == 302:
            # stay on the same page
            return render(request, 'adminPanel/sellers/sellers_index.html')
         # if account creation failed, return the response
         return response
        return redirect('/login/')
    
@login_required(login_url='login')
def seller_index(request):
    """ Returns the list of seller """
    seller_list = CustomUser.objects.filter(role="Seller").order_by('id')
    context = {"data": seller_list}
    if request.method == "POST":
        search = request.POST.get('search')
        sellers = CustomUser.objects.filter(role="Seller", first_name__icontains=search)
        context = {"data": sellers}
        return render(request, 'adminPanel/sellers/sellers_index.html', context)
    return render(request, 'adminPanel/sellers/sellers_index.html', context)

@login_required(login_url='login')
def seller_delete(request, id):
    """ Deletes the sellers """
    data = CustomUser.objects.get(id=id)
    data.delete()
    return redirect("index-seller")


@login_required(login_url='login')
def seller_view(request, id):
    """ Shows the profile of a seller """
    data = CustomUser.objects.get(id=id)
    context = {"data": data}
    return render(request, 'adminPanel/sellers/sellers_view.html', context)


@login_required(login_url='login')
def seller_edit(request, id):
    """ Edits the profile of a seller """
    data = CustomUser.objects.get(id=id)
    context = {"data": data}

    return render(request, 'adminPanel/sellers/sellers_edit.html', context)


@login_required(login_url='login')
def seller_update(request):
    if request.method == "POST":
        seller = CustomUser.objects.get(id=request.POST.get('id'))
        seller.first_name = request.POST.get('first_name')
        seller.last_name = request.POST.get('last_name')
        seller.username = request.POST.get('username')
        seller.password = request.POST.get('password')
        seller.email = request.POST.get('email')
        seller.address = request.POST.get('address')
        seller.contact = request.POST.get('contact')
        seller.gender = request.POST.get('gender')
        seller.role = request.POST.get('role')
        seller.save()

    return redirect('index-seller')

#for seller panel
def seller_dashboard(request):
    return render(request,'sellerPanel/seller_dashboard.html')