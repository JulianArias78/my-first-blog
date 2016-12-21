#!/usr/bin/env python 
# -*- coding: utf-8 -*
from django import forms
from models import RegisterGuardianship,Profile


CODE_CHOICES = (('TI','Tarjeta de identidad'), ('CC','Cedula de ciudadanía'), ("CE", "Cedula de Extranjería"), ("NIT", "NIT"), ("Pst", "Pasaporte"), ("CD", "Carnet Dipomático"))
GENDER_CHOICES = (('M','Masculino'),('F','Femenino'),('LGTBI','LGTBI'))
ROLE_OPTIONS = (("A", "Administrador"),("AUX", "Auxiliar"), ("END", "Consultor"))
ETHNICGROUP_CHOICES = ( ('1','Mestizo - Blanco'), ('2','Afro'),('3','Rom'),('4','Indigena'))
CONDITION_CHOICES = ( ('1','Víctima'), ('2','Discapacidad'),('3','Menor'),('4','Adulto Mayor'),('5','Habitante de calle'))
REPRESENTATION_CHOICES = ( ('1','Adulto Mayor'), ('2','Menor de edad'),('3','En Nombre Propio'),('4','Mediante Apoderado'),('5','Agente Oficioso'))
REGIME_CHOICES = ( ('1','Subsidiado'), ('2','Contributivo'))
GRANT_CHOICES = ( ('1','Si'), ('2','No'))
IMPROPER_CHOICES = ( ('1','Hecho superado'), ('2',u'Daño consumado'), ('3','Existe otro medio de defensa'), ('4','Otro'))

class addPerfilForms(forms.Form):
    
    #user = models.OneToOneField(User, verbose_name="Usuario")
    username = forms.CharField(required=True, label="Nombre de usuario", widget=forms.TextInput(attrs={"title": "Nombre de usuario"}))
    document_type = forms.ChoiceField(required=True, widget=forms.RadioSelect, choices=CODE_CHOICES)
    document_number = forms.CharField(required=True, label="Número de documento", widget=forms.TextInput(attrs={"size": 30, "title": "Número de documento"}))    
    first_name = forms.CharField(required=True, label="Nombres", widget=forms.TextInput(attrs={"size": 20, "title": "Nombres"}))
    last_name = forms.CharField(required=True, label="Apellidos", widget=forms.TextInput(attrs={"size": 20, "title": "Apellidos"}))
    password = forms.CharField(required=True, label="Contraseña", widget=forms.PasswordInput())
    gender = forms.ChoiceField(required=True, widget=forms.RadioSelect, choices=GENDER_CHOICES)
    email = forms.EmailField(required=True, label="Email", widget=forms.TextInput())
    phone = forms.CharField(required=True, label="Número de teléfono", widget=forms.TextInput(attrs={"size": 30, "title": "Número de teléfono"}))
    role = forms.ChoiceField(required=True, widget=forms.RadioSelect, choices=ROLE_OPTIONS)
    is_active = forms.BooleanField(required=False)

    #birthdate = forms.DateField(required=True, label="Fecha de nacimiento",input_formats=["%Y-%m-%d","%d/%m/%Y","%d/%m/%y"])    
    def clean(self):
    		return self.cleaned_data

    # def __init__(self, *args, **kwargs):
    #     super(addPerfilForms, self).__init__(*args, **kwargs)
    #     self.fields['username'].label = "Nombre de Usuario"
    #     self.fields['username'].widget.attrs['class'] = 'form-control'
    #     self.fields['document_type'].label = "Tipo de identificación"
    #     self.fields['document_type'].widget.attrs['class'] = 'form-control'
    #     self.fields['document_number'].label = "Número de identificación"
    #     self.fields['document_number'].widget.attrs['class'] = 'form-control'
    #     self.fields['first_name'].label = "Nombres"
    #     self.fields['first_name'].widget.attrs['class'] = 'form-control'
    #     self.fields['last_name'].label = "Apellidos"
    #     self.fields['last_name'].widget.attrs['class'] = 'form-control'
    #     self.fields['password'].label = "Contraseña"
    #     self.fields['password'].widget.attrs['class'] = 'form-control'
    #     self.fields['gender'].label = "Género"
    #     self.fields['gender'].widget.attrs['class'] = 'form-control'
    #     self.fields['email'].label = "Email"
    #     self.fields['email'].widget.attrs['class'] = 'form-control'
    #     self.fields['phone'].label = "Teléfono"
    #     self.fields['phone'].widget.attrs['class'] = 'form-control'
    #     self.fields['role'].label = "Cargo"
    #     self.fields['role'].widget.attrs['class'] = 'form-control'
    #     self.fields['is_active'].label = "Estado"
    #     self.fields['is_active'].widget.attrs['class'] = 'form-control'

