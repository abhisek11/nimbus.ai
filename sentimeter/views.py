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
        data = sentimeter.primary(input_hastag)
        # data = input_hastag
        return render(request, "result.html", {'data': data})
    return render(request, "index.html", {'input_hastag': user_input})


# # @api_view(["GET"])
# def gettweets(request):
#     tweets = []
#     for tweet in tweepy.Cursor(api.search,q="#" + request.GET.get("text") + " -filter:retweets",rpp=5,lang="en", tweet_mode='extended').items(50):
#         temp = {}
#         temp["text"] = tweet.full_text
#         temp["username"] = tweet.user.screen_name
#         with graph.as_default():
#             prediction = predict(tweet.full_text)
#         temp["label"] = prediction["label"]
#         temp["score"] = prediction["score"]
#         tweets.append(temp)
#     return JsonResponse({"results": tweets});