import os 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lunch.settings')

import django
django.setup()

from randomizer.models import Restaurant 

def populate():
	r1 = add_restaurant('Salaams')
	r2 = add_restaurant('Homemeal')
	r3 = add_restaurant('HealthyFoods')
	
	for r in Restaurant.objects.all():
		print "- {0} -".format(r.name)
	
	
def add_restaurant(name):
	r = Restaurant.objects.get_or_create(name=name)[0]
	r.save()
	return r
	
if __name__ == '__main__':
    print "Starting jobslist population script..."
    populate()