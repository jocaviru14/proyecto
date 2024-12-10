# apps/tu_app/admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario
from .forms import UsuarioCreationForm, UsuarioChangeForm

class UsuarioAdmin(UserAdmin):
    add_form = UsuarioCreationForm
    form = UsuarioChangeForm
    model = Usuario
    list_display = ('username', 'email', 'nombres', 'apellidos', 'usuario_activo', 'usuario_administrador')
    list_filter = ('usuario_activo', 'usuario_administrador')

    fieldsets = (
        (None, {'fields': ('username', 'email', 'nombres', 'apellidos', 'telefono', 'password')}),
        ('Permissions', {'fields': ('usuario_activo', 'usuario_administrador')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'nombres', 'apellidos', 'telefono', 'password1', 'password2', 'usuario_activo', 'usuario_administrador')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)

admin.site.register(Usuario, UsuarioAdmin)

