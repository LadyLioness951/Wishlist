from django.shortcuts import render
from .models import Wishlist

# Create your views here.
def wishlist_index(request):
    wishlist = Wishlist.objects.all()
    return render(request, 'wishlist/index.html', {'wishlist': wishlist})