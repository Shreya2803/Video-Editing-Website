from django.http import HttpResponse
from django.shortcuts import render
import pyttsx3
from django.urls import reverse_lazy,reverse
import PyPDF2
import pdfrw
import io



# Create views here.
def home(request):
  return render(request, 'index.html')
def webpage2(request):
    language = 'en'
    music = ''
    if request.method == 'POST' and request.FILES['pdf']:
        gender = request.POST.get('gender')
        speed = request.POST.get('speed')
        volume = request.POST.get('volume')
        text = request.POST.get('text')

        # if pdf available

        if pdf:
            pdfReader = PyPDF2.PdfFileReader(io.BytesIO(pdf))
            content = ''
                # creating a page object
    
            for i in range(int(pdfReader.numPages)):
                content += pdfReader.getPage(i).extractText() + "\n"
                 
            text = content
            myobj = pyttsx3(gender=gender, speed=speed, volume = volume, text=text )
            myobj.save("TextToSpeech/speech.mp3")
            music = 'ok'
            context = {
                'music': music,
            }
            return render(request, 'page2.html', context)
    
        myobj = pyttsx3(gender=gender, speed=speed, volume = volume, text=text )
        myobj.save("TextToSpeech/speech.mp3")
        music = 'ok'
        context = {
            'music': music,
        }
        return render(request, 'page2.html', context)
    
    context = {
        'music': music,
    }
    return render(request, 'page2.html', context)
    

    
   
    

    
         
       
def webpage3(request):
  
      
    return render(request, 'page3.html')

  