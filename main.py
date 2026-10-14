from textual.app import App
from app.cadastro_conta import Criar_Tabela
from app.ui.interface import TelaMenu
from app.database import Tabela_Cursos

class MeuApp(App):
    def on_mount(self):
        self.push_screen(TelaMenu())

if __name__ == "__main__":
    Tabela_Cursos()
    Criar_Tabela()
    MeuApp().run()
