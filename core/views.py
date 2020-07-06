from django.shortcuts import render
from django.contrib import messages
from .forms import ContatoForms
from django.http import JsonResponse
import zipfile
from django.views.decorators.csrf import csrf_protect

from django.conf import settings
'''produção'''
your_static_root = settings.STATIC_ROOT

'''local'''
#your_static_root = 'core' + settings.STATIC_URL


@csrf_protect
def get(request):
    mini_bacia = int(request.GET.get("mini_bacia"))
    print(mini_bacia)

    path1 = your_static_root

    """AQUI FAZEMOS A BUSCA NO BANCO DE DADOS"""

    if mini_bacia <= 2001:
        file_ZIP = zipfile.ZipFile(r'{}/vazoes/dados_mini0.zip'.format(path1), 'r')
        pathFileQ = file_ZIP.namelist()

    elif mini_bacia <= 4001:
        file_ZIP = zipfile.ZipFile(r'{}/vazoes/dados_mini2.zip'.format(path1), 'r')
        pathFileQ = file_ZIP.namelist()

    elif mini_bacia <= 6001:
        file_ZIP = zipfile.ZipFile(r'{}/vazoes/dados_mini4.zip'.format(path1), 'r')
        pathFileQ = file_ZIP.namelist()

    elif mini_bacia <= 8001:
        file_ZIP = zipfile.ZipFile(r'{}/vazoes/dados_mini6.zip'.format(path1), 'r')
        pathFileQ = file_ZIP.namelist()

    elif mini_bacia <= 10001:
        file_ZIP = zipfile.ZipFile(r'{}/vazoes/dados_mini8.zip'.format(path1), 'r')
        pathFileQ = file_ZIP.namelist()

    elif mini_bacia <= 12001:
        file_ZIP = zipfile.ZipFile(r'{}/vazoes/dados_mini10.zip'.format(path1), 'r')
        pathFileQ = file_ZIP.namelist()

    elif mini_bacia <= 14001:
        file_ZIP = zipfile.ZipFile(r'{}/vazoes/dados_mini12.zip'.format(path1), 'r')
        pathFileQ = file_ZIP.namelist()

    elif mini_bacia <= 16001:
        file_ZIP = zipfile.ZipFile(r'{}/vazoes/dados_mini14.zip'.format(path1), 'r')
        pathFileQ = file_ZIP.namelist()

    elif mini_bacia <= 18001:
        file_ZIP = zipfile.ZipFile(r'{}/vazoes/dados_mini16.zip'.format(path1), 'r')
        pathFileQ = file_ZIP.namelist()

    elif mini_bacia <= 20001:
        file_ZIP = zipfile.ZipFile(r'{}/vazoes/dados_mini18.zip'.format(path1), 'r')
        pathFileQ = file_ZIP.namelist()

    elif mini_bacia <= 22001:
        file_ZIP = zipfile.ZipFile(r'{}/vazoes/dados_mini20.zip'.format(path1), 'r')
        pathFileQ = file_ZIP.namelist()

    elif mini_bacia <= 24001:
        file_ZIP = zipfile.ZipFile(r'{}/vazoes/dados_mini22.zip'.format(path1), 'r')
        pathFileQ = file_ZIP.namelist()

    elif mini_bacia <= 26001:
        file_ZIP = zipfile.ZipFile(r'{}/vazoes/dados_mini24.zip'.format(path1), 'r')
        pathFileQ = file_ZIP.namelist()

    elif mini_bacia <= 28001:
        file_ZIP = zipfile.ZipFile(r'{}/vazoes/dados_mini26.zip'.format(path1), 'r')
        pathFileQ = file_ZIP.namelist()

    elif mini_bacia <= 30001:
        file_ZIP = zipfile.ZipFile(r'{}/vazoes/dados_mini28.zip'.format(path1), 'r')
        pathFileQ = file_ZIP.namelist()

    elif mini_bacia <= 32001:
        file_ZIP = zipfile.ZipFile(r'{}/vazoes/dados_mini30.zip'.format(path1), 'r')
        pathFileQ = file_ZIP.namelist()

    elif mini_bacia <= 33749:
        file_ZIP = zipfile.ZipFile(r'{}/vazoes/dados_mini32.zip'.format(path1), 'r')
        pathFileQ = file_ZIP.namelist()

    with file_ZIP as z:
        with z.open(pathFileQ[0]) as f:
            decod = f.readlines()

    lines = []
    for i in range(len(decod)):
        lines.append(decod[i].decode('utf-8'))

    data = lines[0]
    data_list = data.split(";")  # Criando uma lista com as datas

    vazao = []  # Criando uma lisca com as mini + vazões
    for i in range(1, len(lines)):
        vazao.append(lines[i])

    aux = []
    db_data=[]
    for i in range(len(vazao)):
        if str(mini_bacia) == vazao[i].split(";")[0]:  # AQUI VE SELECIONA A VAZÃO DA MINI ESCOLHIDA
            aux = (vazao[i].split(";"))
    for i in range(1, len(aux)):
        db_data.append(
            {'datetime': (data_list[i]),
             'time_series': (float(aux[i])),
             'cod': mini_bacia,
            })
    #print(your_static_root)
    return JsonResponse(list(db_data), safe=False)



def index(request):
    return render(request, 'index.html')

def mapa(request):
    return render(request, 'mapa.html')

def grafico(request):
    return render(request, 'grafico.html')

def teste(request):
    return render(request, 'teste.html')

def contato(request):
    form = ContatoForms(request.POST or None)

    if str(request.method) == 'POST':
        if form.is_valid():
            form.send_mail()

            messages.success(request, "E-mail enviado com Sucesso!")
            form = ContatoForms()

        else:
            messages.error(request, "Erro ao enviar E-mail""")
    context = {
        'form': form
    }
    return render(request, 'contato.html', context)

