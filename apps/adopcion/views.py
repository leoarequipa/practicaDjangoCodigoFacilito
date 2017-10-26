from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, CreateView
# Create your views here.
from apps.adopcion.models import Persona, Solicitud
from apps.adopcion.forms import PersonaForm, SolicitudForm

def index(request):
    return HttpResponse("Epalmi pana ")

def epa(request):
    return HttpResponse("Epale xd")



class SolicitudCreate(CreateView):
    model = Solicitud #Establezco el modelo
    template_name = 'adopcion/solicitud_form.html' #Sitio de la plantilla
    form_class = SolicitudForm #Formulario primario
    second_form_class = PersonaForm #Formulario Secundario
    success_url = reverse_lazy('adopcion:solicitud_listar') #Url a la que irá si el formulario se llevo correctamente

    def get_context_data(self, **kwargs):
        """Sobreescribiendo este metodo podemos modificar el comportamiento a la hora de obtener el contexto con el que trabajaremos
            por tanto aqui procedemos a combinar los dos formularios
        """

        #Obtenemos el contexto principal
        context = super(SolicitudCreate, self).get_context_data(**kwargs)

        #Si el primer formulario no esta en el contexto
        if 'form' not in context:
            #Se agrega en la lista, usamos el metodo GET
            context['form'] = self.form_class(self.request.GET)

        #Lo mismo que lo de arriba, pero con el segundo
        if 'form2' not in context:
            context['form2'] = self.second_form_class(self.request.GET)

        return context

    """Este se sobreescribe para modificar el comportamiento al submitear el formulario. El procesamiento de los datos"""

    def post(self, request, *args, **kwargs):
        #Obtenemos el objeto
        self.object = self.get_object()

        #obtenemos los datos de los formularios mediante el metodo POST
        form = self.form_class(request.POST)
        form2 = self.second_form_class(request.POST)

        #Si ambos formularios son validos

        if form.is_valid() and form2.is_valid():
            #Guardamos el primero, pero usando la propiedad commit = False no se guardara todavia
            solicitud = form.save(commit = False)
            #Pasamos al segundo formulario, este si lo guardamos automaticamente porque la propiedad commit es True por defecto
            #Esos datos pasan a ser parte de lo requerido en la variable persona de la clase Solicitud

            solicitud.persona = form2.save()
            #Una vez guardado el segundo procedemos a guardar el primero
            solicitud.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form = form, form2 = form2))
class SolicitudList(ListView):
    model = Solicitud
    template_name = 'adopcion/solicitud_list.html'
