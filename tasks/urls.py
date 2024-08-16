from django.urls import path
from.import views

from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('tasks/', views.tasks, name='tasks'),
    path('tasks_completed/', views.tasks_completed, name='tasks_completed'),
    path('logout/', views.signout, name='logout'),
    path('signin/', views.signin, name='signin'),
    path('create_task/', views.create_task, name='create_task'),
    path('tasks/<int:task_id>', views.task_detail, name='task_detail'),
    path('taks/<int:task_id>/complete', views.complete_task, name='complete_task'),
    path('tasks/<int:task_id>/delete', views.delete_task, name='delete_task'),
    path('facturas/', views.factura, name='facturas'),
    path('factura_crear/', views.crear, name='factura_crear'),
    path('factura_editar/<int:id>', views.editar, name='editar'),
    path('factura_eliminar/<int:id>', views.eliminar, name='eliminar'),
    path('factura_detalle/', views.detalle_factura, name='factura_detalle'),
    path('factura_detalle_crear/', views.detalle_factura_crear, name='factura_detalle_crear'),
    path('factura_detalle_editar/<int:id>', views.detalle_factura_editar, name='factura_detalle_editar'),
    path('factura_detalle_eliminar/<int:id>', views.detalle_factura_eliminar, name='factura_detalle_eliminar'),
    path('pago_consulta/', views.pago_consulta, name='pago_consulta'),
    path('pago_insertar/', views.pago_insertar, name='pago_insertar'),
    path('pago_editar/<int:id>', views.pago_actualizar, name='pago_editar'),
    path('pago_eliminar/<int:id>', views.pago_eliminar, name='pago_eliminar'),
    path('carrito_detalle/', views.carrito_detalle, name='carrito_detalle'),
    path('carrito_insertar/', views.carrito_insertar, name='carrito_insertar'),
    path('carrito_editar/<int:id>', views.carrito_actualizar, name='carrito_editar'),
    path('carrito_eliminar/<int:id>', views.carrito_eliminar, name='carrito_eliminar'),
]
