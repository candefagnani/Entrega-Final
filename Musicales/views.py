from django.shortcuts import render
from django.urls import reverse
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from Musicales.models import Post, Profile
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

#Para la página principal; index:
def index(request):
    return render(request, "Musicales/index.html")

#CRUD para el modelo Post:
    #Crear el post
class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    success_url = reverse_lazy("post-list")
    fields = '__all__'

    #Ver en detalle el Post
class PostDetail(DetailView):
    model = Post
 
    #Ver todos los Posts hechos
class PostList(ListView):
    model = Post

    #Modificar el Post
class PostUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    success_url = reverse_lazy("post-list")
    fields = '__all__'

    def test_func(self):
        user_id = self.request.user.id
        post_id = self.kwargs.get('pk')
        return Post.objects.filter(publisher=user_id, id=post_id).exists()

    def handle_no_permission(self):
        return render(self.request, "Musicales/not_found.html")

    #Borrar el Post
class PostDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = reverse_lazy("post-list")

    def test_func(self):
        user_id = self.request.user.id
        post_id = self.kwargs.get('pk')
        return Post.objects.filter(publisher = user_id, id = post_id).exists()

    def handle_no_permission(self):
        return render(self.request, "Musicales/not_found.html")

#CRUD para el modelo Profile 
    #Crear el Perfil
class CreateProfile(CreateView):
    model = Profile
    fields = '__all__'
    
    success_url = reverse_lazy('index')

    #Modificar el Perfil
class ProfileUpdate(UpdateView):
    model = Profile
    fields = '__all__'
    success_url = reverse_lazy('post-list')

    #Detalle del Perfil seleccionado
class ProfileDetail(DetailView):
    model = Profile

class ProfileList(ListView):
    model = Profile
    template_name = 'Musicales/profile_list.html'



#Para crear un Usuario
class SignUp(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    def get_success_url(self):
        # obtiene el usuario recién creado
        user = self.object
        # genera la URL del perfil del usuario recién creado
        url = reverse('create-profile', args=[user.id])
        return url

class Login(LoginView):
    next_page = reverse_lazy("post-list")

class Logout(LogoutView):
    template_name = 'registration/logout.html'