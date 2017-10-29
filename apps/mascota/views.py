from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.core import serializers

# Create your views here.
from apps.mascota.forms import MascotaForm
from apps.mascota.models import Mascota

def listado(request):
    lista = serializers.serialize('json', Mascota.objects.all(), fields=['nombre', 'sexo', 'edad_aproximada'])
    return HttpResponse(lista, content_type='application/json')

def index(request):
    print(request)

    return render(request, 'mascota/index.html')

def mascota_view(request):
    if request.method == 'POST':
        form = MascotaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mascota:index')
    else:
        form = MascotaForm()

    return render(request, 'mascota/mascota_form.html', {'form' : form})


def mascota_list(request):
    mascotas = Mascota.objects.all().order_by('folio')
    contexto = {'mascotas' : mascotas}

    return render(request, 'mascota/mascota_list.html', contexto)

def mascota_edit(request, id_mascota):
    try:
        mascota = Mascota.objects.get(folio=id_mascota)
    except:
        mascota = None

    if mascota is not None:
        if request.method == 'GET':

            form = MascotaForm(instance = mascota)
        else:
            print("khe")
            form = MascotaForm(request.POST, instance = mascota)

            if form.is_valid():
                form.save()

            return redirect('mascota:mascota_listar')

        return render(request, 'mascota/mascota_form.html', {'form':form})

def mascota_delete(request, id_mascota):
    try:
        mascota = Mascota.objects.get(folio=id_mascota)
    except:
        mascota = None

    if mascota is not None:
        if request.method == 'POST':
            mascota.delete()
            return redirect('mascota:mascota_listar')

    return render(request, 'mascota/mascota_delete.html', {'mascota' : mascota})


class MascotaList(ListView):
    model = Mascota
    template_name = 'mascota/mascota_list.html'
    paginate_by = 2

class MascotaCreate(CreateView):
    model = Mascota
    form_class = MascotaForm
    template_name = 'mascota/mascota_form.html'
    success_url = reverse_lazy('mascota:mascota_listar')


class MascotaUpdate(UpdateView):
    model = Mascota
    form_class = MascotaForm
    template_name = 'mascota/mascota_form.html'
    success_url = reverse_lazy('mascota:mascota_listar')

class MascotaDelete(DeleteView):
    model = Mascota
    template_name = 'mascota/mascota_delete.html'
    success_url = reverse_lazy('mascota:mascota_listar')
