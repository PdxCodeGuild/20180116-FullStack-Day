


from django.urls import path
# from django.conf.urls import handler400, handler403, handler404, handler500
#
# handler400 = 'my_app.views.bad_request'
# handler403 = 'my_app.views.permission_denied'
# handler404 = 'my_app.views.page_not_found'
# handler500 = 'my_app.views.server_error'

from . import views

app_name = 'notesapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:note_id>/', views.detail, name='detail'),
    path('savenote/', views.savenote, name='savenote'),
    path('createnotepage/', views.create_note_page, name='createnotepage'),
    path('createnote/', views.createnote, name='createnote')
]

