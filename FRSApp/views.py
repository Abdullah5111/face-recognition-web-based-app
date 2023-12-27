from django.shortcuts import render, redirect
from .forms import ImageUploadForm
from .script import identify, know_faces

def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_image = form.save()
            image_name = uploaded_image.image.name   
            return redirect('success', name=identify(image_name))
    else:
        form = ImageUploadForm()
    return render(request, 'upload_image.html', {'form': form})

def success_view(request, name):
    return render(request, 'success.html', {'name': name})