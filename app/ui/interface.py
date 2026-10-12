from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Input, Button, Static
from app.cadastro_conta import Cadastrar_Conta, ValidarLogin
from textual.containers import Vertical

# widgets: Input, Select, Button, DataTable, etc
# queryone
# compose()
# Todo aplicativo textual geralmente é uma calsse que herda de App

# a ideia é ter uma tela para cada ação no menu principal
# menu - cadastro/ login/ alterar dados/ remover usuario
# obs: quando o cadastro for feito libera o acesso a buscar cursos

class TelaCursos(Screen):

    CSS = """
    TelaCursos {
        align: center middle;
    }

    Input {
        width: 40;
        margin: 1 0;
    }

    Button {
        width: 40;
        margin: 1 0;
    }

    Static {
        width: 40;
        text-align: center;
        margin: 1 0;
    }
    """

    def compose(self):
        yield Input(
            placeholder="Digite o nome do curso. . .",
            id="nome"
        ) 

        yield Button("Buscar", id="busca")

class TelaMenu(Screen):

    CSS = """
    TelaMenu {
        align: center middle;
    }

    #botoes {
        width: 40;
        height: auto;
        align: center middle;
        margin: 0;
    }

    #devpath {
        width: 100%;
        height: 3;
        text-align: center;
        content-align: center middle;
        text-style: bold;
        margin-bottom: 1;

    }

    #botoes > Button {
        width: 40;
        margin: 1 0;
    }
"""


    def compose(self):
        with Vertical(id="botoes"):
            yield Static(
                "[bold #00D9FF]◆ Dev[/][bold white]Path ◆[/]",
                id="devpath",
                markup=True
            )
            yield Button("Cadastrar usuário", id="cadastrar")
            yield Button("Login", id="login")
            yield Button("Alterar dados", id="alterar")
            yield Button("Remover Usuário", id="remover")

    def on_button_pressed(self, event):
        if event.button.id == 'cadastrar':
            # tela de cadastro
            self.app.push_screen(TelaCadastro())

        elif event.button.id == 'login':
            print('login')

        elif event.button.id == 'alterar':
            print('alterar dados')

        elif event.button.id == 'remover':
            print('remover usuario') 


class TelaCadastro(Screen):

    CSS = """
    TelaCadastro {
        align: center middle;
    }

    Input {
        width: 40;
        margin: 1 0;
    }

    Button {
        width: 40;
        margin: 1 0;
    }

    Static {
        width: 40;
        text-align: center;
        margin: 1 0;
    }
    """

    def compose(self):
        yield Static("Cadastro do usuário")
        yield Input(placeholder="Digite o seu e-mail...", id="email")
        yield Input(placeholder="Digite o seu nome de usuário...", id="nome")
        yield Input(
            placeholder="Digite a sua senha...",
            password=True,
            id="senha"
        )
        yield Button("Cadastrar", id="confirmar")
        yield Static("", id="mensagem")

    def on_button_pressed(self, event):
        if event.button.id == 'confirmar':
            nome = self.query_one("#email", Input).value
            email = self.query_one("#nome", Input).value
            senha = self.query_one("#senha", Input).value

            sucesso, mensagem = Cadastrar_Conta(
                email, nome, senha
            )

            if sucesso:

                self.app.push_screen(TelaSucesso())
            else:
                self.query_one("#mensagem", Static).update(mensagem)

class TelaLogin(Screen):
    def compose(self):
        yield Static("Login")
        yield Input(placeholder="Digite seu nome de usuário...", id="nome")
        yield Input(placeholder="Digite sua senha...", id="senha")
        yield Button("Login", id="logar")

    def on_button_pressed(self, event):
        if event.button.id == "logar":
            email = self.query_one("#nome", Input).value
            senha = self.query_one("#senha", Input).value

            sucesso, mensagem = ValidarLogin(nome, senha)
        if sucesso:
            self.app.push_screen(TelaCursos)
        else:
            self.query_one("#mensagem", Static).update(mensagem)

class TelaSucesso(Screen):

    CSS = """
    TelaSucesso {
        align: center middle;
    }

    Static {
        text-align: center;
        margin: 1 0;
    }
    """

    def compose(self):
        yield Static("CONTA CADASTRADA COM SUCESSO!")
        yield Static("Agora você já pode explorar os cursos.")
        yield Button("Continuar", id="continuar")

    def on_button_pressed(self, event):
        if event.button.id == "continuar":
            self.app.switch_screen(TelaCursos())    
