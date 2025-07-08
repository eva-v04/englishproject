from django.shortcuts import render
from django.shortcuts import redirect
from .forms import SignUp

# Create your views here.
def homepage(request):
    return render(request, 'homepage.html')

def signup(request):
    if request.method == 'POST':
        form = SignUp(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = SignUp()
    return render(request, 'signup.html', {'form': form})