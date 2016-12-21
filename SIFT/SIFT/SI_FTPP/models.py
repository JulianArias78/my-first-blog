# -*- coding:utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    CODE_CHOICES = (('TI','Tarjeta de identidad'), ('CC','Cedula de ciudadanía'), ("CE", "Cedula de Extranjería"), ("NIT", "NIT"), ("Pst", "Pasaporte"), ("CD", "Carnet Dipomático"))
    GENDER_CHOICES = (('M','Masculino'), ('F','Femenino'), ('O','LGTBI'))
    ROLE_OPTIONS = (("A", "Administrador"),("AUX", "Auxiliar"), ("END", "Consultor"))

    user = models.OneToOneField(User, verbose_name="Usuario")
    document_type = models.CharField(max_length=20, choices = CODE_CHOICES, default='CC', verbose_name="Tipo de documento", blank=False, null=False)
    document_number = models.CharField(max_length = 30, verbose_name="Número de Identificación", blank=False, null=False)
    gender = models.CharField(max_length=10, choices = GENDER_CHOICES, default='M', verbose_name="Género", blank=False, null=False)
    phone = models.CharField(max_length=30, verbose_name="Teléfono", blank=False, null=False)
    role = models.CharField(max_length=15, choices = ROLE_OPTIONS, default='AUX', verbose_name="Cargo", blank=False, null=False)

    #is_active = models.BooleanField(default=False, blank=False)
    created = models.DateTimeField(default=timezone.now)
    modified = models.DateTimeField(auto_now = True)

    def __unicode__(self):
        return "%s"%(self.user)


