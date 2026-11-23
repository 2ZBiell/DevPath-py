from textual.app import App
from app.cadastro_conta import Criar_Tabela, gerenciador_usuarios
from app.ui.interface import TelaMenu
from app.database import gerenciador_cursos
from app.favoritos import gerenciador_favoritos

class MeuApp(App):

    def __init__(self):
        super().__init__()
        self.usuario_atual = None

    def on_mount(self):
        self.push_screen(TelaMenu())

if __name__ == "__main__":
    gerenciador_cursos.tabela_cursos()
    Criar_Tabela()
    gerenciador_usuarios.adicionar_coluna_tipo_usuario()
    gerenciador_favoritos.criar_tabela()
    MeuApp().run()
