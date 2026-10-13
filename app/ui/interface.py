from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Input, Button, Static
from app.cadastro_conta import Cadastrar_Conta, ValidarLogin
from textual.containers import Vertical
from app.alterar_dados_da_conta import Alterar_email, Alterar_nome_de_usuario, Alterar_senha
from app.deletar_dados import Deletar_Usuario

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
        width: 60;
        margin: 1 0;
    }

    Button {
        width: 60;
        margin: 1 0;
    }

    Static {
        width: 60;
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
        yield Button("← Voltar", id="voltar")

    def on_button_pressed(self, event):
        if event.button.id == "voltar":
            self.app.pop_screen()
            return

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
            yield Button("Sair", id="sair")

    def on_button_pressed(self, event):
        if event.button.id == 'cadastrar':
            # tela de cadastro
            self.app.push_screen(TelaCadastro())

        elif event.button.id == 'login':
            self.app.push_screen(TelaLogin())

        elif event.button.id == 'alterar':
            self.app.push_screen(TelaAtualizar())

        elif event.button.id == 'remover':
            self.app.push_screen(TelaRemover())
        
        elif event.button.id == 'sair':
            self.app.exit()
            return

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
        yield Button("← Voltar", id="voltar")
        yield Static("", id="mensagem")

    def on_button_pressed(self, event):
        if event.button.id == "voltar":
            self.app.pop_screen()

        elif event.button.id == 'confirmar':
            email = self.query_one("#email", Input).value
            nome = self.query_one("#nome", Input).value
            senha = self.query_one("#senha", Input).value

            sucesso, mensagem = Cadastrar_Conta(
                email, nome, senha
            )

            if sucesso:

                self.app.push_screen(TelaSucesso())
            else:
                self.query_one("#mensagem", Static).update(mensagem)

class TelaLogin(Screen):

    CSS = """
    TelaLogin {
        align: center middle;
    }

    Button {
        width: 50;
        margin-bottom: 1;
    }
    
    """

    def compose(self):
        yield Static("Login")
        yield Input(placeholder="Digite seu email...", id="email")
        yield Input(placeholder="Digite sua senha...", id="senha")
        yield Button("Login", id="logar")
        yield Static("", id="mensagem")
        yield Button("← Voltar", id="voltar")
       

    def on_button_pressed(self, event):
        if event.button.id == "voltar":
            self.app.pop_screen()
            return

        elif event.button.id == "logar":
            email = self.query_one("#email", Input).value
            senha = self.query_one("#senha", Input).value

            sucesso, mensagem = ValidarLogin(email, senha)
        if sucesso:
            self.app.push_screen(TelaCursos())
        else:
            self.query_one("#mensagem", Static).update(mensagem)

class TelaSucesso(Screen):

    CSS = """
    TelaSucesso {
        align: center middle;
    }

    #resultado {
        width: 40;
        height: auto;
        align: center middle;
        margin: 0;
    }

    Button {
        width: 40;
        margin: 1 0;
    }
    """

    def compose(self):
        with Vertical(id="resultado"):
            yield Static("CONTA CADASTRADA COM SUCESSO!")
            yield Static("Agora você já pode explorar os cursos.")
            yield Button("Continuar", id="continuar")

    def on_button_pressed(self, event):
        if event.button.id == "continuar":
            self.app.switch_screen(TelaCursos())    

class TelaAtualizar(Screen):
    CSS = """
    TelaAlterar {
        align: center middle;
    }

    Input {
        width: 100%;
        margin-bottom: 1;
    }

    Button {
        width: 40;
        margin-bottom: 1;
        align: center bottom;
    }

    #mensagem {
        width: 100%;
        text-align: center;
        margin-top: 1;
    }
    """

    def compose(self):
        
        yield Static("ALTERAR DADOS DA CONTA")
        yield Input(
            placeholder="E-mail atual", id="email")
        yield Input(
            placeholder="Nome de usuário atual", id="nome_atual")
        yield Input(
            placeholder="Senha atual",
            password=True,
            id="senha"
        )
        yield Input(placeholder="Digite o novo valor...", id="novo_valor")
        yield Button("Alterar e-mail", id="botao_email")
        yield Button("Alterar nome de usuário", id="botao_nome")
        yield Button("Alterar senha", id="botao_senha")
        yield Button("← Voltar", id="voltar")
        yield Static("", id="mensagem")

    def on_button_pressed(self, event):
        if event.button.id == "voltar":
            self.app.pop_screen()
            return

        email = self.query_one("#email", Input).value.strip()
        nome_atual = self.query_one("#nome_atual", Input).value.strip()
        senha = self.query_one("#senha", Input).value
        novo_valor = self.query_one("#novo_valor", Input).value.strip()

        if event.button.id == "botao_email":
            resultado = Alterar_email(
                email, senha, novo_valor
            )

        elif event.button.id == "botao_nome":
            resultado = Alterar_nome_de_usuario(
                nome_atual, senha, novo_valor
            )

        elif event.button.id == "botao_senha":
            resultado = Alterar_senha(
                email, senha, novo_valor
            )

        else:
            return

        sucesso, mensagem = resultado

        self.query_one("#mensagem", Static).update(mensagem)

class TelaRemover(Screen):
    CSS = """
    TelaRemover {
        align: center middle;
    }

    #conteudo {
        width: 45;
        height: auto;
        padding: 1 2;
    }

    Input {
        margin-bottom: 1;
    }

    Button {
        width: 100%;
        margin-bottom: 1;
    }

    #mensagem {
        margin-top: 1;
        text-align: center;
    }
    """

    def compose(self):
        with Vertical(id="conteudo"):
            yield Static("REMOVER CONTA")
            yield Input(placeholder="Digite seu e-mail...",id="email")
            yield Input(
                placeholder="Digite sua senha",
                password=True,
                id="senha"
            )
            yield Button("Remover conta", id="remover")
            yield Button("← Voltar", id="voltar")
            yield Static("", id="mensagem")

    def on_button_pressed(self, event):
        if event.button.id == "voltar":
            self.app.pop_screen()
            return

        if event.button.id == "remover":
            email = self.query_one("#email", Input).value.strip()
            senha = self.query_one("#senha", Input).value

            sucesso, mensagem = Deletar_Usuario(email, senha)

            self.query_one("#mensagem", Static).update(mensagem)

            if sucesso:
                # Depois de remover, retorna ao menu.
                self.app.switch_screen(TelaMenu())
