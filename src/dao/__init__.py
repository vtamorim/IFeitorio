from .dao import AbstractDAO
from .alunodao import AlunoDAO
from .cardapiodao import CardapioDAO
from .notificacaodao import NotificacaoDAO
from .restricaodao import RestricaoDAO

# Arquivo que importa todas as outras classes dessa pasta.
# Esse arquivo faz com que a gente tenha que, ao invés de pôr todas essas linhas acima em outros arquivos,
# nós tenhamos que colocar só algo como "from models import Aluno, Avaliacao, ...".
