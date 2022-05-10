from django.shortcuts import render

def home(request):
    return render(request,'home.html')

def products(request):
    return render(request, 'products.html')    

def machines(request):
    return render(request,'machines.html')


def about_us(request):
    return render(request,'about.html')    

def culture(request):
    return render(request,'culture.html')   

def customizing(request):
    return render(request, 'customizing.html') 

def acidity(request):
    return render(request, 'acidity.html')    

def grind(request):
    return render(request, 'grind.html')  

def beans(request):
    return render(request, 'beans.html')         

def blend(request):
    return render(request, 'blend.html')      