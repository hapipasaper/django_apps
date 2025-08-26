from django.shortcuts import render

def profile(request):
    user_data = {
        'name': 'Ali Ahmed',
        'email': 'Ali@example.com',
        'age': 25,
        'skills': ['python', 'django', 'html', 'css']
    }
    return render(request, 'app2/profile.html', {'user': user_data})