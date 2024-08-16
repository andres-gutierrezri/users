from django.forms import ModelForm
from .models import Task, Factura, Detalle_Factura, Pago

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'important']
        
class FacturaForm(ModelForm):
    class Meta:
        model = Factura
        fields = '__all__'
        
class FacturaDetalleForm(ModelForm):
    class Meta:
        model = Detalle_Factura
        fields = '__all__'
        
class PagoDetalleForm(ModelForm):
    class Meta: 
        model = Pago
        fields = '__all__'
        