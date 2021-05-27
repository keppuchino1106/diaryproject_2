from django.shortcuts import render, redirect, get_object_or_404
from .models import Diary
from .forms import DiaryForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def cover(request):
    # num = Diary.objects.all().__len__()
    num = Diary.objects.count()
    return render(request, 'cover.html', {'num':num})

@login_required(login_url='/account/login/')
def index(request):
    diaries = Diary.objects.all()
    return render(request, 'index.html', {'diaries':diaries})

@login_required(login_url='/account/login/')
def detail(request, id):
    diary = get_object_or_404(Diary, pk = id)
    return render(request, 'detail.html', {'diary':diary})

@login_required(login_url='/account/login/')
def new(request):
    form = DiaryForm()
    return render(request, 'new.html', {'form':form})

@login_required(login_url='/account/login/')
def create(request):
    form = DiaryForm(request.POST, request.FILES)
    if form.is_valid():
        new_diary = form.save(commit=False)
        new_diary.save()
        return redirect('detail', new_diary.id)
    return redirect('home')

@login_required(login_url='/account/login/')
def edit(request, id):
    edit_diary = Diary.objects.get(id = id)
    return render(request, 'edit.html', {'diary':edit_diary})

@login_required(login_url='/account/login/')
def update(request, id):
    # if request.method == "GET":
        # diary = get_object_or_404(Diary, pk = id)
        # return render(request, "", {"diary": diary})
    update_diary = Diary.objects.get(id = id)
    # update_diary = get_object_or_404(Diary, pk = id)
    update_diary.title = request.POST['title']
    update_diary.body = request.POST['body']
    update_diary.save()
    return redirect('detail', update_diary.id)

@login_required(login_url='/account/login/')
def delete(request, id):
    delete_diary = Diary.objects.get(id = id)
    # delete_diary = get_object_or_404(Diary, pk = id)
    delete_diary.delete()
    return redirect('index')