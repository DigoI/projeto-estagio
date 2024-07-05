# Projeto estagio
Ola! bom dia, boa tarde, boa noite! Este é meu primeiro projeto que faço e confesso que meu deu umas dores de cabeça. O projeto em si trata-se de um framework, programado em Django,
para uma rede socialde compartilhamentos de fotos. Alem disso, o codigo é bem simples e facil de se entender e de manusear. Espero que tenha ficando bom.

## Requisitos

- Python 3.x
- Django 3.x
- Django==5.0.6
- djangorestframework==3.15.2


## Configuração do Ambiente

1. Clone o repositório:
    ```sh
    git clone https://github.com/seu-usuario/seu-repositorio.git
    cd seu-repositorio
    ```

2. ambiente virtual:
    ```sh
    python -m venv projeto
    source projeto/bin/activate  # Para Linux/Mac
    projeto\Scripts\activate  # Para Windows
    ```

3. Instale as dependências:
    ```sh
    pip install -r requirements.txt
    ```

4. Faça as migrações do banco de dados:
    ```sh
    python manage.py makemigrations
    python manage.py migrate
    ```

5. Crie um superusuário:
    ```sh
    python manage.py createsuperuser
    ```

6. Inicie o servidor de desenvolvimento:
    ```sh
    python manage.py runserver
    ```

### Post
```python
class Post(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='Post')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