class addRegisterForms(forms.Form):
	#id_register_guardianship = forms.CharField(widget=forms.TextInput())
	id_register_guardianship = forms.CharField(required=True, label="Número de radicado", widget=forms.TextInput(attrs={"size": 20, "title": "Número de radicado"}))
	
	DATEPICKER = {
        'type': 'text',
        'class': 'form-control',
        'id': 'datetimepicker4'
    }
    # Call attrs with form widget
	date_of_the_decision_of_guardianship = forms.DateField(required=True, widget=forms.DateInput(attrs=DATEPICKER))
	concerning = forms.CharField(required=True, widget= forms.TextInput(attrs={'size': 25, 'title': 'Accionante',}))
	gender = forms.ChoiceField(required=True,widget=forms.RadioSelect,choices=GENDER_CHOICES)
	ethnic_group = forms.ChoiceField(required=True, widget=forms.RadioSelect, choices=ETHNICGROUP_CHOICES)
	condition = forms.ChoiceField(widget=forms.RadioSelect, choices=CONDITION_CHOICES, required=True)

	in_respresentation = forms.ChoiceField(widget=forms.RadioSelect, choices=REPRESENTATION_CHOICES, required=True)

	public = forms.BooleanField( required=False)
	private = forms.BooleanField( required=False)
	pension = forms.CharField(required=False, widget= forms.TextInput(attrs={'size': 40, 'title': 'Pension',}))
	epm = forms.BooleanField( required=False)
	epn = forms.BooleanField( required=False)
	regime = forms.ChoiceField(widget=forms.Select, choices=REGIME_CHOICES, required=True)
	which_entity = forms.CharField(required=False, widget= forms.TextInput(attrs={'size': 50, 'title': 'Cuál Entidad?',}))

	asmet_salud = forms.BooleanField( required=False)
	cafe_salud = forms.BooleanField( required=False)
	sos = forms.BooleanField( required=False)
	salud_total = forms.BooleanField( required=False)
	nueva_eps = forms.BooleanField( required=False)
	pijaos_salud = forms.BooleanField( required=False)
	sura = forms.BooleanField( required=False)
	coomeva = forms.BooleanField( required=False)
	cosmitet = forms.BooleanField( required=False)
	other_eps = forms.CharField(required=False, widget= forms.TextInput(attrs={'size': 40, 'title': 'Otra EPS',}))

	personal_integrity = forms.BooleanField( required=False)
	life = forms.BooleanField( required=False)
	human_dignity = forms.BooleanField( required=False)
	health = forms.BooleanField( required=False)
	social_security = forms.BooleanField( required=False)
	right_of_petition = forms.BooleanField( required=False)
	due_process = forms.BooleanField( required=False)
	vital_minimum = forms.BooleanField( required=False)
	work = forms.BooleanField( required=False)
	equality = forms.BooleanField( required=False)
	privacy = forms.BooleanField( required=False)
	free_personality_development = forms.BooleanField( required=False)
	healthy_environment = forms.BooleanField( required=False)
	habeas_data = forms.BooleanField( required=False)
	good_name = forms.BooleanField( required=False)
	education = forms.BooleanField( required=False)
	freedom_of_Worship = forms.BooleanField( required=False)
	freedom_of_expression = forms.BooleanField( required=False)
	other_right = forms.CharField(required=False, widget= forms.TextInput(attrs={'size': 40, 'title': 'Cuál Derecho?',}))

	medicament = forms.BooleanField( required=False)
	process = forms.BooleanField( required=False)
	timely_medical_appointment = forms.BooleanField( required=False)
	specialized_appointment = forms.BooleanField( required=False)
	transfers_and_travel_expenses = forms.BooleanField( required=False)
	prosthesis = forms.BooleanField( required=False)
	disability_payment = forms.BooleanField( required=False)
	supplies = forms.BooleanField( required=False)
	another_negation = forms.CharField(required=False, widget= forms.TextInput(attrs={'size': 30, 'title': 'Cuál Negación?',}))

	grant = forms.ChoiceField(required=True,widget=forms.RadioSelect, choices=GRANT_CHOICES)
	improper_for = forms.ChoiceField(required=True,widget=forms.RadioSelect, choices=IMPROPER_CHOICES)
	fraud_court_decision = forms.BooleanField( required=False)

	fosyga = forms.BooleanField( required=False)
	fomag = forms.BooleanField( required=False)
	health_secretary = forms.BooleanField( required=False)

	#Auxiliar_de_registro = forms.ForeignKey(Auxiliar_de_registro)
	#Auxiliar_de_registro = forms.ModelMultipleChoiceField(queryset=Registar_tutela.objects.all(), widget=forms.HiddenInput()


	def clean(self):
			return self.cleaned_data

