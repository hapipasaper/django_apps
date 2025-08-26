from django.shortcuts import render

def product_list(request):
    products = [
        {'name': 'Laptop', 'price': 999.99, 'available': True},
        {'name': 'Smartphone', 'price': 699.50, 'available': False},
        {'name': 'Headphones', 'price': 59.99, 'available': True},
    ]
    return render(request, 'app3/products.html', {'products': products})