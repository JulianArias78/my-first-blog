# -*- coding:utf-8 -*-
import os, sys, django
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from SI_FTPP.forms import addRegisterForms, addPerfilForms
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.core.mail import EmailMessage
from django.core.urlresolvers import reverse
from SI_FTPP.models import RegisterGuardianship, Profile
from django.contrib.auth.models import User
from django.db.models import Q

def login_page(request):
    print "login_page"
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('home'))

    data={}
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        print username, password
        user = authenticate(username=username, password=password)
        print user
        if user is not None:
            if user.is_active:
                print(login(request, user))
                data['success']="login correcto"
                print "success",data
                return HttpResponseRedirect(reverse('home'))
            else:
                data['error']="el usuario no esta activo"
                print "error",data
        else:
            data['error']="No es posible acceder a la plataforma, usuario o contraseña incorrectos. Si persiste el error, póngase en contacto con el administrador"
            print "error",data
    return render(request, "login.html", data)

@login_required(login_url='/')
def logout_page(request):
    print "logout"
    logout(request)
    return HttpResponseRedirect(reverse('home'))

#@login_required(login_url='/')
def home(request):
    return render(request, "home.html", {})


def addRegister (request):
    if request.user.profile.role == "END":
        return HttpResponseRedirect('/')
    message_success = None
    message_error = None
    form = addRegisterForms()
    if request.user.is_authenticated():
        if request.method == "POST":
            form = addRegisterForms(request.POST)
            if form.is_valid():
                id_register_guardianship = form.cleaned_data['id_register_guardianship']

                date_of_the_decision_of_guardianship = form.cleaned_data['date_of_the_decision_of_guardianship']
                
                concerning = form.cleaned_data['concerning']

                gender = form.cleaned_data['gender']
                
                ethnic_group = form.cleaned_data['ethnic_group']
                
                condition = form.cleaned_data['condition']
                
                in_respresentation = form.cleaned_data['in_respresentation']
                
                public = form.cleaned_data['public']
                private = form.cleaned_data['private']
                pension = form.cleaned_data['pension']
                epm = form.cleaned_data['epm']
                epn = form.cleaned_data['epn']
                
                regime = form.cleaned_data['regime']

                which_entity = form.cleaned_data['which_entity']

                asmet_salud = form.cleaned_data['asmet_salud']
                cafe_salud = form.cleaned_data['cafe_salud']
                sos = form.cleaned_data['sos']
                salud_total = form.cleaned_data['salud_total']
                nueva_eps = form.cleaned_data['nueva_eps']
                pijaos_salud = form.cleaned_data['pijaos_salud']
                sura = form.cleaned_data['sura']
                coomeva = form.cleaned_data['coomeva']
                cosmitet = form.cleaned_data['cosmitet']
                other_eps = form.cleaned_data['other_eps']

                personal_integrity = form.cleaned_data['personal_integrity']
                life = form.cleaned_data['life']
                human_dignity = form.cleaned_data['human_dignity']
                health = form.cleaned_data['health']
                social_security = form.cleaned_data['social_security']
                right_of_petition = form.cleaned_data['right_of_petition']
                due_process = form.cleaned_data['due_process']
                vital_minimum = form.cleaned_data['vital_minimum']
                work = form.cleaned_data['work']
                equality = form.cleaned_data['equality']
                privacy = form.cleaned_data['privacy']
                free_personality_development = form.cleaned_data['free_personality_development']
                healthy_environment = form.cleaned_data['healthy_environment']
                habeas_data = form.cleaned_data['habeas_data']
                good_name = form.cleaned_data['good_name']
                education = form.cleaned_data['education']
                freedom_of_Worship = form.cleaned_data['freedom_of_Worship']
                freedom_of_expression = form.cleaned_data['freedom_of_expression']
                other_right = form.cleaned_data['other_right']

                medicament = form.cleaned_data['medicament']
                process = form.cleaned_data['process']
                timely_medical_appointment = form.cleaned_data['timely_medical_appointment']
                specialized_appointment = form.cleaned_data['specialized_appointment']
                transfers_and_travel_expenses = form.cleaned_data['transfers_and_travel_expenses']
                prosthesis = form.cleaned_data['prosthesis']
                disability_payment = form.cleaned_data['disability_payment']
                supplies = form.cleaned_data['supplies']
                another_negation = form.cleaned_data['another_negation']

                grant = form.cleaned_data['grant']
                improper_for = form.cleaned_data['improper_for']
                fraud_court_decision = form.cleaned_data['fraud_court_decision']
                                
                fosyga = form.cleaned_data['fosyga']
                fomag = form.cleaned_data['fomag']
                health_secretary = form.cleaned_data['health_secretary']

                #Auxiliar_de_registro = form.cleaned_data['Auxiliar_de_registro']

                r = RegisterGuardianship()
                r.id_register_guardianship = id_register_guardianship
    
                r.date_of_the_decision_of_guardianship = date_of_the_decision_of_guardianship

                r.concerning = concerning

                r.gender = gender

                r.ethnic_group = ethnic_group

                r.condition = condition

                r.in_respresentation = in_respresentation

                r.public = public
                r.private = private
                r.pension = pension
                r.epm = epm
                r.epn = epn
                r.regime = regime
                r.which_entity = which_entity

                r.asmet_salud = asmet_salud
                r.cafe_salud = cafe_salud
                r.sos = sos
                r.salud_total = salud_total
                r.nueva_eps = nueva_eps
                r.pijaos_salud = pijaos_salud
                r.sura = sura
                r.coomeva = coomeva
                r.cosmitet = cosmitet 
                r.other_eps = other_eps

                r.personal_integrity = personal_integrity
                r.life = life
                r.human_dignity = human_dignity
                r.health = health
                r.social_security = social_security
                r.right_of_petition = right_of_petition
                r.due_process = due_process
                r.vital_minimum = vital_minimum
                r.work = work
                r.equality = equality
                r.privacy = privacy
                r.free_personality_development = free_personality_development
                r.healthy_environment = healthy_environment
                r.habeas_data = habeas_data
                r.good_name = good_name
                r.education = education
                r.freedom_of_Worship = freedom_of_Worship
                r.freedom_of_expression = freedom_of_expression
                r.other_right = other_right

                r.medicament = medicament
                r.process = process
                r.timely_medical_appointment = timely_medical_appointment
                r.specialized_appointment = specialized_appointment
                r.transfers_and_travel_expenses = transfers_and_travel_expenses
                r.prosthesis = prosthesis
                r.disability_payment = disability_payment
                r.supplies = supplies
                r.another_negation = another_negation

                r.grant = grant
                r.improper_for = improper_for
                r.fraud_court_decision = fraud_court_decision
                
                r.fosyga = fosyga
                r.fomag = fomag
                r.health_secretary = health_secretary

                r.author = request.user
                #r.Auxiliar_de_registro = request.user #funciona

                r.save()
                message_success = "La tutela se ha guardado satisfactoriamente."
                print message_success
            else:
                print form.errors
                print "formulario no es valido"
                message_error = form.errors
            form = addRegisterForms()
            return render(request,'register.html', {
                "form":form,
                "message_success": message_success,
                "message_error": message_error})
        else:
            form = addRegisterForms()
            ctx = {'form':form}
            return render(request,'register.html', ctx)
    else:
        return HttpResponseRedirect('/')

