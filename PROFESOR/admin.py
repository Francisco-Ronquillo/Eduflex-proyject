from django.contrib import admin
from EDUFLEX.utils import  cifrar_contraseña
from PROFESOR.models import Profesor
@admin.register(Profesor)
class ProfesorAdmin(admin.ModelAdmin):
    list_display = ('nombres', 'apellidos', 'usuario', 'email', 'especializacion', 'genero', 'fecha_nac')
    search_fields = ('usuario', 'email', 'nombres', 'apellidos')

    def save_model(self, request, obj, form, change):
        # Si la contraseña fue modificada o es creación
        if not change or 'contraseña' in form.changed_data:
            obj.contraseña = cifrar_contraseña(obj.contraseña)
        super().save_model(request, obj, form, change)

