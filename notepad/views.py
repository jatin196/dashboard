from django.shortcuts import render, redirect, get_object_or_404, reverse
from .models import Note
from .forms import NoteModelForm


# def create_view(request):
# #     form = NoteModelForm(request.POST or None, request.FILES or None)
# #     if request.method == "POST":
# #         if form.is_valid():
# #             form.instance.user = request.user
# #             form.save()
# #             return redirect('/')
# #
# #     context = {
# #         'form': form
# #     }
# #
# #     return render(request, "create.html", context)

def create_view(request):

	form = NoteModelForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		form.instance.user = request.user
		form.save()
		return redirect('/')

	context = {
		'form': form
	}

	return render(request, "create.html", context)


def list_view(request):
    notes = Note.objects.all()
    context = {
        'all_objects' : notes
    }
    return render(request, "list.html", context)

def delete_view(request, id):
    item_to_delete = Note.objects.filter(pk=id)
    if item_to_delete.exists():
        if request.user==item_to_delete[0].user:
            item_to_delete[0].delete()
    return redirect('list')

def update_view(request, id):
    obj = get_object_or_404(Note, id=id)
    form = NoteModelForm(request.POST or None, request.FILES or None, instance=obj)
    if form.is_valid():
        form.instance.user = request.user
        form.save()
        return redirect(reverse('list'))

    context = {
        'form': form
    }

    return render(request, "create.html", context)