from django.urls import path

from .views import CreateCalculatorView

urlpatterns = [
    path('', CreateCalculatorView.as_view())
]