from django.shortcuts import render
from django.views import View

# Create your views here.
class Home(View):

  def get(self, request):

      return render(request, 'main/index.html')

  def post(self, request):

      Name = request.POST['name']
      Weight = (request.POST['weight'])
      HeightFt = (request.POST['heightft'])
      HeightIn = (request.POST['heightin'])  
      replDict = {}
      isCorrect = True

      try:
        Weight = int(Weight)
        HeightFt = int(HeightFt)
        HeightIn = int(HeightIn)
      except ValueError:
        isCorrect = False
        replDict['error5'] = "Invalid inputs in Weight, Heightft or Heightin"
        return render(request, 'main/erroranalysis.html', {'replDict' : replDict})

      if HeightFt < 0:
          replDict['error1'] = "HeightFt cannot be negative!"
          isCorrect = False

      if HeightFt > 10:
        replDict['error2'] = "HeightFt cannot be that excessive. " + HeightFt +  " is way too large!"
        isCorrect = False

      if HeightIn < 0:
        replDict['error3'] = "HeightIn cannot be negative!"
        isCorrect = False

      if HeightIn >= 12:
        replDict['error4'] = "HeightIn should not be equal to or larger than 12. Please re-enter the information by clicking this link."
        isCorrect = False
              
      height = (HeightFt * 12) + HeightIn
      bmi = 703 * height / (Weight * Weight)

      if isCorrect == False:
        return render(request, 'main/erroranalysis.html', {'replDict' : replDict})


      return render(request, 'main/response.html', {'bmi':bmi,'name':Name,'weight':Weight,'heightft':HeightFt,'heightin':HeightIn,'replDict':replDict})