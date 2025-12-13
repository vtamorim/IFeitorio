from .dao import AbstractDAO
from .alunodao import AlunoDAO
from .refeicaodao import RefeicaoDAO
from .cardapiodao import CardapioDAO
from .coordenadordao import CoordenadorDAO
from .faltadao import FaltaDAO
from .justificativadao import JustificativaDAO
from .notificacaodao import NotificacaoDAO
from .restricaodao import RestricaoDAO
from .avaliacaodao import AvaliacaoDAO

# Arquivo que importa todas as outras classes dessa pasta.
# Esse arquivo faz com que a gente tenha que, ao invés de pôr todas essas linhas acima em outros arquivos,
# nós tenhamos que colocar só algo como "from models import Aluno, Avaliacao, ...".
