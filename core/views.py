from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage

def home(request):
    return render(request, 'home.html')

def login_view(request):
    return render(request, 'login.html')

@login_required
def test_skin(request):
    trial_used = request.session.get('trial_count', 0)
    
    if trial_used >= 3:
        return redirect('trial_ends')

    if request.method == 'POST' and request.FILES.get('image'):
        image = request.FILES['image']
        
        # Save image to media directory
        fs = FileSystemStorage()
        filename = fs.save(image.name, image)
        image_url = fs.url(filename)

        # Increment trial count
        request.session['trial_count'] = trial_used + 1

        # Dummy ML result — replace this with real model later
        prediction = "Melanoma"
        confidence = "94%"

        return render(request, 'test_skin.html', {
            'prediction': {
                'label': prediction,
                'confidence': confidence,
                'image': image_url,
            }
        })

    return render(request, 'test_skin.html')

@login_required
def trial_ends(request):
    return render(request, 'trial_ends.html')

def logout_view(request):
    logout(request)
    return redirect('home')
