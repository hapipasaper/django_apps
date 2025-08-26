from django.shortcuts import render

def home(request):
    name = 'Habiba'
    items = ['Apple', 'Banana', 'Mango']
    context = {'name': name, 'items': items}
    return render(request, 'app1/home.html', context)