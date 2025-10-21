from django.db import models
from django.utils import timezone
from datetime import date
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class atleta(models.Model):
    
    OPCIONES_SEXO = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    ]
    
    id_atleta = models.AutoField(primary_key=True)
    ci_atleta = models.CharField(max_length=15, unique=True, blank=True, null=True)
    nom_atleta = models.CharField(max_length=20)
    apell_atleta = models.CharField(max_length=20)
    sexo = models.CharField(max_length=1, choices=OPCIONES_SEXO, default='M')
    fecha_nac = models.DateField()
    altura = models.FloatField(max_length=3)
    peso = models.FloatField(max_length=5)
    talla = models.FloatField(max_length=3)
    envergadura = models.FloatField(max_length=3)
    telf_atleta = models.CharField(max_length=11)
    condicion = models.TextField(null=True, blank=True)
    observacion = models.TextField(null=True, blank=True)
    foto = models.ImageField(upload_to='fotos_atletas/', blank=True, null=True)
    
    def _str_(self):
        return self.id_atleta
    
    def calcular_edad(self):
        hoy = date.today()
        edad = hoy.year - self.fecha_nac.year
        if (hoy.month, hoy.day) < (self.fecha_nac.month, self.fecha_nac.day):
            edad -= 1
        return edad
    
    
class Representante(models.Model):
    
    OPCIONES_SEXO = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    ]
    
    ci_repre = models.CharField(max_length=15, unique=True)
    nom_repre = models.CharField(max_length=20)
    apell_repre = models.CharField(max_length=20)
    telf_repre = models.CharField(max_length=11)
    direccion = models.TextField()
    correo = models.EmailField(unique=True, null=True, blank=True)
    sexo_repre = models.CharField(max_length=1, choices=OPCIONES_SEXO, default='M')
    parentesto = models.TextField(null=True, blank=True)
    
    
class entrenador(models.Model):
    
    OPCIONES_SEXO = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    ]
    
    ci_entrenador = models.BigIntegerField(primary_key=True, validators=[MaxValueValidator(99999999999), MinValueValidator(0)])
    nom_entre = models.CharField(max_length=20)
    apell_entre = models.CharField(max_length=20)
    telf_entre = models.IntegerField(validators=[MaxValueValidator(99999999999), MinValueValidator(0)])
    correo_entre = models.EmailField(unique=True, null=True, blank=True)
    sexo_entre = models.CharField(max_length=1, choices=OPCIONES_SEXO, default='M')
    
    
class asistencia(models.Model):
    id_asistencia = models.AutoField(primary_key=True)
    id_atleta = models.ForeignKey(atleta, on_delete=models.CASCADE, related_name='asistencia_atleta')
    fecha_asis = models.DateField()
    estado = models.BooleanField(default=True)
    
        
class entre_asis(models.Model):
    id_asistencia = models.ForeignKey(asistencia, on_delete=models.CASCADE,related_name='registros_entrenamiento',verbose_name='Registro de Asistencia')
    ci_entrenador = models.ForeignKey(entrenador, on_delete=models.CASCADE, related_name='registros_supervisados')
    
    class meta:
        unique_together = ['id_asistencia', 'ci_entrenador'] 
        
        
class categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    id_atleta = models.ForeignKey(atleta, on_delete=models.SET_NULL, related_name='categoria_atleta', null=True, blank=True)
    nom_categoria = models.CharField(max_length=20, unique=True)
    detalle_cat = models.TextField(null=True, blank=True)
    

class horario(models.Model):
    id_hor = models.AutoField(primary_key=True)
    id_categoria = models.ForeignKey(categoria, on_delete=models.CASCADE, related_name='horarios_categoria',)
    hora_inicio = models.TimeField()
    hora_salida = models.TimeField()
    observ_hora = models.TextField(null=True, blank=True)
    
    
class requisitos(models.Model):
    id_req = models.AutoField(primary_key=True)
    id_atleta = models.ForeignKey(atleta, on_delete=models.CASCADE, related_name='requisitos_atleta')
    nom_req = models.CharField(max_length=20, unique=True)
    desq_req = models.TextField(null=True, blank=True)
    det_req = models.TextField(null=True, blank=True)
    
    
class inscripcion(models.Model):
    id_inscripcion = models.AutoField(primary_key=True)
    id_atleta = models.ForeignKey(atleta, on_delete=models.CASCADE,related_name='inscripciones_atleta')
    fecha_insc = models.DateField()
    deta_insc = models.TextField(blank=True, null=True)
    
    
class pruebas(models.Model):
    UNIDAD_CHOICES = [
    ('MTS', 'Metros'),
    ('SEG', 'Segundos'),
    ('PTS', 'Puntos'),
    ('KIL', 'Kilogramos'),
]
    id_prueba = models.AutoField(primary_key=True)
    id_atleta =models.ForeignKey(atleta, on_delete=models.CASCADE,related_name='atleta_evaluado')
    ci_entrenador = models.ForeignKey(entrenador, on_delete=models.CASCADE, related_name='entrenador_asignado')
    lugar = models.TextField(blank=True, null=True)
    nom_prue = models.CharField(max_length=50)
    desc_prue = models.TextField(blank=True, null=True)
    unidad_medida = models.CharField(max_length=3,choices=UNIDAD_CHOICES, default='PTS')
    fecha_prue = models.DateField()
    observ_prue =models.TextField(blank=True, null=True)
    
    
class insc_atle_repre(models.Model): # ⚠️ CORRECCIÓN: Ahora hereda de models.Model
    id_inscripcion = models.ForeignKey(inscripcion, on_delete=models.CASCADE,related_name='inscripciones_dato')
    ci_repre = models.ForeignKey(Representante, on_delete=models.CASCADE,related_name='representante_del_atleta')
    id_atleta =models.ForeignKey(atleta, on_delete=models.CASCADE,related_name='atleta_inscrito')
    
    
class result_prue(models.Model):
    id_resultado = models.AutoField(primary_key=True)
    id_atleta =models.ForeignKey(atleta, on_delete=models.CASCADE,related_name='atleta_resultado')
    fuerza = models.DecimalField(max_digits=3,decimal_places=2)
    resistencia = models.DecimalField(max_digits=3,decimal_places=2)
    puntaje = models.DecimalField(max_digits=3,decimal_places=2)
    
    
class mensualidad(models.Model):
    id_mensualidad = models.AutoField(primary_key=True)
    id_atleta =models.ForeignKey(atleta, on_delete=models.CASCADE,related_name='atleta_mensualidad')
    fecha_men = models.DateField(default=timezone.now)
    monto = models.DecimalField(max_digits=3,decimal_places=2)
    estado_pago = models.BooleanField(default=True)
    total = models.DecimalField(max_digits=3,decimal_places=2)
    observ_men = models.TextField(blank=True,null=True)
    comprobante = models.ImageField(upload_to='comprobantes/', blank=True, null=True)