from datetime import datetime
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from system.models import CustomUser, Order, Item, Bill
from .forms import OrderCreateForm, PaymentCreateForm
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required(login_url='login')
def buyer_dashboard(request):
    """ Returns the list of items """
    item_list = Item.objects.all().order_by('id')
    context = {"data": item_list}
    if request.method == "POST":
        search = request.POST.get('search')
        items = Item.objects.filter(item_name__icontains=search)
        context = {"data": items}
        return render(request, 'buyerPanel/buyer_dashboard.html', context)
    return render(request, 'buyerPanel/buyer_dashboard.html', context)


class Order_add_view(View):
    """ This class adds the order """

    def get(self, request):
        if request.user.is_authenticated:
            user_role = request.user.role
            if user_role == "Seller":
                order_create_form = OrderCreateForm()
                context = {"form": order_create_form}
                return render(request, 'buyerPanel/orders/order_add.html', context)
        return redirect('/login/')

    def post(self, request):
        if request.user.is_authenticated:
            user_role = request.user.role
            if user_role == "Buyer":
                item = Item()
                item.item_name = request.POST.get('item_name')
                item.item_price = request.POST.get('item_price')
                item.item_description = request.POST.get('item_description')
                item.item_image = request.FILES.get('item_image')
                item.customusers = request.user
                item.save()
                return redirect('buyer-dashboard')

        return redirect('/login/')


@login_required(login_url='login')
def buyItem(request, id):
    if request.user.is_authenticated:
        user_role = request.user.role
        if user_role == "Buyer":
            data = Item.objects.get(id=id)
            context = {"data": data}
        return render(request, 'buyerPanel/orders/order_items.html', context)
    return redirect('/login/')


@login_required(login_url='login')
def item_view(request, id):
    """ Shows the profile of a item """
    if request.user.is_authenticated:
        user_role = request.user.role
        if user_role == "Buyer":
            data = Item.objects.get(id=id)
            context = {"data": data}
            return render(request, 'buyerPanel/items/items_view.html', context)
    return redirect('/login/')


@login_required(login_url='login')
def add_order(request, id):
    if request.method == 'POST':
        quantity = int(request.POST['quantity'])
        item = Item.objects.get(id=id)
        buyer = CustomUser.objects.get(id=request.user.id)
        order = Order.objects.create(
            order_quantity=quantity,
            item_id=item,
            customusers=buyer,
            order_status='UnVerified'
        )
        order.save()
        return redirect('buyer-dashboard')
    else:
        return redirect('buyer-dashboard')


@login_required(login_url='login')
def order_index(request):
    """ Returns the list of orders """
    verified_orders = Order.objects.filter(customusers=request.user, order_status='Verified')
                                            
    bills = Bill.objects.filter(order_id__in=verified_orders)
    context = {"data": bills}
    if request.method == "POST":
        search = request.POST.get('search')
        bills = Bill.objects.filter(order_id__item_id__item_name__icontains=search,
                                    order_id__customusers=request.user, order_id__order_status='Verified')
        context = {"data": bills}
        return render(request, 'buyerPanel/orders/order_index.html', context)
    return render(request, 'buyerPanel/orders/order_index.html', context)


@login_required(login_url='login')
# def bill_index(request, id):
#     """ Shows the profile of an order """
#     order = Order.objects.select_related('item_id__customusers').get(id=id)
#     bills = Bill.objects.select_related('order_id__customusers').get(id=id)
#     item = order.item_id
#     bills = Bill.objects.filter(order_id=id)
#     context = {"order": order, "item": item, "bills": bills}
#     return render(request, 'buyerPanel/orders/orders_view.html', context)
def bill_index(request, id):
    """ Returns the list of orders """
    verified_orders = Order.objects.filter(
        customusers=request.user, order_status='Verified')
    bills = Bill.objects.filter(order_id__in=verified_orders)
    context = {"data": bills}
    return render(request, 'buyerPanel/orders/orders_view.html', context)


# @login_required(login_url='login')
# def payment_create(request, bill_id):
#     bill = get_object_or_404(Bill, id=bill_id)
#     if request.method == 'POST':
#         payment_form = PaymentCreateForm(request.POST)
#         if payment_form.is_valid():
#             payment_info = payment_form.save(commit=False)
#             payment_info.customusers = request.user
#             payment_info.save()
#             bill.bill_status = Bill.PAID
#             bill.paid_date = datetime.now()
#             bill.save()
#             return redirect('order-index')
#     else:
#         form = PaymentCreateForm()
#     return render(request, 'buyerPanel/payments/payment_create.html', {'form': form, 'bill': bill})



def payment_create(request, bill_id):
    bill = get_object_or_404(Bill, id=bill_id)
    if request.method == 'POST':
        payment_form = PaymentCreateForm(request.POST)
        if payment_form.is_valid():
            payment_info = payment_form.save(commit=False)
            payment_info.customusers = request.user
            payment_info.save()
            bill.bill_status = Bill.PAID
            bill.paid_date = datetime.now()
            bill.save()
            
            # Update total earnings for the seller
            seller = bill.order_id.item_id.customusers
            if bill.bill_status == Bill.PAID:
                earnings = seller.total_earnings + bill.order_id.total_cost
                CustomUser.objects.filter(id=seller.id).update(total_earnings=earnings)
            
            return redirect('order-index')
    else:
        form = PaymentCreateForm()
    return render(request, 'buyerPanel/payments/payment_create.html', {'form': form, 'bill': bill})
