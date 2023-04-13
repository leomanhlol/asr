from django.contrib import messages
from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404, render
from . import asr
from . import convert
from .models import Record
import os 


def record(request):
    if request.method == "POST":
        audio_file = request.FILES.get("recorded_audio")
        language = request.POST.get("language")
        record = Record.objects.create(language=language, voice_record=audio_file)
        record.save()
        messages.success(request, "Audio recording successfully added!")
        return JsonResponse(
            {
                "url": record.get_absolute_url(),
                "success": True,
            }
        )
    context = {"page_title": "Record audio"}
    return render(request, "core/record.html", context)


def record_detail(request, id):
    record = get_object_or_404(Record, id=id)
    path_file = '/home/manhd/django-ajax-record/media/'
    os.chdir(path_file)
    cv = convert.conv(record.voice_record)
    record.language = asr.stt('/home/manhd/django-ajax-record/media/records/audiorecord.wav')
    record.save()
    
    context = {
        "page_title": "Recorded audio detail",
        "record": record,
    }
    return render(request, "core/record_detail.html", context)


def index(request):
    records = Record.objects.all()
    context = {"page_title": "Voice records", "records": records}
    return render(request, "core/index.html", context)






