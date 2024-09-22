from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .models import (
    Task,
    Factura,
    Detalle_Factura,
    Pago,
    Carrito,
    Pedido,
)
from .forms import (
    FacturaForm,
    FacturaDetalleForm,
    PagoDetalleForm,
    CarritoForm,
    PedidoForm,
)


from .forms import TaskForm

# Create your views here.


# ---------------------------------------------------------------------------------
# Home
# ---------------------------------------------------------------------------------


def home(request):
    return render(request, "home.html")


# ---------------------------------------------------------------------------------
# Registro
# ---------------------------------------------------------------------------------


def signup(request):
    if request.method == "GET":
        return render(request, "signup.html", {"formulario": UserCreationForm})
    else:

        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(
                    request.POST["username"], password=request.POST["password1"]
                )
                user.save()
                login(request, user)
                return redirect("tasks")
            except IntegrityError:
                return render(
                    request,
                    "signup.html",
                    {
                        "formulario": UserCreationForm,
                        "error": "Username already exists.",
                    },
                )

        return render(
            request,
            "signup.html",
            {"formulario": UserCreationForm, "error": "Passwords did not match."},
        )


# ---------------------------------------------------------------------------------
# Tareas
# ---------------------------------------------------------------------------------


@login_required
def tasks(request):
    tasks = Task.objects.filter(user=request.user, datecompleted__isnull=True)
    return render(request, "tasks.html", {"tasks": tasks})


@login_required
def tasks_completed(request):
    tasks = Task.objects.filter(
        user=request.user, datecompleted__isnull=False
    ).order_by("-datecompleted")
    return render(request, "tasks.html", {"tasks": tasks})


@login_required
def create_task(request):
    if request.method == "GET":
        return render(request, "create_task.html", {"formulario": TaskForm})
    else:
        try:
            formulario = TaskForm(request.POST)
            new_task = formulario.save(commit=False)
            new_task.user = request.user
            new_task.save()
            return redirect("tasks")
        except ValueError:
            return render(
                request,
                "create_task.html",
                {"formulario": TaskForm, "error": "Error creating task."},
            )


# ---------------------------------------------------------------------------------
# Login y Logout
# ---------------------------------------------------------------------------------


@login_required
def signout(request):
    logout(request)
    return redirect("home")


def signin(request):
    if request.method == "GET":
        return render(request, "signin.html", {"formulario": AuthenticationForm})
    else:
        user = authenticate(
            request,
            username=request.POST["username"],
            password=request.POST["password"],
        )
        if user is None:
            return render(
                request,
                "signin.html",
                {
                    "formulario": AuthenticationForm,
                    "error": "Username or password is incorrect.",
                },
            )

        login(request, user)
        return redirect("tasks")


# ---------------------------------------------------------------------------------
# Tarea Detalle
# ---------------------------------------------------------------------------------


@login_required
def task_detail(request, task_id):
    if request.method == "GET":
        task = get_object_or_404(Task, pk=task_id, user=request.user)
        formulario = TaskForm(instance=task)
        return render(
            request, "task_detail.html", {"task": task, "formulario": formulario}
        )
    else:
        try:
            task = get_object_or_404(Task, pk=task_id, user=request.user)
            formulario = TaskForm(request.POST, instance=task)
            formulario.save()
            return redirect("tasks")
        except ValueError:
            return render(
                request,
                "task_detail.html",
                {
                    "task": task,
                    "formulario": formulario,
                    "error": "Error updating task.",
                },
            )


@login_required
def complete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id, user=request.user)
    if request.method == "POST":
        task.datecompleted = timezone.now()
        task.save()
        return redirect("tasks")


@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id, user=request.user)
    if request.method == "POST":
        task.delete()
        return redirect("tasks")


# ---------------------------------------------------------------------------------
# Facturas
# ---------------------------------------------------------------------------------


@login_required
def factura(request):
    factura = Factura.objects.all()
    return render(request, "factura.html", {"factura": factura})


@login_required
def crear(request):
    formulario = FacturaForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect("facturas")
    return render(request, "crear_factura.html", {"formulario": formulario})


@login_required
def editar(request, id):
    factura = Factura.objects.get(id=id)
    formulario = FacturaForm(
        request.POST or None, request.FILES or None, instance=factura
    )
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect("facturas")
    return render(request, "editar.html", {"formulario": formulario})


@login_required
def eliminar(request, id):
    factura = Factura.objects.get(id=id)
    factura.delete()
    return redirect("facturas")


