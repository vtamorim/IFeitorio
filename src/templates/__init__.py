from .login_ui import LoginUI
from .signin_ui import SigninUI
from .aluno_perfil_ui import AlunoPerfilUI
from .aluno_visualizar_cardapios_ui import AlunoVisualizarCardapiosUI
from .aluno_avaliar_refeicao_ui import AlunoAvaliarRefeicaoUI
from .aluno_visualizar_notificacoes_ui import AlunoVisualizarNotificacoesUI
from .aluno_justificar_ui import AlunoJustificarUI
from .coord_perfil_ui import CoordenadorPerfilUI
from .coord_gerenciar_restricoes_ui import CoordenadorGerenciarRestricoesUI
from .coord_gerenciar_refeicoes_ui import CoordenadorGerenciarRefeicoesUI
from .coord_gerenciar_cardapios_ui import CoordenadorGerenciarCardapiosUI

# Arquivo que importa todas as outras classes dessa pasta.
# Esse arquivo faz com que a gente tenha que, ao invés de pôr todas essas linhas acima em outros arquivos,
# nós tenhamos que colocar só algo como "from templates import LoginUI, ...".
