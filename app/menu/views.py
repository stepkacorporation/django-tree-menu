from django.views.generic import TemplateView


class ExampleView(TemplateView):
    template_name = 'menu/example.html'