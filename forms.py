from django import forms
from .models import entrenador,  atleta, categoria
from django.core.exceptions import ValidationError



OPCIONES_SEXO_MF_LARGA = [
    ('M', 'Masculino'),  # Clave DB: 'M', Etiqueta visible: 'Masculino'
    ('F', 'Femenino'),   # Clave DB: 'F', Etiqueta visible: 'Femenino'
]

class EntrenadorForm(forms.ModelForm):
    

    class Meta:
        model = entrenador
        fields = [
            'ci_entrenador', 
            'nom_entre', 
            'apell_entre', 
            'telf_entre', 
            'correo_entre', 
            'sexo_entre'
        ]
        
        labels = {
            'ci_entrenador': 'Cédula de Identidad',
            'nom_entre': 'Nombres', 
            'apell_entre': 'Apellidos', 
            'telf_entre': 'Teléfono Celular', 
            'correo_entre': 'Correo Electrónico',
            'sexo_entre': 'Sexo',
        }
        
        widgets = {
            'ci_entrenador': forms.TextInput(attrs={'class': 'form-control rounded-2', 'placeholder': 'Cédula sin guiones', 'maxlength': '15', 'pattern': r'\d{7,15}', 'required': True}),
            'nom_entre': forms.TextInput(attrs={'class': 'form-control rounded-2', 'placeholder': 'Nombres', 'pattern': r'[a-zA-ZñÑáéíóúÁÉÍÓÚ\s]+', 'required': True}),
            'apell_entre': forms.TextInput(attrs={'class': 'form-control rounded-2', 'placeholder': 'Apellidos', 'pattern': r'[a-zA-ZñÑáéíóúÁÉÍÓÚ\s]+', 'required': True}),
            'telf_entre': forms.TextInput(attrs={'class': 'form-control rounded-2', 'placeholder': '4125551234', 'maxlength': '10', 'pattern': r'[0-9]{10}', 'required': True}),
            'correo_entre': forms.EmailInput(attrs={'class': 'form-control rounded-2', 'placeholder': 'ejemplo@correo.com'}),
            
            # 🚨 ESTO ES CLAVE: Usamos Select y le pasamos las opciones M/F y la clase de Bootstrap
            'sexo_entre': forms.Select(
                choices=OPCIONES_SEXO_MF_LARGA, 
                attrs={'class': 'form-select rounded-2', 'required': True}
            ),
        }
        


class AtletaForm(forms.ModelForm):
    # El campo 'sexo' en el HTML usa botones de radio que necesitan ser tratados
    sexo = forms.ChoiceField(
        choices=atleta.OPCIONES_SEXO,
        required=True,
        # 💥 CORRECCIÓN: Usar forms.Select en lugar de forms.RadioSelect
        widget=forms.Select(attrs={'class': 'form-select rounded-2'}) 
    )
    
    # El campo 'talla' se deja como ChoiceField con Select
    OPCIONES_TALLA = [
        (40.0, 'S'),
        (42.0, 'M'),
        (44.0, 'L'),
        (46.0, 'XL'),
        (48.0, 'XXL'),
    ]
    talla = forms.ChoiceField(
        choices=OPCIONES_TALLA,
        required=True,
        widget=forms.Select(attrs={'class': 'form-select rounded-2'})
    )

    class Meta:
        model = atleta
        # Listado de campos del modelo que se incluirán en el formulario
        fields = [
            'ci_atleta', 'nom_atleta', 'apell_atleta', 'sexo', 'fecha_nac', 
            'altura', 'peso', 'talla', 'envergadura', 'telf_atleta', 
            'condicion', 'observacion', 'foto'
        ]
        
        # Asignación de widgets y clases de Bootstrap para estilizado
        widgets = {
            'ci_atleta': forms.TextInput(attrs={'class': 'form-control rounded-2', 'placeholder': 'Cédula de Identidad'}),
            'nom_atleta': forms.TextInput(attrs={'class': 'form-control rounded-2'}),
            'apell_atleta': forms.TextInput(attrs={'class': 'form-control rounded-2'}),
            'fecha_nac': forms.DateInput(attrs={'class': 'form-control rounded-2', 'type': 'date'}),
            'altura': forms.NumberInput(attrs={'class': 'form-control rounded-2', 'placeholder': 'Ej: 1.85', 'step': '0.01'}),
            'peso': forms.NumberInput(attrs={'class': 'form-control rounded-2', 'placeholder': 'Ej: 75.5', 'step': '0.01'}),
            'envergadura': forms.NumberInput(attrs={'class': 'form-control rounded-2', 'placeholder': 'Ej: 1.90', 'step': '0.01'}),
            'telf_atleta': forms.TextInput(attrs={'class': 'form-control rounded-2', 'placeholder': 'Ej: 4125551234'}),
            'condicion': forms.Textarea(attrs={'class': 'form-control rounded-2', 'rows': 4}),
            'observacion': forms.Textarea(attrs={'class': 'form-control rounded-2', 'rows': 4}),
            'foto': forms.FileInput(attrs={'class': 'form-control rounded-2', 'accept': 'image/*'}),
        }
        
        # Etiquetas (Labels) en español
        labels = {
            'ci_atleta': 'Cédula',
            'nom_atleta': 'Nombres',
            'apell_atleta': 'Apellidos',
            'fecha_nac': 'Fecha de Nacimiento del Atleta',
            'altura': 'Altura (m)',
            'peso': 'Peso (kg)',
            'talla': 'Talla (Uniforme)',
            'envergadura': 'Envergadura (m)',
            'telf_atleta': 'Teléfono Celular',
            'condicion': 'Condición del Atleta',
            'observacion': 'Observaciones del Atleta (Notas del Entrenador)',
            'foto': 'Cargar Foto del Atleta',
        }
        
        
