
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import DeleteView,CreateView,UpdateView
from .models import Item
from .forms import FormItem
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class HomeView(TemplateView):
    template_name = 'Inv_app/home.html'
 
class ItemView(LoginRequiredMixin,ListView):
    model = Item
    template_name = 'Inv_app/inventario.html'
    context_object_name = 'items'

class DeleteItemView(DeleteView):
    model = Item
    template_name = 'Inv_app/delete_item.html'
    success_url = '/inventario/'
    
class UpdateItemView(UpdateView):
    model = Item
    form_class = FormItem
    template_name = 'Inv_app/update_item.html'
    success_url = '/inventario/'
    
class CreateItemView(CreateView):
    model = Item
    form_class = FormItem
    template_name = 'Inv_app/create_item.html'
    success_url = '/inventario/'