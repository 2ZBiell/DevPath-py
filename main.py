from textual.app import App
from app.cadastro_conta import Criar_Tabela
from app.ui.interface import TelaMenu, TelaCursos

class MeuApp(App):
    def on_mount(self):
        self.push_screen(TelaMenu())

if __name__ == "__main__":
    Criar_Tabela()
    MeuApp().run()
