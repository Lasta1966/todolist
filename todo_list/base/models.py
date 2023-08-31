from django.db import models
from django.contrib.auth.models import User

# Užduoties modelis, kuriame saugomos užduočių informacijos.
class Task(models.Model):
    # Susieja užduotį su konkrečiu vartotoju.
    # Jei vartotojas bus pašalintas, visos jo užduotys taip pat bus pašalintos.
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True) 
    
    # Užduoties pavadinimas. Gali būti tuščias.
    title = models.CharField(max_length=200, null=True, blank=True)
    
    # Ilgesnis užduoties aprašymas. Gali būti tuščias.
    description = models.TextField(null=True, blank=True)
    
    # Nurodo ar užduotis yra atlikta. Pagal nutylėjimą - "ne".
    complete = models.BooleanField(default=False)
    
    # Automatiškai nustato dabartinį laiką, kai užduotis sukurta.
    created = models.DateTimeField(auto_now_add=True)
    
    # Grąžina užduoties pavadinimą, kai modelio objektas konvertuojamas į tekstą.
    def __str__(self):
        return self.title
    
    # Papildomos modelio savybės.
    class Meta:
        # Užduotys bus rūšiuojamos pagal būseną - neatliktos bus rodomos pirmiausia.
        ordering = ['complete']
