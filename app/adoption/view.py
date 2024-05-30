from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView
from django.shortcuts import get_object_or_404, render
from .models import Questionnaire, AdoptionApplication
from pet.models import Pet
from .forms import AdoptionApplicationForm
from blog.filters import BlogFilter


class ApplyForAdoptionView(CreateView):
    model = AdoptionApplication
    form_class = AdoptionApplicationForm
    template_name = 'adoption/apply.html'
    success_url = reverse_lazy('adoption_success')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        pet = get_object_or_404(Pet, id=self.kwargs['pet_id'])
        questionnaire = get_object_or_404(Questionnaire, shelter=pet.shelter)
        kwargs.update({'questionnaire': questionnaire, 'initial': {'user': self.request.user, 'pet': pet, 'questionnaire': questionnaire}})
        return kwargs
    
    def get(self, request, *args, **kwargs):
        self.object = None
        filter = BlogFilter(request.GET)

        form = self.get_form()
        pet = get_object_or_404(Pet, id=self.kwargs['pet_id'])
        context = self.get_context_data(form=form, pet_name=pet.name)
        context['filter'] = filter

        if request.htmx:
            context['extends_base'] = 'partials/empty_base.html'
            return render(request, 'adoption/apply.html', context)
        context['extends_base'] = 'base.html'
        return self.render_to_response(context)

class AdoptionApplicationListView(ListView):
    model = AdoptionApplication
    template_name = 'adoption_application_list.html'
    context_object_name = 'applications'

    def get_queryset(self):
        return AdoptionApplication.objects.filter(user=self.request.user)

class AdoptionApplicationDetailView(DetailView):
    model = AdoptionApplication
    template_name = 'adoption_application_detail.html'
    context_object_name = 'application'
