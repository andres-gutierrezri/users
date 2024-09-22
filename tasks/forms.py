from django.forms import ModelForm
from .models import Task, Factura, Detalle_Factura, Pago, Carrito, Pedido


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["title", "description", "important"]


class FacturaForm(ModelForm):
    class Meta:
        model = Factura
        fields = "__all__"


class FacturaDetalleForm(ModelForm):
    class Meta:
        model = Detalle_Factura
        fields = "__all__"


class PagoDetalleForm(ModelForm):
    class Meta:
        model = Pago
        fields = "__all__"


class CarritoForm(ModelForm):
    class Meta:
        model = Carrito
        fields = "__all__"


class PedidoForm(ModelForm):
    class Meta:
        model = Pedido
        fields = "__all__"
