from django.shortcuts import render
from django.http import HttpRequest
from .models import Tweet
from .forms import Tweetform
from django.shortcuts import get_object_or_404,redirect
# Create your views here.

def hello(request):
    return render(request, "index.html")


def listTweets(request):
    tweets = Tweet.objects.all().order_by("-created_at")
    return render(request,'all_tweets.html',{"tweets":tweets})



def createTweet(request):
    if request.method == "POST":
        form = Tweetform(request.POST, request.FILES)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect("listTweets")
        else:
            print(form.errors)  # Debugging
    else:
        form = Tweetform()

    return render(request, "create_tweet.html", {"form": form})
    


def editTweet(request,tweet_id):
 tweet = get_object_or_404(Tweet,pk=tweet_id,user = request.user)

 if request.method=="POST":
    form = Tweetform(request.POST,request.Files,instance=tweet)
    if  form.is_valid():
          tweet= form.save(commit=False) 
          tweet.user=request.user
          tweet.save()

          return redirect("listTweets")
 else:

  form = Tweetform(instance=tweet)

 return render(request,"create_tweet.html",{"form":form})   


def deleteTweet(request,tweet_id):
   tweet = get_object_or_404(Tweet,pk=tweet_id,user = request.user)
   if request.method=="POST":
      tweet.delete()
      return redirect("listTweets")
   
   else:
    return render(request,"delete_tweet.html",{"tweet":tweet})     