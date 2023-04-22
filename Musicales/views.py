from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from Musicales.models import Post, Profile, Mensaje
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

#Para la página principal; index:
def index(request):
    context = {
        "posts": Post.objects.all()
    }
    return render(request, "Musicales/index.html", context)

#CRUD para el modelo Post:
    #Crear el post
class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    success_url = reverse_lazy("post-list")
    fields = ['musical','estreno','descripcion','actor_principal','cancion_principal','duracion','imagen','puntuacion','comentario']

    def form_valid(self, form):
        form.instance.publisher = self.request.user
        return super().form_valid(form)

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
    fields = ['musical','estreno','descripcion','actor_principal','cancion_principal','duracion','imagen','puntuacion','comentario']

    def form_valid(self, form):
        form.instance.publisher = self.request.user
        return super().form_valid(form)

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
    fields = ['instagram','email','imagen']

    def form_valid(self, form):
        form.instance.profile = self.request.user
        return super().form_valid(form)
    
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
        user = self.object
        url = reverse('create-profile', args=[user.id])
        return url

class Login(LoginView):
    next_page = reverse_lazy("index")

class Logout(LogoutView):
    template_name = 'registration/logout.html'

def about(request):
	return render(request, 'Musicales/about.html', context = None)

#CRUD MENSAJES
    #Crear Mensaje
class MensajeCreate(CreateView):
    model = Mensaje
    fields = '__all__'
    success_url = reverse_lazy("index")

    #Ver los mensajes en formato lista
class  MensajeList(LoginRequiredMixin, ListView):
    model = Mensaje
    context_object_name = "mensajes"
    
    def get_queryset(self):
        return Mensaje.objects.filter(destinatario=self.request.user.id).all()
    
    #Borrar el mensaje
class MensajeDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model= Mensaje
    success_url = reverse_lazy("mensaje-list")

    def test_func(self):
        user_id = self.request.user.id
        mensaje_id = self.kwargs.get('pk')
        return Mensaje.objects.filter(destinatario=user_id).exists()

    def handle_no_permission(self):
        return render(self.request, "Musicales/not_found.html")