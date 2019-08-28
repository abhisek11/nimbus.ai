from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .forms import userinput
from sentimeter import sentimeter


def index(request):
    user_input = userinput()
    return render(request, "index.html", {'input_hastag': user_input})

def analyse(request):
    user_input = userinput(request.GET or None)
    if request.GET and user_input.is_valid():
        input_hastag = user_input.cleaned_data['q']
        print(input_hastag)
        data_all = sentimeter.primary(input_hastag)
        # data = input_hastag
        data=data_all[:4]
        data_p_n_nu=data_all[4:]
        data_positive=data_p_n_nu[0]['Positive_list']
        # print("data_positive",data_positive)
        # print("data::",data)
        # print("pop data::::::::::::::::::::::::::::::::::::::::::",data_p_n_nu)
        return render(request, "result.html", {'data': data,'data_p_n_nu':data_positive})
    return render(request, "index.html", {'input_hastag': user_input})


