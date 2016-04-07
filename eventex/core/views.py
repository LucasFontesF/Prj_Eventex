from django.shortcuts import render

#Uma view no django é um objeto chamável (callable) que recebe como 1º parâmetro uma instância
#httprequest e retorna uma instância httpresponse
def home(request):
    #renderizar um html chamado index.html
    return render(request, 'index.html')