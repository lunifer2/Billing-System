from datetime import timezone
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from django.contrib.auth.models import User
from .forms import ItemCreateForm
from system.models import Item, Bill, CustomUser, Order
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.

@login_required(login_url='login')
def seller_dashboard(request):
    """ Returns the list of items """
    item_list = Item.objects.filter(customusers=request.user)
    context = {"data": item_list}
    if request.method == "POST":
        search = request.POST.get('search')
        items = Item.objects.filter(item_name__icontains=search)
        context = {"data": items}
        return render(request, 'sellerPanel/seller_dashboard.html', context)
    return render(request, 'sellerPanel/seller_dashboard.html', context)


class Item_add_view(View):
    """ This class adds the items """

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
                item.customusers_id = request.user.id
                item.save()
                return redirect('seller-dashboard')

        return redirect('/login/')


@login_required(login_url='login')
def item_index(request):
    """ Returns the list of items """
    item_list = Item.objects.filter(customusers=request.user).order_by('id')
    context = {"data": item_list}
    if request.method == "POST":
        search = request.POST.get('search')
        items = Item.objects.filter(item_name__icontains=search)
        context = {"data": items}
        return render(request, 'sellerPanel/items/items_index.html', context)
    return render(request, 'sellerPanel/items/items_index.html', context)


@login_required(login_url='login')
def item_delete(request, id):
    """ Deletes the items """
    data = Item.objects.get(id=id)
    data.delete()
    return redirect("seller-dashboard")


@login_required(login_url='login')
def item_view(request, id):
    """ Shows the profile of a item """
    data = Item.objects.get(id=id)
    context = {"data": data}
    return render(request, 'sellerPanel/items/items_view.html', context)


@login_required(login_url='login')
def item_edit(request, id):
    """ Edits the profile of a item """
    data = Item.objects.get(id=id)
    context = {"data": data}

    return render(request, 'sellerPanel/items/items_edit.html', context)


@login_required(login_url='login')
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


@login_required(login_url='login')
def order_index(request):
    """ Returns the list of orders """
    order_list = Order.objects.filter(
        item_id__customusers=request.user).order_by('id')
    context = {"data": order_list}
    if request.method == "POST":
        search = request.POST.get('search')
        order = Order.objects.filter(item_id__item_name__icontains=search)
        context = {"data": order}
        return render(request, 'sellerPanel/orders/orders_index.html', context)
    return render(request, 'sellerPanel/orders/orders_index.html', context)


@login_required(login_url='login')
def order_view(request, id):
    """ Shows the profile of a order """
    order_list = Order.objects.filter(
        item_id__customusers=request.user).order_by('id')
    context = {"order": order_list}
    return render(request, 'sellerPanel/orders/orders_view.html', context)


@login_required(login_url='login')
def bill_index(request, id):
    """ Shows the profile of an order """
    order = Order.objects.select_related('item_id__customusers').get(id=id)
    item = order.item_id
    bills = Bill.objects.filter(order_id=id)
    context = {"order": order, "item": item, "bills": bills}
    return render(request, 'sellerPanel/orders/orders_view.html', context)


@login_required(login_url='login')
def create_bill(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    order.order_status = Order.VERIFIED
    order.save()

    bill = Bill.objects.create(
        bill_status=Bill.UNPAID,
        customusers=order.customusers,
        order_id=order,
    )
    messages.success(request, 'Bill created successfully.')
    return redirect('seller-order-index')


class Bill_add_view(View):
    """ This class adds the bill """

    def get(self, request, order_id):
        if request.user.is_authenticated:
            var = order_id
            user_role = request.user.role
            if user_role == "Seller":
                orderDetail = Order.objects.filter(id=var)
                order = get_object_or_404(Order, pk=order_id)
                context = {"order": order, "od": orderDetail}
                return render(request, 'sellerPanel/bills/bills_add.html', context)
        return redirect('/login/')

    def post(self, request, order_id):
        if request.user.is_authenticated:
            user_role = request.user.role
            if user_role == "Seller":
                order = get_object_or_404(Order, pk=order_id)
                seller = CustomUser.objects.get(id=request.user.id)
                bill_status = request.POST.get('bill_status')
                bill = Bill.objects.create(
                    bill_status=bill_status,
                    order_id=order,
                    customusers=seller
                )
                # Check if the bill is paid and set the paid_date accordingly
                if bill.bill_status == 'paid':
                    bill.paid_date = timezone.now()
                bill.save()
                return redirect('bill-index')
        return redirect('/login/')
