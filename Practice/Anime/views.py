from django.shortcuts import render
from django.http import HttpRequest
from .models import Tweet
from .forms import Tweetform,userForm
from django.shortcuts import get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
# Create your views here.

def hello(request):
    return render(request, "index.html")


def listTweets(request):
    tweets = Tweet.objects.all().order_by("-created_at")
    return render(request,'all_tweets.html',{"tweets":tweets})


@login_required
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
    

@login_required
def editTweet(request,tweet_id):
 tweet = get_object_or_404(Tweet,pk=tweet_id,user = request.user)

 if request.method=="POST":
    form = Tweetform(request.POST,request.FILES,instance=tweet)
    if  form.is_valid():
          tweet= form.save(commit=False) 
          tweet.user=request.user
          tweet.save()

          return redirect("listTweets")
 else:

  form = Tweetform(instance=tweet)

 return render(request,"create_tweet.html",{"form":form})   

@login_required
def deleteTweet(request,tweet_id):
   tweet = get_object_or_404(Tweet,pk=tweet_id,user = request.user)
   if request.method=="POST":
      tweet.delete()
      return redirect("listTweets")
   
   else:
    return render(request,"delete_tweet.html",{"tweet":tweet})     
   


def register(request):
   if request.method=="POST":
      form = userForm(request.POST)
      if  form.is_valid():
          user= form.save(commit=False) 
          user.set_password(form.cleaned_data["password1"])
          user.save()
          login(request,user)
          return redirect("listTweets")
        

   else:
      form = userForm()


   return render(request,"registration/register.html",{"form":form})  
    