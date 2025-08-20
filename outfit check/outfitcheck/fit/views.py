from .forms import OutfitForm
from .models import Outfit
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .outfit_ai import rate_outfit
from .models import Outfit
from .clip_analysis import rate_outfit_clip  
from .models import Outfit
from django.shortcuts import render, get_object_or_404
from .models import Outfit  
from .clip_analysis import rate_outfit_clip  
from django.shortcuts import render, get_object_or_404
from .models import Outfit
from .clip_analysis import rate_outfit_clip
from django.contrib.auth.decorators import login_required
from .models import Outfit
from django.shortcuts import get_object_or_404, redirect
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Outfit


@login_required
def delete_outfit(request, outfit_id):
    
    outfit = get_object_or_404(Outfit, id=outfit_id, user=request.user)

    if request.method == 'POST':
        outfit.delete()
        return redirect('dashboard') 
    return redirect('dashboard')







def style_gallery_view(request):
    outfits = Outfit.objects.all()
    return render(request, 'gallery.html', {'outfits': outfits})



def outfit_result_view(request, outfit_id):
    try:
        outfit = get_object_or_404(Outfit, id=outfit_id)

        if not outfit.image:
            return render(request, 'outfit/result.html', {
                'outfit': None,
                'score': 0,
                'reasons': {
                    'Color': 'No image found.',
                    'Fit': 'No image to evaluate.',
                    'Trend': 'No image provided.'
                },
                'suggestions': ['Please upload a valid outfit image.']
            })

        image_path = outfit.image.path

       
        score, reasons, suggestions = rate_outfit_clip(image_path)

        return render(request, 'outfit/result.html', {
            'outfit': outfit,
            'score': score,
            'reasons': reasons,
            'suggestions': suggestions
        })

    except Exception as e:
        return render(request, 'outfit/result.html', {
            'outfit': None,
            'score': 0,
            'reasons': {
                'Color': 'Error analyzing image.',
                'Fit': 'Something went wrong during analysis.',
                'Trend': 'AI failed to evaluate.'
            },
            'suggestions': [
                'Try uploading a different image.',
                f'Error message: {str(e)}'
            ]
        })



def outfit_result(request, outfit_id):
    outfit = Outfit.objects.get(id=outfit_id)
    image_path = outfit.image.path

    score, reasons, suggestions = rate_outfit_clip(image_path)

    return render(request, 'outfitcheck/result.html', {
        'outfit': outfit,
        'score': score,
        'reasons': reasons,
        'suggestions': suggestions
    })



def outfit_result(request, outfit_id):
    outfit = Outfit.objects.get(id=outfit_id)
    image_path = outfit.image.path

    score, reasons, suggestions = rate_outfit(image_path)

    context = {
        'outfit': outfit,
        'score': score,
        'reasons': reasons,
        'suggestions': suggestions
    }
    return render(request, 'outfitcheck/result.html', context)


def home_view(request):
    return render(request, 'home.html')


def about_view(request):
    return render(request, 'about.html')


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


@login_required
def dashboard_view(request):
    outfits = request.user.outfit_set.all()
    return render(request, 'dashboard.html', {'outfits': outfits})


@login_required
def upload_outfit(request):
    if request.method == 'POST':
        form = OutfitForm(request.POST, request.FILES)
        if form.is_valid():
            outfit = form.save(commit=False)
            outfit.user = request.user  # ✅ This is the fix!
            outfit.save()
            return redirect('dashboard')
    else:
        form = OutfitForm()
    return render(request, 'upload.html', {'form': form})


def outfit_list(request):
    outfits = Outfit.objects.order_by('-uploaded_at')
    return render(request, 'list.html', {'outfits': outfits})


def gallery_view(request):
    outfits = Outfit.objects.all().order_by('-id')
    return render(request, 'gallery.html', {'outfits': outfits})


# @login_required
# def delete_outfit(request, pk):
#     outfit = get_object_or_404(Outfit, pk=pk)
#     if request.method == 'POST':
#         outfit.delete()
#         return redirect('dashboard')