def about_view(request):
    return render(request, "about.html", {})

#arreglar
def restore_password(request):
    if request.POST:
        username = request.POST.get("username")
        document = request.POST.get("document_number")
        role = request.POST.get("role")
        from_email = request.POST.get("email")
        print username
        print document
        print role
        print from_email
        subject = 'Alguien solicito reestablecer la contraseña para la cuenta en SIFT'
        message = ("Hola, Admin!!!, éste usuario solicitó recientemente reestablecer la contraseña de SIFT.                                            "
            "Los siguientes son los datos ingresados en el formulario para su respectiva verificacion:                                      "
            "                                                                                                   "
            "Nombre de Usuario ingresado: {}                    Numero de documento ingresado: {}               Cargo ingresado: {}             Email ingresado: {}".format(username, document, role, from_email))
            
        mail = EmailMessage(subject, message, from_email, ['proyectopersoneriap@gmail.com'])#correo de destino
        mail.send()
        return redirect("restore_password_done")
    else:
        return render(request, "restore_password.html", {})

def restore_password_done(request):
    return render(request, "password_reset_done.html",{})

def create_user(request):
    if request.user.profile.role != "A":
        return HttpResponseRedirect('/')
    data = request.POST.dict()
    data.update({"is_active": False})
    form = addPerfilForms(request.POST)
    message_success = None
    message_error = None

    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data['username']
            document_type = form.cleaned_data['document_type']
            document_number = form.cleaned_data['document_number']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            password = form.cleaned_data['password']
            gender = form.cleaned_data['gender']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            role = form.cleaned_data['role']
            is_active = form.cleaned_data['is_active']

            new_user=User(
                username=username,
                first_name=first_name,
                last_name=last_name,
                email=email,
                is_active=is_active
            )

            new_user.save()
            new_user.set_password(password)
            new_user.save()

            new_user_profile=Profile(
                user=new_user,
                document_type=document_type,
                document_number=document_number,
                gender=gender,
                phone=phone,
                role=role
            )

            new_user_profile.save()

            message_success = ("El usuario ha sido registrado exitosamente.")
        else:
            message_error = form.errors

    return render(request, "create_user.html", {
        "form": form,
        "message_success": message_success,
        "message_error": message_error
    })