# ---------------------------------------------------------------------------------
# Detalle Factura
# ---------------------------------------------------------------------------------


@login_required
def detalle_factura(request):
    factura_detalle = Detalle_Factura.objects.all()
    return render(
        request,
        "crud_detalle_factura/factura_detalle.html",
        {"factura_detalle": factura_detalle},
    )


@login_required
def detalle_factura_crear(request):
    formulario_pago = FacturaDetalleForm(request.POST or None, request.FILES or None)
    if formulario_pago.is_valid():
        formulario_pago.save()
        return redirect("factura_detalle")
    return render(
        request,
        "crud_detalle_factura/crear_factura_detalle.html",
        {"formulario_pago": formulario_pago},
    )


@login_required
def detalle_factura_editar(request, id):
    factura_detalle = Detalle_Factura.objects.get(id=id)
    formulario_pago = FacturaDetalleForm(
        request.POST or None, request.FILES or None, instance=factura_detalle
    )
    if formulario_pago.is_valid() and request.POST:
        formulario_pago.save()
        return redirect("factura_detalle")
    return render(
        request,
        "crud_detalle_factura/editar_factura_detalle.html",
        {"formulario_pago": formulario_pago},
    )


@login_required
def detalle_factura_eliminar(request, id):
    factura_detalle = Detalle_Factura.objects.get(id=id)
    factura_detalle.delete()
    return redirect("factura_detalle")


# ---------------------------------------------------------------------------------
# Pagos
# ---------------------------------------------------------------------------------


@login_required
def pago_consulta(request):
    pago_detalle = Pago.objects.all()
    return render(request, "pago/pago_detalle.html", {"pago_detalle": pago_detalle})


@login_required
def pago_insertar(request):
    formulario_pago = PagoDetalleForm(request.POST or None, request.FILES or None)
    if formulario_pago.is_valid():
        formulario_pago.save()
        return redirect("pago_consulta")
    return render(request, "pago/pago_crear.html", {"formulario_pago": formulario_pago})


@login_required
def pago_actualizar(request, id):
    pago_detalle = Pago.objects.get(id=id)
    formulario_pago = PagoDetalleForm(
        request.POST or None, request.FILES or None, instance=pago_detalle
    )
    if formulario_pago.is_valid() and request.POST:
        formulario_pago.save()
        return redirect("pago_consulta")
    return render(
        request, "pago/editar_pago.html", {"formulario_pago": formulario_pago}
    )


@login_required
def pago_eliminar(request, id):
    pago_detalle = Pago.objects.get(id=id)
    pago_detalle.delete()
    return redirect("pago_consulta")


# ---------------------------------------------------------------------------------
# Carrito
# ---------------------------------------------------------------------------------


@login_required
def carrito(request):
    carrito = Carrito.objects.all()
    return render(request, "carrito/carrito.html", {"carrito": carrito})


@login_required
def crear_carrito(request):
    formulario = CarritoForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect("consulta_carrito")
    return render(request, "carrito/crear_carrito.html", {"formulario": formulario})


@login_required
def editar_carrito(request, id):
    carrito = Carrito.objects.get(id=id)
    formulario = CarritoForm(
        request.POST or None, request.FILES or None, instance=carrito
    )
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect("consulta_carrito")
    return render(request, "carrito/editar_carrito.html", {"formulario": formulario})


@login_required
def eliminar_carrito(request, id):
    carrito = Carrito.objects.get(id=id)
    carrito.delete()
    return redirect("consulta_carrito")


# ---------------------------------------------------------------------------------
# Pedido
# ---------------------------------------------------------------------------------


@login_required
def pedido(request):
    pedido = Pedido.objects.all()
    return render(request, "pedido/pedido.html", {"pedido": pedido})


@login_required
def crear_pedido(request):
    formulario = PedidoForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect("consulta_pedido")
    return render(request, "pedido/crear_pedido.html", {"formulario": formulario})


@login_required
def editar_pedido(request, id):
    pedido = Pedido.objects.get(id=id)
    formulario = PedidoForm(
        request.POST or None, request.FILES or None, instance=pedido
    )
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect("consulta_pedido")
    return render(request, "pedido/editar_pedido.html", {"formulario": formulario})


@login_required
def eliminar_pedido(request, id):
    pedido = Pedido.objects.get(id=id)
    pedido.delete()
    return redirect("consulta_pedido")
