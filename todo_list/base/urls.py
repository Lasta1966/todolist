from django.urls import path
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, DeleteView, CustomLoginView, RegisterPage
from django.contrib.auth.views import LogoutView

urlpatterns = [
    # URL maršrutas prisijungimui. Naudojamas CustomLoginView, kuris gali būti pritaikytas pagal jūsų poreikius.
    path('login/', CustomLoginView.as_view(), name='login'),
    
    # URL maršrutas atsijungimui. Po sėkmingo atsijungimo nukreipia vartotoją į prisijungimo puslapį.
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    
    # URL maršrutas vartotojo registracijai. Naudojamas RegisterPage vaizdas.
    path('register/', RegisterPage.as_view(), name='register'),
    
    # Pagrindinis puslapis, kuriame pateikiamas užduočių sąrašas.
    path('', TaskList.as_view(), name='tasks'),
    
    # Detali užduoties peržiūra pagal jos unikalų ID (pk - primary key).
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
    
    # Užduoties kūrimo puslapis.
    path('task-create/', TaskCreate.as_view(), name='task-create'),
    
    # Užduoties atnaujinimo puslapis pagal jos unikalų ID.
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name='task-update'),
    
    # Užduoties šalinimo puslapis pagal jos unikalų ID.
    path('task-delete/<int:pk>/', DeleteView.as_view(), name='task-delete'),
]
