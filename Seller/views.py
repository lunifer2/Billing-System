from django.shortcuts import render

# Create your views here.
def seller_dashboard(request):
    return render(request,'sellerPanel/seller_dashboard.html')