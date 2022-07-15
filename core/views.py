from django.shortcuts import render,redirect
from .forms import SignUpForm
from django.contrib.auth import login

# Create your views here.
def frontpage(request):
    return render(request,('core/frontpage.html'))

def signup(request):
    if request.method=='POST':
        form=SignUpForm(request.POST)

        if form.is_valid():
            user=form.save()
            login(request,user)

            return redirect('frontpage')

    else:
        form=SignUpForm()  #if it is not a post request , create nan empty instance
    
    return render(request, 'core/signup.html', {'form': form})