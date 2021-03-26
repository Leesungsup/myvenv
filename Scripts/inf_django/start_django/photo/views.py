from django.shortcuts import render
from .models import Photo
from django.views.generic.edit import CreateView,DeleteView,UpdateView
from django.shortcuts import redirect
from django.urls import reverse_lazy
# Create your views here.
def photo_list(request):
    #보여줄 사진 데이터
    photos=Photo.objects.all()
    return render(request,'photo/list.html',{'photos':photos})
class PhotoUploadView(CreateView):
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
class PhotoDeleteView(DeleteView):
    model=Photo
    success_url=reverse_lazy('photo_list')
    template_name='photo/delete.html'
class PhotoUpdateView(UpdateView):
    model=Photo
    fields=['photo','text']
    template_name='photo/update.html'
