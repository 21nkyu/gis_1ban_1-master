from django.urls import path
from django.views.generic import TemplateView

app_name = "articleapp" #지정해 줘야 reverse_lazy 역산?

urlpatterns =[
    path('list/', TemplateView.as_view(template_name='articleapp/list.html'), name='list')

]
