from django.shortcuts import render

# Create your views here.
def ntr(request):
    return render(request,'ntr.html')

def happy(request):
    return render(request,'happy.html')