class RegisterGuardianship(models.Model):
	GENDER_CHOICES = (('M','Masculino'), ('F','Femenino'), ('O','LGTBI'))
	ETHNICGROUP_CHOICES = ( ('1','Mestizo - Blanco'), ('2','Afro'),('3','Rom'),('4','Indigena'))
	CONDITION_CHOICES = ( ('1','Víctima'), ('2','Discapacidad'),('3','Menor'),('4','Adulto Mayor'),('5','Habitante de calle'))
	REPRESENTATION_CHOICES = ( ('1','Adulto Mayor'), ('2','Menor de edad'),('3','En Nombre Propio'),('4','Mediante Apoderado'),('5','Agente Oficioso'))
	REGIME_CHOICES = ( ('1','Subsidiado'), ('2','Contributivo'))
	GRANT_CHOICES = ( ('1','Si'), ('2','No'))
	IMPROPER_CHOICES = ( ('1','Hecho superado'), ('2',u'Daño consumado'), ('3','Existe otro medio de defensa'), ('4','Otro'))

	#Datos Tutela
	author = models.ForeignKey(User, verbose_name="Autor", null=False, blank=True)
	id_register_guardianship = models.CharField(max_length=20, verbose_name="Radicado", blank=False,null=False)

	date_of_the_decision_of_guardianship = models.DateField(verbose_name="Fecha del Fallo", null=False, blank=False)

	concerning = models.CharField(max_length=25, verbose_name="Accionante", blank=False,null=False)

	gender = models.CharField(max_length=10, choices = GENDER_CHOICES, default='M', verbose_name="Género", blank=False, null=False)

	ethnic_group = models.CharField(max_length=25, verbose_name="Etnia", choices=ETHNICGROUP_CHOICES, default='1', null=False, blank=False)

	condition = models.CharField(max_length=25, verbose_name="Condición", choices=CONDITION_CHOICES, default='1', null=False, blank=False)
	#En representacion

	in_respresentation = models.CharField(max_length=20, choices = REPRESENTATION_CHOICES, default='1', blank=False, null=False)
	
	#Entidad Accionada
	public = models.BooleanField(verbose_name="Pública",default=False)
	private = models.BooleanField(verbose_name="Privada",default=False)
	pension = models.CharField(max_length=40, verbose_name="Pensión", blank=True, null=True)
	epm = models.BooleanField(verbose_name="EPM",default=False)
	epn = models.BooleanField(verbose_name="EPN",default=False)
	regime = models.CharField(max_length=15, choices=REGIME_CHOICES,  default='1', verbose_name="Régimen", blank=False, null=False)
	which_entity = models.CharField(max_length=50, verbose_name="Cuál Entidad?", blank=True, null=True)
	
	asmet_salud = models.BooleanField( default=False)
	cafe_salud = models.BooleanField( default=False)
	sos= models.BooleanField( default=False)
	salud_total = models.BooleanField( default=False)
	nueva_eps = models.BooleanField( default=False)
	pijaos_salud = models.BooleanField( default=False)
	sura = models.BooleanField( default=False)
	coomeva = models.BooleanField( default=False)
	cosmitet = models.BooleanField( default=False)
	other_eps = models.CharField(max_length=40,verbose_name="Otra Eps", blank=True,null=True)

	#Derecho Vulnerado
	personal_integrity = models.BooleanField(verbose_name="Integridad Personal", default=False)
	life = models.BooleanField(verbose_name="Vida", default=False)
	human_dignity = models.BooleanField(verbose_name="Dignidad Humana", default=False)
	health = models.BooleanField(verbose_name="Salud", default=False)
	social_security = models.BooleanField(verbose_name="Seguridad Social", default=False)
	right_of_petition = models.BooleanField(verbose_name="DErecho de Petición", default=False)
	due_process = models.BooleanField(verbose_name="Debido Proceso", default=False)
	vital_minimum = models.BooleanField(verbose_name="Mínimo Vital", default=False)
	work = models.BooleanField(verbose_name="Trabajo", default=False)
	equality = models.BooleanField(verbose_name="Igualdad", default=False)
	privacy = models.BooleanField(verbose_name="Intimidad", default=False)
	free_personality_development = models.BooleanField(verbose_name="Libre Desarrollo de la Personalidad", default=False)
	healthy_environment = models.BooleanField(verbose_name="Hambiente Sano", default=False)
	habeas_data = models.BooleanField(verbose_name="Habeas Data", default=False)
	good_name = models.BooleanField(verbose_name="Buen Nombre", default=False)
	education = models.BooleanField(verbose_name="Educación", default=False)
	freedom_of_Worship = models.BooleanField(verbose_name="Libertad de Culto", default=False)
	freedom_of_expression = models.BooleanField(verbose_name="Libertad de Expresión", default=False)
	other_right = models.CharField(max_length=40,verbose_name="Cuál Derecho?", blank=True,null=True)

	#Relacion al fallo
	medicament = models.BooleanField(verbose_name="Medicamento", default=False)
	process = models.BooleanField(verbose_name="Procedimiento", default=False)
	timely_medical_appointment = models.BooleanField(verbose_name="Cita Médica Oportuna", default=False)
	specialized_appointment = models.BooleanField(verbose_name="Cita Especializada", default=False)
	transfers_and_travel_expenses = models.BooleanField(verbose_name="Traslados y Viáticos", default=False)
	prosthesis = models.BooleanField(verbose_name="Protesis", default=False)
	disability_payment = models.BooleanField(verbose_name="Pago Incapacidad", default=False)
	supplies = models.BooleanField( verbose_name="Insumos",default=False)
	another_negation = models.CharField(max_length=30, verbose_name="Cuál Negación?", blank=True, null=True)

	grant = models.CharField(max_length=5, choices=GRANT_CHOICES, default='1', null=False, blank=False)
	improper_for = models.CharField(max_length=25, choices=IMPROPER_CHOICES,  verbose_name="Improcedente", default='1', null=False, blank=False)
	fraud_court_decision = models.BooleanField(verbose_name="Fraude a resolución judicial", default=False)

	fosyga = models.BooleanField( default=False)
	fomag = models.BooleanField( default=False)
	health_secretary = models.BooleanField(verbose_name="Secretaría de Salud", default=False)

	timestamp = models.DateTimeField(auto_now_add = True, auto_now= False)
	def __unicode__(self): #que es?
		return self.id_register_guardianship