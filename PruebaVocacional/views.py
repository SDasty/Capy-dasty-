from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Test, Student
from .forms import TestForm, StudentForm



def home(request,id_estudiante):
    
    return render(request,'home.html',{'id_estudiante': id_estudiante})

def home_name(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            estudiante = form.save()  
            return redirect('home', id_estudiante=estudiante.id_estudiante)
    else:
        form = StudentForm()
    return render(request, 'home_name.html', {'form': form})
        
        
        
        
        


def test(request,id_estudiante):
    return render(request,'test.html',{'id_estudiante': id_estudiante})

def answers(request,id_estudiante):
    
    student = Student.objects.get(id_estudiante=id_estudiante)
    print(student.nombre)
    print(student.id_estudiante)
    questions =['¿Te gusta trabajar con números y fórmulas?','¿Te gustaría trabajar en un laboratorio?','¿Te sientes atraído/a por el mundo de los negocios?','¿Te gusta leer y analizar obras literarias?','¿Te gustaría trabajar en un hospital?','¿Te atrae la idea de diseñar edificios y construcciones?','¿Te gusta crear contenido para redes sociales?','¿Te atrae la idea de investigar nuevos medicamentos?','¿Te interesa la programación de computadoras?','¿Te gustaría trabajar en laindustria cinematográfica?','¿Te sientes atraído/a por el arte y la creatividad?','¿Te gustaría trabajar en una organización sin fines de lucro?','¿Te atrae la idea de trabajar en un banco?','¿Te gusta trabajar con maquinaria y herramientas?','¿Te interesa la ingeniería civil?','¿Te gustaría trabajar en la producción de música?','¿Te atrae la idea de trabajar en un despacho de abogados o estudio jurídico,?','¿Te interesa la biología y la vida marina?','¿Te gustaría trabajar en el área de recursos humanos?','¿Te gusta el análisis de datos?','¿Te interesa la psicología y la salud mental?','¿Te atrae la idea de trabajar en una agencia de publicidad?','¿Te gustaría trabajar en la industria alimentaria?','¿Te sientes atraído/a por el mundo del deporte?','¿Te gustaría trabajar en el área de ventas?','¿Te interesa la mecánica y la tecnología?','¿Te atrae la idea de trabajar en una organización internacional?','¿Te gusta trabajar con animales?','¿Te gustaría trabajar en una revista o periódico?','¿Te interesa la arqueología y la historia antigua?']
    if request.method == 'POST':
        form = TestForm(request.POST)
        if form.is_valid():
            test = form.save(commit=False)
            test.id_estudiante = student
            test.nombre = student.nombre
            test.save()
            return redirect('result', id_estudiante=id_estudiante)
        else:
            print("Errores en el formulario:")
            print(form.errors)
    else:
        form = TestForm(initial={'nombre': student.nombre, 'id_estudiante': id_estudiante})

    return render(request, 'answers.html', {'form': form, 'id_estudiante': id_estudiante, 'questions': questions, 'nombre': student.nombre})

def result(request,id_estudiante):
    test  = Test.objects.get(id_estudiante=id_estudiante)
    
    areas={1:'Administrativas y contables',2: 'Humanísticas, Ciencias Jurídicas y Sociales',3:'Artísticas',4:'Ciencias de la salud',5:'Ingenierías, carreras técnicas y computación',6:'Ciencias exactas'}
    puntos={1:0,2:0,3:0,4:0,5:0,6:0}
    
    universidades = {
  "Administrativas y contables": [
    {
      "Nombre" : "Eafit",
      "Logo" : "https://www.universidadesonline.com.co/logos/original/logo-universidad-eafit.png",
      "Enlace": "https://www.eafit.edu.co/Administracion"
    },
    
    {
      "Nombre" : "Universidad de medellin",
      "Logo" : "https://geobon.org/wp-content/uploads/2019/06/1200px-Escudo_Universidad_de_Medellin.svg_-1024x1024.png",
      "Enlace": "https://fcea.udemedellin.edu.co/administracion-de-empresas/#gsc.tab=0"
    },
	
    {
      "Nombre" : "POLI",
      "Logo" : "https://medellin.poli.edu.co/sites/default/files/logos/politecnico-grancolombiano_2.svg",
      "Enlace": "https://medellin.poli.edu.co/?switch_domain=medellin_poli_edu_co"
    }
  ],
  "Humanísticas, Ciencias Jurídicas y Sociales": [
    {
      "Nombre" : "Unaula",
      "Logo" : "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fceadigilaw.org%2Fwp-content%2Fuploads%2F2020%2F03%2FUNAULA.png&f=1&nofb=1&ipt=3080ca322eab4b2f94c5c30b079e916f2e29cc7f7473c46a4a641cd4a57c6703&ipo=images",
      "Enlace": "https://www.unaula.edu.co/derecho"
    },
    
    {
      "Nombre" : "EAFIT",
      "Logo" : "https://www.universidadesonline.com.co/logos/original/logo-universidad-eafit.png",
      "Enlace": "https://www.eafit.edu.co/escuela-humanidades"
    },
	
    {
      "Nombre" : "UNAL",
      "Logo" : "https://www.salsa-tipiti.org/wp-content/uploads/2023/05/UNAL-LOGO-2.jpg",
      "Enlace": "https://cienciashumanasyeconomicas.medellin.unal.edu.co/"
    }
  ],
  "Artísticas": [
    {
      "Nombre" : "EAFIT",
      "Logo" : "https://www.universidadesonline.com.co/logos/original/logo-universidad-eafit.png",
      "Enlace": "https://www.eafit.edu.co/escuela-humanidades"
    },
    
    {
      "Nombre" : "Bellas artes",
      "Logo" : "https://yt3.ggpht.com/a/AATXAJzokYvFFyYlVTXB7dCV3dvBCGX0cJOG0iV2PA=s900-c-k-c0xffffffff-no-rj-mo",
      "Enlace": "https://bellasartesmed.edu.co/pregrados/artes-plasticas/"
    },
	
    {
      "Nombre" : "UPB",
      "Logo" : "https://whatthelogo.com/storage/logos/universidad-pontificia-bolivariana-84437.png",
      "Enlace": "https://www.upb.edu.co/es/bienestar/arte-cultura/formacion-artistica-cultural-medellin"
    }
  ],
  "Ciencias de la salud": [
    {
      "Nombre" : "CES",
      "Logo" : "https://yt3.ggpht.com/a/AGF-l78Cmyck6lei2NCvPAYerzhxRr9e4-IAXvsALg=s900-c-k-c0xffffffff-no-rj-mo",
      "Enlace": "https://www.ces.edu.co/programas/carreras/?facultad-programa=facultad-de-medicina&orderby=start_at"
    },
    
    {
      "Nombre" : "Remington",
      "Logo" : "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.dC-GyhQdR8q2piulz2TbKgHaHa%26pid%3DApi&f=1&ipt=a52d3e6bc919c383fc8e6d400a7d0bbd8248ce8ee6d987e89a0e52ec58e36238&ipo=images",
      "Enlace": "https://www.uniremington.edu.co/facultades/facultad-de-ciencias-de-la-salud/medicina/"
    },
	
    {
      "Nombre" : "udea",
      "Logo" : "https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2F1.bp.blogspot.com%2F-i-a8Vk0uKKQ%2FUaRlpJICDuI%2FAAAAAAAABh0%2Fj0sTjvOv-9k%2Fs1600%2Flogotipo%2Budea.png&f=1&nofb=1&ipt=d3653bdac0cd970f43f493dd33ac1a27ccd6f897318a27a3235999553503a174&ipo=images",
      "Enlace": "https://www.udea.edu.co/wps/portal/udea/web/inicio/unidades-academicas/medicina"
    }
  ],
  "Ingenierías, carreras técnicas y computación": [
    {
      "Nombre" : "Politecnico jaime isaza cadavid",
      "Logo" : "https://i1.rgstatic.net/ii/institution.image/AS:267480063250434%401440783624387_l",
      "Enlace": "https://www.politecnicojic.edu.co/facultad-de-ingenieria"
    },
    
    {
      "Nombre" : "Eafit",
      "Logo" : "https://www.universidadesonline.com.co/logos/original/logo-universidad-eafit.png",
      "Enlace": "https://www.eafit.edu.co/escuela-ingenieria"
    },
	
    {
      "Nombre" : "ITM",
      "Logo" : "https://w7.pngwing.com/pngs/349/183/png-transparent-instituto-tecnologico-metropolitano-de-medellin-university-itm-campus-prado-technology-institute-medellin-blue-text-logo.png",
      "Enlace": "https://www.itm.edu.co/facultad-ingenierias/"
    }
  ],
  "Ciencias exactas": [
    {
      "Nombre" : "udea",
      "Logo" : "https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2F1.bp.blogspot.com%2F-i-a8Vk0uKKQ%2FUaRlpJICDuI%2FAAAAAAAABh0%2Fj0sTjvOv-9k%2Fs1600%2Flogotipo%2Budea.png&f=1&nofb=1&ipt=d3653bdac0cd970f43f493dd33ac1a27ccd6f897318a27a3235999553503a174&ipo=images",
      "Enlace": "https://www.udea.edu.co/wps/portal/udea/web/inicio/unidades-academicas/ciencias-exactas-naturales"
    },
    
    {
      "Nombre" : "UNAL",
      "Logo" : "https://www.salsa-tipiti.org/wp-content/uploads/2023/05/UNAL-LOGO-2.jpg",
      "Enlace": "https://ciencias.medellin.unal.edu.co/"
    },
	
    {
      "Nombre" : "ITM",
      "Logo" : "https://w7.pngwing.com/pngs/349/183/png-transparent-instituto-tecnologico-metropolitano-de-medellin-university-itm-campus-prado-technology-institute-medellin-blue-text-logo.png",
      "Enlace": "https://www.itm.edu.co/facultad-ciencias-exactas-aplicadas/departamento-de-educacion-y-ciencias-basicas/"
    }
  ]

}
    table = [
    [[1, 6], 5, 4, 2],
    [6, 4, 2, [1, 3]],
    [[1, 2], 5, [4, 6], 3],
    [2, 3, [4, 5], [1, 6]],
    [4, 2, [1, 5, 6], 3],
    [5, 3, [1, 4, 6], 2],
    [3, [1, 2], 4, [5, 6]],
    [4, 5, [1, 2, 6], 3],
    [5, 6, [1, 4], [3, 2]],
    [[2, 3], 5, [1, 6], 4],
    [[2, 3], 5, [4, 6], 1],
    [2, [1, 3], 4, [5, 6]],
    [1, 5, [2, 6], [3, 4]],
    [5, [4, 6], [1, 2], 3],
    [5, 6, 3, 1],
    [3, 2, 5, 4],
    [2, 1, 5, 3],
    [4, 6, 5, 1],
    [2, 1, 1, 3],
    [[1, 6], 5, 2, 3],
    [2, 4, 6, 5],
    [3, 2, 1, 4],
    [4, 2, 1, 3],
    [4, 2, 3, 5],
    [1, 2, 3, 4],
    [5, 6, 4, 2],
    [5, 1, 5, 2],
    [4, 4, 4, 3],
    [2, 3, 1, 4],
    [2, 3, 6, 1]
]
    total_puntos = 0
    for i in range(1,31):
        respuesta = getattr(test,f"respuesta{i}",None)
        if respuesta is not None:
            value = table[i-1][respuesta]
            try:
                for j in value:
                    total_puntos+=1
                    puntos[j] = puntos[j]+1
            except:
                total_puntos+=1
                puntos[value] = puntos[value]+1


    puntos = {k: v for k, v in sorted(puntos.items(), key=lambda item: item[1],reverse=True)}
    print(total_puntos)
    ranking = []
    for clave in puntos:
        area = areas[clave]
        percentage = (puntos[clave]/total_puntos)*100
        percentage = format(percentage, '.2f')        
        ranking.append((area,percentage,universidades[area]))   
        
    return render(request,'result.html',{'id_estudiante':id_estudiante,'nombre':test.nombre,'ranking':ranking})
