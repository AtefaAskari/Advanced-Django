from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from .forms import ProfileForm 
from .models import Profile 
import pdfkit

def home(request):
    return render(request, 'home.html')


def submit_cv(request):
    form = ProfileForm(request.POST or None, request.FILES or None)
    if request.method == 'POST' and form.is_valid():
        profile = form.save()
        return redirect('cv_page', id=profile.id)
    return render(request, 'add_cv.html', {'form': form})


def CV(request, id):
    profile = get_object_or_404(Profile, pk=id)
    context = {'profile': profile}
    return render(request, 'cv_template.html', context)


def CV_list(request):
    profiles = Profile.objects.order_by('-id')  # Ensuring the latest CV appears first
    return render(request, 'resume_list.html', {'profiles': profiles})


def download_CV(request, id):
    profile = get_object_or_404(Profile, pk=id)
    template = loader.get_template('cv_template.html')
    html = template.render({'profile': profile, 'print': True})
    options = {
        'page-size': 'A4',  # Changed to A4 for standard CV format
        'encoding': 'UTF-8',
        'quiet': ''  # Suppresses warnings from pdfkit
    }
    try:
        pdf = pdfkit.from_string(html, False, options)
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="{profile.full_name.replace(" ", "_")}_CV.pdf"'
        return response
    except Exception as e:
        return HttpResponse(f"Error generating PDF: {str(e)}", status=500)


def delete_cv(request, id):
    cv = get_object_or_404(Profile, id=id)
    if request.method == 'POST':
        cv.delete()
        return redirect('cv_list')
    return render(request, 'cv_confirm_delete.html', {'cv': cv})