#arreglar
#@login_required(login_url="/")
def home_admin(request):
    if request.user.profile.role != "A":
        return HttpResponseRedirect('/')

    user_profile = User.objects.filter(
        is_active=True)
    return render(request, "home_admin.html",{})

def list_user(request):
    if request.user.profile.role != "A":
        return HttpResponseRedirect('/')

    user_profile = User.objects.filter(
        is_active=True)
    user_profile1 = Profile.objects.filter()

    data={
        "user_profile": user_profile, 
        "user_profile1": user_profile1
    }

    return render(request, "list_user.html",data)

def edit_user(request,id_user):
    if request.user.profile.role != "A":
        return HttpResponseRedirect('/')
    usuario=User.objects.get(id=id_user)
    profile = usuario.profile
    print usuario
    message_success = None
    message_error = None

    form = addPerfilForms(initial={
            "username":usuario.username,
            "document_type":usuario.profile.document_type,
            "document_number":usuario.profile.document_number,
            "first_name":usuario.first_name,
            "last_name":usuario.last_name,
            "password":usuario.password,
            "gender":usuario.profile.gender,
            "email":usuario.email,
            "phone":usuario.profile.phone,
            "role":usuario.profile.role,
            "is_active":usuario.is_active
            }
        )
    if request.method == "POST":
        form = addPerfilForms(request.POST)
        print "es post"
        if form.is_valid():
            print "el formulario es valido"
            username = form.cleaned_data['username']
            document_type = form.cleaned_data['document_type']
            document_number = form.cleaned_data['document_number']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            password = form.cleaned_data['password']
            gender = form.cleaned_data['gender']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            role = form.cleaned_data['role']
            is_active = form.cleaned_data['is_active']

            usuario.username = username
            profile.document_type = document_type
            profile.document_number = document_number
            usuario.first_name = first_name
            usuario.last_name = last_name
            usuario.password = password
            profile.gender = gender
            usuario.email = email
            profile.phone = phone
            profile.role = role
            usuario.is_active = is_active

            usuario.save()
            profile.save()
            message_success = ("El Usuario ha sido modificado satisfactoriamente.")
            print message_success
        else:
            print form.errors
            print "formilario no es valido"
            message_error = form.errors
    return render(request, "edit_user.html",{
        "form":form, 
        "usuario":usuario,
        "message_success": message_success,
        "message_error": message_error})

