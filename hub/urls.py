from os import read
from .views import about_us, acidity, beans, blend, culture, customizing, grind, home, machines, products
from django.urls import path

urlpatterns = [
        path('',home, name="home_page"),
        path('products/', products,name='products'),
        path('machines/', machines,name='machines'),
        path('about_us/', about_us,name='about_us'),
        path('customizing/',customizing,name='customizing'),

        path('culture/',culture,name='culture'),
        path('grind/', grind,name='grind'),
        path('acidity/', acidity,name='acidity'),
        path('beans/', beans,name='beans'),

        path('blend/', blend,name='blend'),

]