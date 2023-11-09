from django.shortcuts import render
from PruebaVocacional.models import Student
from .forms import CalculadoraNotasForm  # Asegúrate de que la ruta sea correcta
from .utils import calcular_promedio_ponderado  # Asegúrate de que la ruta sea correcta



def calculaNota(request, id_estudiante):
    if request.method == 'POST':
        form = CalculadoraNotasForm(request.POST)
        if form.is_valid():
            notas_creditos = []

            for i in range(1, 6):  # Supongamos que tienes 5 entradas de notas y créditos
                nota = form.cleaned_data.get(f'nota{i}')
                creditos = form.cleaned_data.get(f'creditos{i}')

                if nota is not None and creditos is not None:
                    notas_creditos.append((nota, creditos))

            promedio_ponderado = calcular_promedio_ponderado(notas_creditos)

            context = {
                'promedio_ponderado': promedio_ponderado,
                'id_estudiante': id_estudiante,  # Asegúrate de incluir id_estudiante en el contexto
            }

            return render(request, 'resultado_calculo.html', context)
    else:
        form = CalculadoraNotasForm()

    context = {
        'form': form,
        'id_estudiante': id_estudiante,  # Asegúrate de incluir id_estudiante en el contexto
    }

    return render(request, 'calcular_nota.html', context)




