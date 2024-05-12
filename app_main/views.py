from django.utils import timezone
from django.shortcuts import render, redirect, get_object_or_404
from .models import Note
from .forms import NoteForm

def home_page(request):
    if not request.user.is_authenticated:
        return redirect('login')

    full_name = request.user.get_full_name()

    notes = Note.objects.filter(owner=request.user)

    context = {
        "full_name": full_name,
        "notes": notes,
    }

    return render(request, 'app_main/home.html', context)


def create_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.owner = request.user
            note.save()
            return redirect('home')
    else:
        form = NoteForm()
    return render(request, 'app_main/create_note.html', {'form': form})



def edit_note(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            note = form.save(commit=False)
            note.updated = timezone.now()
            note.save()
            print("Note updated successfully:", note.updated)
            return redirect('home')
    else:
        form = NoteForm(instance=note)
    return render(request, 'app_main/edit_note.html', {'form': form})




def delete_note(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    if request.method == 'POST':
        note.delete()
    return redirect('home')
