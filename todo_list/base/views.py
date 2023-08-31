from django.shortcuts import redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Task
from django.urls import reverse_lazy
# reverse_lazy yra Django funkcija, kuri skirta išgauti URL pagal tam tikrą URL vardo raktažodį. 
# Tai yra vėluojančio įvertinimo (lazy evaluation) versija funkcijos reverse, kuri taip pat skirta šiai pačiai paskirčiai.
# Skirtumas tarp reverse ir reverse_lazy yra tas, kad reverse_lazy grąžina vėluojančio įvertinimo URL objektą, kuris bus vertinamas tik tada, kai reikės realaus URL. 
# Tai ypač naudinga, kai norite nurodyti URL kaip pradinę reikšmę klasės atributui, nes kai klasė yra įkeliama, URL gali būti dar neapibrėžti.

# Prisijungimo langas
class CustomLoginView(LoginView):
    template_name = 'base/login.html'  # Prisijungimo šablonas.
    fields = '__all__'  
    redirect_authenticated_user = True  # Nukreipia prisijungusį vartotoją
    
    def get_success_url(self):
        return reverse_lazy('tasks')  # Nukreipimas po sėkmingo prisijungimo.

# Registracijos langas
class RegisterPage(FormView):
    template_name = 'base/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('tasks')
    
    def form_valid(self, form):
        user = form.save()  # Įrašo vartotoją į duomenų bazę.
        if user is not None:
            login(self.request, user)  # Prisijungia vartotoją.
        return super(RegisterPage, self).form_valid(form)
    
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('tasks')  # Nukreipia jei vartotojas jau prisijungęs.
        return super(RegisterPage, self). get(*args,**kwargs)

# Užduočių sąrašas
class TaskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)  # Rodoma tik vartotojo užduotys.
        context['count'] = context['tasks'].filter(complete=False).count()  # Nesutvarkytų užduočių skaičius.
        
        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['tasks'] = context['tasks'].filter(title__startswith=search_input)  # Užduočių paieška.
            
        context['search_input'] = search_input
        return context

# Detali užduoties informacija
class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'base/task.html'

# Užduoties kūrimas
class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('tasks')
    
    def form_valid(self, form):
        form.instance.user = self.request.user  # Priskiriama užduotis vartotojui.
        return super(TaskCreate, self).form_valid(form)

# Užduoties redagavimas
class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('tasks')

# Užduoties šalinimas
class DeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')