def delete_user(request,id_user):
    if request.user.profile.role != "A":
        return HttpResponseRedirect('/')
    usuario=User.objects.get(id=id_user)
    usuario.is_active = False
    usuario.save()
    print usuario

    return redirect("/listar_usuarios")

#@login_required(login_url="/")    
def home_aux(request):
    if request.user.profile.role != "AUX":
        return HttpResponseRedirect('/')

    user_profile = User.objects.filter(is_active=True)

    return render(request, "home_aux.html",{})

def list_register(request):
    if request.user.profile.role == "END":
        return HttpResponseRedirect('/')

    register_guardianship = RegisterGuardianship.objects.filter()

    return render(request, "list_register.html",{"register_guardianship": register_guardianship})

def edit_register(request,id_register):
    if request.user.profile.role != "A":
        return HttpResponseRedirect('/')
    register=RegisterGuardianship.objects.get(id=id_register)
#   profile = usuario.profile
    print register
    message_success = None
    message_error = None
    form = addRegisterForms(initial={
            "id_register_guardianship":register.id_register_guardianship,
            "date_of_the_decision_of_guardianship":register.date_of_the_decision_of_guardianship,
            "concerning":register.concerning,
            "gender":register.gender,
            "ethnic_group":register.ethnic_group,
            "condition":register.condition,
            "in_respresentation":register.in_respresentation,
            "public":register.public,
            "private":register.private,
            "epm":register.epm,
            "epn":register.epn,
            "regime":register.regime,
            "which_entity":register.which_entity,
            "asmet_salud":register.asmet_salud,
            "cafe_salud":register.cafe_salud,
            "sos":register.sos,
            "salud_total":register.salud_total,
            "nueva_eps":register.nueva_eps,
            "pijaos_salud":register.pijaos_salud,
            "sura":register.sura,
            "coomeva":register.coomeva,
            "cosmitet":register.cosmitet,
            "other_eps":register.other_eps,
            "personal_integrity":register.personal_integrity,
            "life":register.life,
            "human_dignity":register.human_dignity,
            "health":register.health,
            "social_security":register.social_security,
            "right_of_petition":register.right_of_petition,
            "due_process":register.due_process,
            "vital_minimum":register.vital_minimum,
            "work":register.work,
            "equality":register.equality,
            "privacy":register.privacy,
            "free_personality_development":register.free_personality_development,
            "healthy_environment":register.healthy_environment,
            "habeas_data":register.habeas_data,
            "good_name":register.good_name,
            "education":register.education,
            "freedom_of_Worship":register.freedom_of_Worship,
            "freedom_of_expression":register.freedom_of_expression,
            "other_right":register.other_right,
            "medicament":register.medicament,
            "process":register.process,
            "timely_medical_appointment":register.timely_medical_appointment,
            "specialized_appointment":register.specialized_appointment,
            "transfers_and_travel_expenses":register.transfers_and_travel_expenses,
            "prosthesis":register.prosthesis,
            "disability_payment":register.disability_payment,
            "supplies":register.supplies,
            "another_negation":register.another_negation,
            "grant":register.grant,
            "improper_for":register.improper_for,
            "fraud_court_decision":register.fraud_court_decision,
            "fosyga":register.fosyga,
            "fomag":register.fomag,
            "health_secretary":register.health_secretary
            }
        )
    if request.method == "POST":
        form = addRegisterForms(request.POST)
        print "es post"
        if form.is_valid():
            print "el formulario es valido"
            id_register_guardianship = form.cleaned_data['id_register_guardianship']

            date_of_the_decision_of_guardianship = form.cleaned_data['date_of_the_decision_of_guardianship']
            
            concerning = form.cleaned_data['concerning']

            gender = form.cleaned_data['gender']
            
            ethnic_group = form.cleaned_data['ethnic_group']
            
            condition = form.cleaned_data['condition']
            
            in_respresentation = form.cleaned_data['in_respresentation']
            
            public = form.cleaned_data['public']
            private = form.cleaned_data['private']
            pension = form.cleaned_data['pension']
            epm = form.cleaned_data['epm']
            epn = form.cleaned_data['epn']
            
            regime = form.cleaned_data['regime']

            which_entity = form.cleaned_data['which_entity']

            asmet_salud = form.cleaned_data['asmet_salud']
            cafe_salud = form.cleaned_data['cafe_salud']
            sos = form.cleaned_data['sos']
            salud_total = form.cleaned_data['salud_total']
            nueva_eps = form.cleaned_data['nueva_eps']
            pijaos_salud = form.cleaned_data['pijaos_salud']
            sura = form.cleaned_data['sura']
            coomeva = form.cleaned_data['coomeva']
            cosmitet = form.cleaned_data['cosmitet']
            other_eps = form.cleaned_data['other_eps']

            personal_integrity = form.cleaned_data['personal_integrity']
            life = form.cleaned_data['life']
            human_dignity = form.cleaned_data['human_dignity']
            health = form.cleaned_data['health']
            social_security = form.cleaned_data['social_security']
            right_of_petition = form.cleaned_data['right_of_petition']
            due_process = form.cleaned_data['due_process']
            vital_minimum = form.cleaned_data['vital_minimum']
            work = form.cleaned_data['work']
            equality = form.cleaned_data['equality']
            privacy = form.cleaned_data['privacy']
            free_personality_development = form.cleaned_data['free_personality_development']
            healthy_environment = form.cleaned_data['healthy_environment']
            habeas_data = form.cleaned_data['habeas_data']
            good_name = form.cleaned_data['good_name']
            education = form.cleaned_data['education']
            freedom_of_Worship = form.cleaned_data['freedom_of_Worship']
            freedom_of_expression = form.cleaned_data['freedom_of_expression']
            other_right = form.cleaned_data['other_right']

            medicament = form.cleaned_data['medicament']
            process = form.cleaned_data['process']
            timely_medical_appointment = form.cleaned_data['timely_medical_appointment']
            specialized_appointment = form.cleaned_data['specialized_appointment']
            transfers_and_travel_expenses = form.cleaned_data['transfers_and_travel_expenses']
            prosthesis = form.cleaned_data['prosthesis']
            disability_payment = form.cleaned_data['disability_payment']
            supplies = form.cleaned_data['supplies']
            another_negation = form.cleaned_data['another_negation']

            grant = form.cleaned_data['grant']
            improper_for = form.cleaned_data['improper_for']
            fraud_court_decision = form.cleaned_data['fraud_court_decision']
                            
            fosyga = form.cleaned_data['fosyga']
            fomag = form.cleaned_data['fomag']
            health_secretary = form.cleaned_data['health_secretary']

            register.id_register_guardianship = id_register_guardianship

            register.date_of_the_decision_of_guardianship = date_of_the_decision_of_guardianship

            register.concerning = concerning

            register.gender = gender

            register.ethnic_group = ethnic_group

            register.condition = condition

            register.in_respresentation = in_respresentation

            register.public = public
            register.private = private
            register.pension = pension
            register.epm = epm
            register.epn = epn
            register.regime = regime
            register.which_entity = which_entity

            register.asmet_salud = asmet_salud
            register.cafe_salud = cafe_salud
            register.sos = sos
            register.salud_total = salud_total
            register.nueva_eps = nueva_eps
            register.pijaos_salud = pijaos_salud
            register.sura = sura
            register.coomeva = coomeva
            register.cosmitet = cosmitet 
            register.other_eps = other_eps

            register.personal_integrity = personal_integrity
            register.life = life
            register.human_dignity = human_dignity
            register.health = health
            register.social_security = social_security
            register.right_of_petition = right_of_petition
            register.due_process = due_process
            register.vital_minimum = vital_minimum
            register.work = work
            register.equality = equality
            register.privacy = privacy
            register.free_personality_development = free_personality_development
            register.healthy_environment = healthy_environment
            register.habeas_data = habeas_data
            register.good_name = good_name
            register.education = education
            register.freedom_of_Worship = freedom_of_Worship
            register.freedom_of_expression = freedom_of_expression
            register.other_right = other_right

            register.medicament = medicament
            register.process = process
            register.timely_medical_appointment = timely_medical_appointment
            register.specialized_appointment = specialized_appointment
            register.transfers_and_travel_expenses = transfers_and_travel_expenses
            register.prosthesis = prosthesis
            register.disability_payment = disability_payment
            register.supplies = supplies
            register.another_negation = another_negation

            register.grant = grant
            register.improper_for = improper_for
            register.fraud_court_decision = fraud_court_decision
            
            register.fosyga = fosyga
            register.fomag = fomag
            register.health_secretary = health_secretary

            register.save()
            message_success = "El Registro de Tutela ha sido modificado satisfactoriamente."
            print message_success
        else:
            print form.errors
            print "formulario no es valido"
            message_error = form.errors
    return render(request, "edit_register.html",{
        "form":form, 
        "register":register,
        "message_success": message_success,
        "message_error": message_error})

