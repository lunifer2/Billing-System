from django.shortcuts import redirect, render
from django.views import View
from system.models import CustomUser, Order, Item
from .forms import OrderCreateForm
# Create your views here.
def buyer_dashboard(request):
    """ Returns the list of items """
    item_list = Item.objects.all().order_by('id')
    context = {"data": item_list}
    if request.method == "POST":
        search = request.POST.get('search')
        items = Item.objects.filter(item_name__icontains=search)
        context = {"data": items}
        return render(request, 'buyerPanel/buyer_dashboard.html', context)
    return render(request,'buyerPanel/buyer_dashboard.html',context)

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
    
def buyItem(request, id):
    if request.user.is_authenticated:
        user_role = request.user.role
        if user_role == "Buyer":
         data = Item.objects.get(id=id)
         context = {"data": data}
        return render(request, 'buyerPanel/orders/order_items.html', context)
    return redirect('/login/')

def item_view(request, id):
    """ Shows the profile of a item """
    if request.user.is_authenticated:
        user_role = request.user.role
        if user_role == "Buyer":
            data = Item.objects.get(id=id)
            context = {"data": data}
        return render(request, 'buyerPanel/items/items_view.html', context)
    return redirect('/login/')

def add_order(request, id):
    if request.method == 'POST':
        quantity = int(request.POST['quantity'])
        item = Item.objects.get(id=id)
        buyer = CustomUser.objects.get(user=request.user)
        order = Order.objects.create(
            order_quantity=quantity,
            item_id=item,
            customusers=buyer,
            order_status='UnVerified'
        )
        order.save()
        return redirect('buyer-dashboard')
    else:
        # item = Item.objects.get(id=id)
        # return render(request, 'buyerPanel/orders/order_items.html', {'item': item})
        return redirect('buyer-dashboard')
