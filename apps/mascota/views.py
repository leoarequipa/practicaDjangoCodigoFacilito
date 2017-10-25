from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse

# Create your views here.
from apps.mascota.forms import MascotaForm
from apps.mascota.models import Mascota

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
