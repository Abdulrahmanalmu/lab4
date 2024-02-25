from django.shortcuts import render

# Create your views here.

def default_view(request):
    return render(request, 'tax_app/index.html')

def calculate_tax(request, price):
    tax_rate = 0.15
    total_price = price * (1 + tax_rate)
    return render(request, 'tax_app/calculate_tax.html', {'total_price': total_price})

def tax_rate_view(request):
    tax_rate = 0.15
    return render(request, 'tax_app/taxrate.html', {'tax_rate': tax_rate})
