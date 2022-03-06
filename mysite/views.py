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
      def webpage3(request):
     if request.method == 'POST':
         audio = request.POST.get('audio')
         video = request.POST.get('video')
         compress= request.POST.get('compress')
         background_audio_clip = AudioFileClip(audio)
         final_clip = video.set_audio(background_audio_clip)
         final_clip.write_videofile(final_video_path, codec='libx264', audio_codec="aac")
         if compress =='YES':
             def compress_video( output_file_name, target_size):
                  # Reference: https://en.wikipedia.org/wiki/Bit_rate#Encoding_bit_rate
    min_audio_bitrate = 32000
    max_audio_bitrate = 256000

    probe = ffmpeg.probe(video_full_path)
    # Video duration, in s.
    duration = float(probe['format']['duration'])
    # Audio bitrate, in bps.
    audio_bitrate = float(next((s for s in probe['streams'] if s['codec_type'] == 'audio'), None)['bit_rate'])
    # Target total bitrate, in bps.
    target_total_bitrate = (target_size * 1024 * 8) / (1.073741824 * duration)

    # Target audio bitrate, in bps
    if 10 * audio_bitrate > target_total_bitrate:
        audio_bitrate = target_total_bitrate / 10
        if audio_bitrate < min_audio_bitrate < target_total_bitrate:
            audio_bitrate = min_audio_bitrate
        elif audio_bitrate > max_audio_bitrate:
            audio_bitrate = max_audio_bitrate
    # Target video bitrate, in bps.
    video_bitrate = target_total_bitrate - audio_bitrate

    i = ffmpeg.input(video_full_path)
    ffmpeg.output(i, os.devnull,
                  **{'c:v': 'libx264', 'b:v': video_bitrate, 'pass': 1, 'f': 'mp4'}
                  ).overwrite_output().run()
    ffmpeg.output(i, output_file_name,
                  **{'c:v': 'libx264', 'b:v': video_bitrate, 'pass': 2, 'c:a': 'aac', 'b:a': audio_bitrate}
                  ).overwrite_output().run()

compress_video( 'output.mp4', 50 * 1000)
   
  
      
    return render(request, 'page3.html')

  