# def delete_register(request,id_register):
#     registerGuar=RegisterGuardianship.objects.get(id=id_register)
#   #usuario=User.objects.get(id=id_register)
#   usuario.is_active = False
#   usuario.save()
#   print usuario

#   return redirect("/listar_tutela")

#@login_required(login_url="/")    
def home_end(request):
    if request.user.profile.role != "END":
        return HttpResponseRedirect('/')

    user_profile = User.objects.filter(
        is_active=True)

    return render(request, "home_end.html",{})

#@login_required(login_url="/")    
def admin_site(request):
    if request.user.profile.role != "A":
        return HttpResponseRedirect('/')
    return render(request, "base_admin.html",{})

#@login_required(login_url="/")    
def help_site(request):
    if request.user.profile.role == "END":
        return HttpResponseRedirect('/')
    return render(request, "help.html",{})
    
#@login_required(login_url="/")    
def check_failure(request):
    if request.user.profile.role == "AUX":
        return HttpResponseRedirect('/')

#   if request.user.profile.role == "AUX":
#       return HttpResponseRedirect('/')
    if request.POST:
        date = request.POST.get("fecha")
        print date

    #return render(request, "googlecharts_configuration.htm",data)

        return redirect("check_failure")
    else:
        return render(request, "check_failure.html",{})
    #return render(request, "check_failure.html",{})

