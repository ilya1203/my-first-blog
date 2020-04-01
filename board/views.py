from django.shortcuts import render

from .models import Rubric, Ccont, VidRubric

def index(request):
    rubr = Rubric.objects.all()
    vr = VidRubric.objects.order_by('-name')
    cont = Ccont.objects.all()
    context = {'rubric': rubr, 'cont': cont, 'vr': vr}
    return render(request, 'board/index.html', context)

def by_rubric(request, rubric_id):
    nns = Ccont.objects.order_by('-published')
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk=rubric_id)
    vr = VidRubric.objects.order_by('-name')
    context = {'nns': nns, 'rubric': rubrics, 'current_rubric': current_rubric, 'vr': vr}
    return render(request, 'board/index.html', context)

def by_vid_rubric(request, rubric_id):
    rubr = Rubric.objects.all()
    vr = VidRubric.objects.order_by('-name')
    cont = Ccont.objects.order_by('-published')
   
    context = {'rubric': rubr,'current_rubric': rubric_id, 'nns': cont, 'vr': vr}
    return render(request, 'board/index.html', context)
