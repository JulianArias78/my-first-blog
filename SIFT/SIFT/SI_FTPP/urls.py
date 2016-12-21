from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.home, name="home" ),
    url(r'^registro/$', views.addRegister, name="register"),
    url(r'^acerca/$', views.about_view, name="vista_about"),
    url(r'^inicio_sesion/$', views.login_page, name="login_page" ),
    url(r'^logout/$', views.logout_page, name="logout_page" ),
    url(r'^reestablecer/$', views.restore_password, name="restore_password" ),
    url(r'^reestablecer_aviso/$', views.restore_password_done, name="restore_password_done" ),
    url(r'^crear_usuario/', views.create_user, name="create_user" ),
    url(r"^perfil_admin/$", views.home_admin, name="home_admin"),
    url(r"^listar_usuarios/$", views.list_user, name="list_user"),
    url(r"^editar_usuario/(?P<id_user>[0-9]+)/$", views.edit_user, name="edit_user"),
    url(r"^eliminar_usuario/(?P<id_user>[0-9]+)/$", views.delete_user, name="delete_user"),
    url(r"^perfil_aux/$", views.home_aux, name="home_aux"),
    url(r"^listar_tutela/$", views.list_register, name="list_register"),
    url(r"^editar_tutela/(?P<id_register>[0-9]+)/$", views.edit_register, name="edit_register"),
    url(r"^perfil_end/$", views.home_end, name="home_end"),
    url(r"^admin_sitio/$", views.admin_site, name="admin_site"),
    url(r"^ayuda/$", views.help_site, name="help_site"),
    url(r"^consulta/$", views.check_failure, name="check_failure"),
    url(r"^graficos/$", views.google_chart, name="google_chart"),

]