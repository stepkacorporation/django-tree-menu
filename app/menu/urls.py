from django.urls import path

from .views import ExampleView

app_name = 'menu'

urlpatterns = [
    path('', ExampleView.as_view(), name='example'),
]
