from django.views.generic import TemplateView
from adoption.models import AdoptionApplication
from pet.models import Pet
from adopter.models import Adopter
from blog.models import BlogPost
from shelter.models import Shelter

class HomeView(TemplateView):
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()

        context['latest_pets'] = Pet.objects.all().order_by('-created_at')[:6]
        context['latest_blog_posts'] = BlogPost.objects.all().order_by('-created_at')[:6]
        context['shelters'] = Shelter.objects.all().order_by('-created_at')[:12]

        context['extends_base'] = "base.html"

        # Counts
        context['pet_count'] = Pet.objects.count()
        context['shelter_count'] = Shelter.objects.count()
        context['adoption_count'] = AdoptionApplication.objects.count()
        context['history_count'] = BlogPost.objects.count()


        if request.htmx:
            context['extends_base'] = 'partials/empty_base.html'
            
        return self.render_to_response(context)