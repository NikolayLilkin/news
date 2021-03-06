from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView 
from django.core.exceptions import PermissionDenied
from .models import Article
from django.urls import reverse_lazy
class ArticleListView(ListView):
    model=Article
    template_name = 'article_list.html'

class ArticleDetailView(DetailView):
    model=Article
    template_name = 'article_detail.html'

class ArticleDeleteView(LoginRequiredMixin,DeleteView):
    model=Article
    template_name = 'article_delete.html'
    login_url = 'login'
    success_url = reverse_lazy('article_list')

    def dispatch(self, request, *args, **kwargs): 
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

class ArticleUpdateView(LoginRequiredMixin,UpdateView):
    model=Article
    fields = ('title','body')
    template_name = 'article_edit.html'
    login_url = 'login'

class ArticleCreateView(CreateView):
    model=Article
    fields = ('title','body')
    template_name = 'article_new.html'

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ArticleCreateView(LoginRequiredMixin,CreateView):
    model = Article
    template_name = 'article_new.html'
    fields = ('title','body')
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)        