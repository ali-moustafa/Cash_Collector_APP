from django.contrib.auth import authenticate, login
from django.http import JsonResponse


def LoginView(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return JsonResponse({'message': 'Login successful.'})
        else:
            return JsonResponse({'message': 'Invalid username or password.'}, status=401)

    return JsonResponse({'message': 'Method not allowed.'}, status=405)