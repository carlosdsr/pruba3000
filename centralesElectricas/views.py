from django.shortcuts import render, redirect
from .forms import CentralesElectricasForm, ImprimirCentral1Form, ImprimirCentral2Form, \
    ImprimirCentral3Form, asociacionNodosForm,editarNodosForm,ImprimirKWsForm
from .models import CentralesElectricas, AsociacionNodos
from django.contrib import messages
from django.views.generic import ListView


def registrarNodo(request):
    if request.method == "POST":
        form = CentralesElectricasForm(request.POST)

        if form.is_valid():
            try:
                form.save()
                messages.success(request, f'Se ha registrado el nodo con exito')
                return redirect('/dashboard-OPE/')
            except:
                pass
    else:
        form = CentralesElectricasForm()
    return render(request, 'centralesElectricas/registrarNodo.html', {'form': form})


def editarNodos(request):
    if request.method == "POST":

        form = editarNodosForm(request.POST)
        form2 = ImprimirKWsForm(request.POST)
        nombreAsociacion= request.POST.get('NombreAsociacion')
        kws = request.POST.get('KWs')
        nodo1 = AsociacionNodos.objects.get(id=int(NombreAsociacion))


        if form2.is_valid():
            try:

                nodo1.KWs=kws
                nodo1.save(update_fields=['KWs'])
                
                messages.success(request, f'Su asociacion fue editada con exito')
               
                return redirect('/dashboard-OPE/')
            
            except:
                pass
    else:
        form = editarNodosForm(instance=request.user)
        form2 = ImprimirKWsForm(request.POST)
  
    return render(request, 'centralesElectricas/editarAsociaciones.html', {'form': form, 'form2': form2})

def eliminarNodos(request):
    if request.method == "POST":

       
        form2 = ImprimirKWsForm(request.POST)
        nombreAsociacion= request.POST.get('NombreAsociacion')
        
        asociacion = AsociacionNodos.objects.get(id=int(NombreAsociacion))
        asociacion.delete()
        messages.success(request, f'Su asociacion fue eliminada con exito')
               
        return redirect('/dashboard-OPE/')
  
    else:
        
        form2 = ImprimirKWsForm(request.POST)
  
    return render(request, 'centralesElectricas/eliminarAsociacion.html', {'form2': form2})





def asociarNodos(request):
    if request.method == "POST":
        form = ImprimirCentral1Form(request.POST)
        form1 = ImprimirCentral2Form(request.POST)
        form2 = ImprimirCentral3Form(request.POST)
        form3 = asociacionNodosForm(request.POST)
        central1 = request.POST.get('central1')
        central2 = request.POST.get('central2')
        central3 = request.POST.get('central3')
        kws = request.POST.get('KWs')
        nombre = request.POST.get('nombreAsociacion')

        if central3 == '':
            nodo3 = 0
        else:
            nodo3 = CentralesElectricas.objects.get(id=int(central3))

        nodo1 = CentralesElectricas.objects.get(id=int(central1))
        nodo2 = CentralesElectricas.objects.get(id=int(central2))
        if nodo1.tipoDeNodo == 'Centrales de Generacion' and nodo2.tipoDeNodo == 'Centros de Distribucion'\
                and nodo3 == 0:
            data = {'nodo1': central1,
                    'nodo2': central2,
                    'nodo3': central3,
                    'KWs': kws,
                    'nombreAsociacion': nombre,
                    'tipoAsociacion': 'C.Generacion->C.Distribucion'
                    }
            form3 = asociacionNodosForm(data)
            if form3.is_valid():
                try:
                    form3.save()
                    messages.success(request, f'La asociacion C.Generacion->C.Distribucion se realizo con exito')
                    return redirect('/dashboard-OPE/')
                except:
                    pass
        elif nodo1.tipoDeNodo == 'Centrales Termoelectricas' and nodo2.tipoDeNodo == 'Centros de Distribucion'\
                and nodo3 == 0:
            data = {'nodo1': central1,
                    'nodo2': central2,
                    'nodo3': central3,
                    'KWs': kws,
                    'nombreAsociacion': nombre,
                    'tipoAsociacion': 'C.Termoelectricas->C.Distribucion'
                    }
            form3 = asociacionNodosForm(data)
            if form3.is_valid():
                try:
                    form3.save()
                    messages.success(request, f'La asociacion C.Termoelectricas->C.Distribucion se realizo con exito')
                    return redirect('/dashboard-OPE/')
                except:
                    pass
        elif nodo1.tipoDeNodo == 'Centros de Distribucion' and nodo2.tipoDeNodo == 'Centros de Distribucion'\
                and nodo1.id != nodo2.id and nodo3 == 0:
            data = {'nodo1': central1,
                    'nodo2': central2,
                    'nodo3': central3,
                    'KWs': kws,
                    'nombreAsociacion': nombre,
                    'tipoAsociacion': 'C.Distribucion->C.Distribucion'
                    }
            form3 = asociacionNodosForm(data)
            if form3.is_valid():
                try:
                    form3.save()
                    messages.success(request, f'La asociacion C.Distribucion->C.Distribucion se realizo con exito')
                    return redirect('/dashboard-OPE/')
                except:
                    pass
        elif nodo1.tipoDeNodo == 'Centrales de Generacion' and nodo2.tipoDeNodo == 'Centrales Termoelectricas' \
                and nodo3.tipoDeNodo == 'Centros de Distribucion':
            data = {'nodo1': central1,
                    'nodo2': central2,
                    'nodo3': central3,
                    'KWs': kws,
                    'nombreAsociacion': nombre,
                    'tipoAsociacion': 'C.Generacion->C.Termoelectricas->C.Distribucion'
                    }
            form3 = asociacionNodosForm(data)
            if form3.is_valid():
                try:
                    form3.save()
                    messages.success(request, f'La asociacion C.Generacion->C.Termoelectricas->C.Distribucion'
                    f' se realizo con exito')
                    return redirect('/dashboard-OPE/')
                except:
                    pass
        else:
            messages.warning(request, f'No se pudo realizar ninguna asociacion')
            pass
    else:
        form = ImprimirCentral1Form()
        form1 = ImprimirCentral2Form()
        form2 = ImprimirCentral3Form()
        form3 = asociacionNodosForm()
    return render(request, 'centralesElectricas/asociarNodos.html', {'form': form, 'form1': form1, 'form2': form2, 'form3': form3})


class ListaDeCentrales(ListView):
    template_name = 'centralesElectricas/listaDeCentrales.html'
    queryset = CentralesElectricas.objects.all()



