# API Books
> API que retorna uma lista de livros, onde permite criar, ler, atualizar e deletar um livro.
> adicionar o autor do livro a partir de uma lista de autores importada de um arquivo csv
> api feita a partir desse desafio https://github.com/olist/work-at-olist

O deploy dessa api está no:
https://apistorebooks.herokuapp.com/

# Funcionalidades da api:
> Ver os detalhes sobre um livro(id, ano de publicação e autor)
> Filtrar livros por nome, ano de publicação e autor

# Instalação 
> pipenv shell
> pipenv -r requirements.txt

# Para importar o arquivo csv com os autores
> python manage.py load -csv authors.csv

# Para rodar a api
> python manage.py runserver


# Frameworks :
* Django  
* Django Rest Framework
* Pandas
  
# Banco de Dados:
* Postgresql

