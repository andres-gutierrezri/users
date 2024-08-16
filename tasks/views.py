from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .models import Task, Factura, Detalle_Factura, Pago, Carrito
from .forms import FacturaForm, FacturaDetalleForm, PagoDetalleForm, CarritoDetalleForm


from .forms import TaskForm


# Create your views here.
def signup(request):
    if request.method == "GET":
        return render(request, "signup.html", {"form": UserCreationForm})
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
                    {"form": UserCreationForm, "error": "Username already exists."},
                )

        return render(
            request,
            "signup.html",
            {"form": UserCreationForm, "error": "Passwords did not match."},
        )


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
        return render(request, "create_task.html", {"form": TaskForm})
    else:
        try:
            form = TaskForm(request.POST)
            new_task = form.save(commit=False)
            new_task.user = request.user
            new_task.save()
            return redirect("tasks")
        except ValueError:
            return render(
                request,
                "create_task.html",
                {"form": TaskForm, "error": "Error creating task."},
            )


def home(request):
    return render(request, "home.html")


@login_required
def signout(request):
    logout(request)
    return redirect("home")


def signin(request):
    if request.method == "GET":
        return render(request, "signin.html", {"form": AuthenticationForm})
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
                    "form": AuthenticationForm,
                    "error": "Username or password is incorrect.",
                },
            )

        login(request, user)
        return redirect("tasks")


@login_required
def task_detail(request, task_id):
    if request.method == "GET":
        task = get_object_or_404(Task, pk=task_id, user=request.user)
        form = TaskForm(instance=task)
        return render(request, "task_detail.html", {"task": task, "form": form})
    else:
        try:
            task = get_object_or_404(Task, pk=task_id, user=request.user)
            form = TaskForm(request.POST, instance=task)
            form.save()
            return redirect("tasks")
        except ValueError:
            return render(
                request,
                "task_detail.html",
                {"task": task, "form": form, "error": "Error updating task."},
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


@login_required
# leer  los  datos
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


@login_required
# leer  los  datos  de pago
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


@login_required
# leer  los  datos
def carrito_detalle(request):
    carrito_detalle = Carrito.objects.all()
    return render(
        request, "carrito/carrito_detalle.html", {"carrito_detalle": carrito_detalle}
    )


@login_required
def carrito_insertar(request):
    carrito_formulario = CarritoDetalleForm(request.POST or None, request.FILES or None)
    if carrito_formulario.is_valid():
        carrito_formulario.save()
        return redirect("carrito_detalle")
    return render(
        request,
        "carrito/carrito_insertar.html",
        {"carrito_formulario": carrito_formulario},
    )


@login_required
def carrito_actualizar(request, id):
    carrito_detalle = Carrito.objects.get(id=id)
    carrito_formulario = CarritoDetalleForm(
        request.POST or None, request.FILES or None, instance=carrito_detalle
    )
    if carrito_formulario.is_valid() and request.POST:
        carrito_formulario.save()
        return redirect("carrito_detalle")
    return render(
        request,
        "carrito/carrito_editar.html",
        {"carrito_formulario": carrito_formulario},
    )


@login_required
def carrito_eliminar(request, id):
    carrito_detalle = Carrito.objects.get(id=id)
    carrito_detalle.delete()
    return redirect("carrito_detalle")