# 📁 app_name/forms.py (CORREGIDO)


class CategoriaForm(forms.ModelForm): # Usa ModelForm
    
    class Meta:
        # ¡ESTO RESUELVE EL ERROR! Vincula el formulario al modelo
        model = categoria 
        
        # Define qué campos del modelo se incluirán en el formulario
        fields = ['nom_categoria', 'detalle_cat'] 
        
        # Widgets para aplicar estilos de Bootstrap/AdminLTE
        widgets = {
            'nom_categoria': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: U12 (2014-2015)',
            }),
            'detalle_cat': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Información adicional sobre la categoría.'
            }),
        }
        
        labels = {
            'nom_categoria': 'Nombre de la Categoría',
            'detalle_cat': 'Detalle/Descripción de la Categoría'
        }

    # Validación personalizada (clean_nom_categoria)
    def clean_nom_categoria(self):
        nombre = self.cleaned_data.get('nom_categoria').strip()
        
        if len(nombre) < 3:
            raise ValidationError("El nombre debe tener al menos 3 caracteres.")
            
        return nombre.upper() # Opcional: convertir a mayúsculas
    

class MensualidadForm(forms.ModelForm):
    # Opcional: Personalizar el campo 'periodo_cubierto' 
    # para usar un selector de fecha más amigable (widget)
    periodo_cubierto = forms.DateField(
        label='Mes/Periodo Cubierto',
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        # Ayuda al usuario a entender que solo importa el mes y año
        help_text='Selecciona el primer día del mes que se está pagando (ej: 01/10/2025).'
    )
    
    class Meta:
        model = Mensualidad
        
        # Campos que se mostrarán y pedirán al usuario
        fields = [
            'id_atleta', 
            'periodo_cubierto', 
            'monto_base', 
            'total_pagado',
            'estado_pago',
            'observ_men', 
            'comprobante'
        ]
        
        # Widgets para aplicar clases de estilo de AdminLTE/Bootstrap
        widgets = {
            'id_atleta': forms.Select(attrs={'class': 'form-control select2'}), # select2 es común en AdminLTE
            'monto_base': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'total_pagado': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'estado_pago': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'observ_men': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            # 'comprobante' usa el widget FileInput por defecto
        }
        
        # Campos a excluir automáticamente y que se manejan en la vista/lógica:
        # - id_mensualidad (AutoField)
        # - fecha_pago (default=timezone.now)
        # - recibo_emitido (default=False)