from django.shortcuts import render
from randomizer.models import Restaurant
from random import choice
from randomizer.forms import RestaurantForm

# Create your views here.

def index(request):
	rests = Restaurant.objects.order_by('name')
	restaurant = choice(Restaurant.objects.all())
	
	
	if request.method == 'POST':
		form = RestaurantForm(request.POST)
		if form.is_valid():
			newrest = form.save(commit=False)
			newrest.save()
				
			
		else:
			print form.errors
	else:
		form = RestaurantForm()
	
	context = {'rests': rests,
				'form': form,
				'restaurant': restaurant
				}
	
	return render(request, 'randomizer/index.html', context)
