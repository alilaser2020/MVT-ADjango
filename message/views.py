from django.views.generic import TemplateView


class ViewMessage(TemplateView):
    template_name = 'home.html'

