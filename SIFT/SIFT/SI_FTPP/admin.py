from django.contrib import admin

from .models import Profile, RegisterGuardianship

class ProfileAdmin(admin.ModelAdmin):
    # fields = (
    #     )
    model = Profile

    list_display = (
        'user',
        'get_name',
        'document_number',
        'gender',
        'phone',
        'role'
    )

    def get_name(self, obj):
        return obj.user.first_name+" "+obj.user.last_name
    get_name.admin_order_field = 'user'  
    get_name.short_description = 'Name'  

admin.site.register(Profile, ProfileAdmin)

class RegisterGuardianshipAdmin(admin.ModelAdmin):
    model = RegisterGuardianship

    list_display = (
        'id_register_guardianship',
        'date_of_the_decision_of_guardianship',
        'concerning',
        'gender',
        'ethnic_group',
        'condition',
        'in_respresentation',
        'public',
        'private',
        'pension',
        'epm',
        'epn',
        'regime',
        'which_entity',
        'asmet_salud',
        'cafe_salud',
        'sos',
        'salud_total',
        'nueva_eps',
        'pijaos_salud',
        'sura',
        'coomeva',
        'cosmitet',
        'other_eps',
        'personal_integrity',
        'life',
        'human_dignity',
        'health',
        'social_security',
        'right_of_petition',
        'due_process',
        'vital_minimum',
        'work',
        'equality',
        'privacy',
        'free_personality_development',
        'healthy_environment',
        'habeas_data',
        'good_name',
        'education',
        'freedom_of_Worship',
        'freedom_of_expression',
        'other_right',
        'medicament',
        'process',
        'timely_medical_appointment',
        'specialized_appointment',
        'transfers_and_travel_expenses',
        'prosthesis',
        'disability_payment',
        'supplies',
        'another_negation',
        'grant',
        'improper_for',
        'fraud_court_decision',
        'fosyga',
        'fomag',
        'health_secretary',
        'timestamp'
    )

admin.site.register(RegisterGuardianship, RegisterGuardianshipAdmin)