from django.shortcuts import render
from django.views import View
tickets = []

# Create your views here.
class Home(View):
  def get(self,request):
    return render(request, 'main/index.html')
  def post(self,request):
    datetime = request.POST["datetime"]
    location = request.POST["location"] 
    
    
    tickets.append((datetime,location))
    
    
    return render(request, 'main/results.html',{"tickets":tickets})