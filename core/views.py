from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required


def index(request):
    return render(request, 'core/index.html')

def about(request):
    return render(request, 'core/about.html')


    
@staff_member_required
def products(request):
    return render(request, 'core/products.html')











