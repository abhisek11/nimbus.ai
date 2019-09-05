from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .forms import userinput
from sentimeter import sentimeter
# import HTML


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
        # for req_data in data_p_n_nu:
        data_positive=data_p_n_nu[0]
        data_negative=data_p_n_nu[1]
        data_neutral=data_p_n_nu[2]
        positive_list=[[x['text'],x['screen_name'],x['created_at'],x['user_location'],x['user_id']]
         for x in data_positive['Positive_list'] ]
        negative_list=[[x['text'],x['screen_name'],x['created_at'],x['user_location'],x['user_id']]
         for x in data_negative['Negative_list'] ]
        neutral_list=[[x['text'],x['screen_name'],x['created_at'],x['user_location'],x['user_id']]
         for x in data_neutral['Neutral_list'] ]
        print("data_positive",data_negative)
        # image=request.build_absolute_uri('/sentimeter/static/media/abg1.png'.url)
        # print('image',image)
        return render(request, "result.html", {'data': data,'data_positive':positive_list,
                                'data_negative':negative_list,'data_neutral':neutral_list,'input_hastag': input_hastag})
    return render(request, "index.html", {'input_hastag': user_input})


