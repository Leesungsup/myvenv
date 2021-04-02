from django.shortcuts import render
from .models import Photo
from django.views.generic.edit import CreateView,DeleteView,UpdateView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
@login_required
def photo_list(request):
    #보여줄 사진 데이터
    photos=Photo.objects.all()
    return render(request,'photo/list.html',{'photos':photos})
class PhotoUploadView(LoginRequiredMixin,CreateView):
    model=Photo
    fields=['photo','text']#작성자,작성시간
    template_name='photo/upload.html'
    def form_valid(self,form):
        form.instance.author_id=self.request.user.id
        if form.is_valid():
            #데이터가 올바르다면 처리
            form.instance.save()
            return redirect('..')
        else:
            return self.render_to_response({'form':form})
class PhotoDeleteView(LoginRequiredMixin,DeleteView):
    model=Photo
    success_url=reverse_lazy('photo_list')
    template_name='photo/delete.html'
class PhotoUpdateView(LoginRequiredMixin,UpdateView):
    model=Photo
    fields=['photo','text']
    template_name='photo/update.html'
