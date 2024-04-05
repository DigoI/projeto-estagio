from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth.models import User
from post.models import Post,  Like, Comment
from .serializers import UserSerializer
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.response import Response
from .serializers import UserSerializer, PostSerializer, CommentSerializer, LikeSerializer
from post.forms import ImageUploadForm
from django.contrib.auth import logout
from django.http import JsonResponse
from django.contrib.auth.views import LogoutView, PasswordChangeView, PasswordResetView

class CustomLogoutView(viewsets.ModelViewSet):
    def get_next_page(self):
        # Adicione o redirecionamento personalizado após o logout
        pass

class CustomPasswordChangeView(PasswordChangeView):
    def form_valid(self, form):
        # Lógica adicional após a alteração de senha
        return super().form_valid(form)

class CustomPasswordResetView(PasswordResetView):
    def form_valid(self, form):
        # Lógica adicional após o envio do email de redefinição de senha
        return super().form_valid(form)




class UserRegistrationAPIView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
        

class UserLoginAPIView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer = UserSerializer

 
class PostAPIView(viewsets.ModelViewSet):
        queryset = Post.objects.all()
        serializer = PostSerializer()
    
    

class CommentAPIView(viewsets.ModelViewSet):
        queryset = Comment.objects.all()
        serializer = CommentSerializer()

    

class LikeAPIView(viewsets.ModelViewSet):
        queryset= Like.objects.all()
        serializer = LikeSerializer()


def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image_file = form.cleaned_data['image']
            # Realize a validação adicional do tipo de arquivo aqui, se necessário
            # Salve o arquivo no sistema de arquivos
            with open('caminho/para/salvar/a/imagem/nome_do_arquivo.jpg', 'wb') as f:
                for chunk in image_file.chunks():
                    f.write(chunk)
            return render(request, 'upload_success.html')
    else:
        form = ImageUploadForm()
    return render(request, 'upload_form.html', {'form': form})
