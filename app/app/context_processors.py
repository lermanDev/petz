from django.db.models import Count
from shelter.models import State
from pet.models import Specie
from blog.models import BlogCategory

def species_context(request):
    species = Specie.objects.annotate(num_pets=Count('pet')).order_by('-num_pets')
    states = State.objects.all()
    return {'species_list': species, 'states_list': states}


def blog_categories_context(request):
    categories = BlogCategory.objects.annotate(num_posts=Count('blogpost')).order_by('-num_posts')
    return {'blog_categories': categories}