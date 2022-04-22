from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from app.models import *
def insert_topic(request):
    if request.method=='POST':
        #print(request.POST)
        #TN=request.POST['topic']
        TN=request.POST.get('topic')
        print(TN)
        T=Topic.objects.get_or_create(topic_name=TN)[0]
        T.save()

    return render(request,'insert_topic.html')

def insert_webpage(request):
    toipcs=Topic.objects.all()
    d={'ts':'topics'}
    if request.method=='POST':
        tn=request.POST['topic']
        print(tn)
        T=Topic.objects.get_or_create(topic_name=tn)[0]
        T.save()
        n=request.POST['name']
        u=request.POST['url']
        W=Webpage.objects.get_or_create(topic_name=T,name=n,url=u)[0]
        W.save()
        return HttpResponse('webpage is submitted successfully')
    return render(request,'insert_webpage.html',d)