from django.shortcuts import render
import random
city_names=["london","paris","singapore","dubai","macau","mumbai","pune","delhi","chennai","jaipur","boston"]
word=""
def home(request):
    global word
    word=random.choice(city_names)
    jum=random.sample(word,len(word))
    jum_word=''.join(jum)
    return render(request,'home.html',{'word':jum_word})
def check(request):
    global word
    ans=request.GET.get("ans")
    if ans==word:
        msg="u r right ans is "+word
    else:
        msg="u r wrong correct ans is "+word
    return render(request,'check.html',{'msg':msg})
# Create your views here.