def google_chart(request):
#   if request.user.profile.role == "AUX":
#       return HttpResponseRedirect('/')
    ethnic_group_1=RegisterGuardianship.objects.filter(ethnic_group='1')
    numet1 = 0
    for item in ethnic_group_1:
        numet1 = numet1 +1
    print numet1
    ethnic_group_2=RegisterGuardianship.objects.filter(ethnic_group='2')
    numet2 = 0
    for item in ethnic_group_2:
        numet2 =numet2 +1
    print numet2
    ethnic_group_3=RegisterGuardianship.objects.filter(ethnic_group='3')
    numet3 = 0
    for item in ethnic_group_3:
        numet3 = numet3 +1
    print numet3
    ethnic_group_4=RegisterGuardianship.objects.filter(ethnic_group='4')
    numet4 = 0
    for item in ethnic_group_4:
        numet4 = numet4 +1
    print numet4

    register_guardianship_1=RegisterGuardianship.objects.filter(gender='M')
    num1 = 0
    for item in register_guardianship_1:
        num1 = num1 +1
    print num1
    register_guardianship_2=RegisterGuardianship.objects.filter(gender='F')
    num2 = 0
    for item in register_guardianship_2:
        num2 = num2 +1
    print num2
    register_guardianship_3=RegisterGuardianship.objects.filter(gender='LGTBI')
    num3 = 0
    for item in register_guardianship_3:
        num3 = num3 +1
    print num3


    condition_1=RegisterGuardianship.objects.filter(condition='1')
    cond1 = 0
    for item in condition_1:
        cond1 = cond1 +1
    print cond1
    condition_2=RegisterGuardianship.objects.filter(condition='2')
    cond2 = 0
    for item in condition_2:
        cond2 =cond2 +1
    print cond2
    condition_3=RegisterGuardianship.objects.filter(condition='3')
    cond3 = 0
    for item in condition_3:
        cond3 = cond3 +1
    print cond3
    condition_4=RegisterGuardianship.objects.filter(condition='4')
    cond4 = 0
    for item in condition_4:
       cond4 = cond4 +1
    print cond4

    condition_5=RegisterGuardianship.objects.filter(condition='5')
    cond5 = 0
    for item in condition_5:
       cond5 =cond5 +1
    print cond5


    regime_1=RegisterGuardianship.objects.filter(regime='1')
    reg1 = 0
    for item in regime_1:
        reg1 = reg1 +1
    print reg1

    regime_2=RegisterGuardianship.objects.filter(regime='2')
    reg2 = 0
    for item in regime_2:
        reg2 =reg2 +1
    print reg2


    entidad_1=RegisterGuardianship.objects.filter(public=True)
    ent1 = 0
    for item in entidad_1:
        ent1 = ent1 +1
    print ent1

    entidad_2=RegisterGuardianship.objects.filter(private=True)
    ent2 = 0
    for item in entidad_2:
        ent2 =ent2 +1
    print ent2


    eps_1=RegisterGuardianship.objects.filter(asmet_salud=True)
    eps1 = 0
    for item in eps_1:
        eps1 = eps1 +1
    print eps1

    eps_2=RegisterGuardianship.objects.filter(cosmitet=True)
    eps2 = 0
    for item in eps_2:
        eps2 = eps2 +1
    print eps2

    eps_3=RegisterGuardianship.objects.filter(cafe_salud=True)
    eps3 = 0
    for item in eps_3:
        eps3 =eps3 +1
    print eps3

    eps_4=RegisterGuardianship.objects.filter(sos=True)
    eps4 = 0
    for item in eps_4:
        eps4 = eps4 +1
    print eps4

    eps_5=RegisterGuardianship.objects.filter(salud_total=True)
    eps5 = 0
    for item in eps_5:
        eps5 =eps5 +1
    print eps5

    eps_6=RegisterGuardianship.objects.filter(nueva_eps=True)
    eps6 = 0
    for item in eps_6:
        eps6 = eps6 +1
    print eps6

    eps_7=RegisterGuardianship.objects.filter(pijaos_salud=True)
    eps7 = 0
    for item in eps_7:
        eps7 =eps7 +1
    print eps7

    eps_8=RegisterGuardianship.objects.filter(sura=True)
    eps8 = 0
    for item in eps_8:
        eps8 = eps8 +1
    print eps8

    eps_9=RegisterGuardianship.objects.filter(coomeva=True)
    eps9 = 0
    for item in eps_9:
        eps9 =eps9 +1
    print eps9


    data={
    "register_guardianship_1": register_guardianship_1, 
    "register_guardianship_2": register_guardianship_2,
    "register_guardianship_3": register_guardianship_3,
    "numet1": numet1, 
    "numet2": numet2,
    "numet3": numet3,
    "numet4": numet4,
    "num1": num1, 
    "num2": num2,
    "num3": num3,
    "cond1": cond1, 
    "cond2": cond2,
    "cond3": cond3,
    "cond4": cond4,
    "cond5": cond5,
    "reg1": reg1, 
    "reg2": reg2,
    "ent1": ent1, 
    "ent2": ent2,
    "eps1": eps1, 
    "eps2": eps2,
    "eps3": eps3, 
    "eps4": eps4,
    "eps5": eps5, 
    "eps6": eps6,
    "eps7": eps7, 
    "eps8": eps8,
    "eps9": eps9
    }

#return render(request, "googlecharts_configuration.htm",data)
    return render(request, "googlecharts_configuration.htm", data)

