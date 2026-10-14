from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Input, Button, Static, OptionList
from textual.widgets.option_list import Option
from app.buscar import BuscarCursos
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

    #titulo {
        width: 100%;
        text-align: center;
        margin: 1 0;
    }

    #detalhes {
        width: 70;
        height: auto;
        padding: 2;
        border: round cyan;
    }

    Input {
        width: 100%;
        margin: 1 0;
    }

    Button {
        width: 100%;
        margin: 1 0;
    }
    """

    def compose(self):
        with Vertical(id="detalhes"):
            yield Static("BUSCAR CURSOS", id="titulo")
            yield Input(placeholder="Digite o nome do curso. . .", id="nome")
            yield Button("Buscar", id="busca")
            yield Static("", id="mensagem")
            yield OptionList(id="resultados")
            yield Button("← Voltar", id="voltar")

    def on_button_pressed(self, event):
        if event.button.id == "voltar":
            self.app.pop_screen()
            return

        if event.button.id == "busca":
            nome = self.query_one("#nome", Input).value.strip()

            resultados = BuscarCursos(nome_do_curso=nome)

            lista = self.query_one("#resultados", OptionList)
            mensagem = self.query_one("#mensagem", Static)

            lista.clear_options()
            self.cursos = resultados

            if resultados:
                for curso in resultados:
                    nome_curso = curso[1]
                    plataforma = curso[2]

                    lista.add_option(
                        Option(
                            f"{nome_curso} | {plataforma}",
                            id=str(curso[0])
                        )
                    )

                mensagem.update("Selecione um curso e aperte Enter.")

            else:
                mensagem.update("Nenhum curso encontrado.")

    def on_option_list_option_selected(
        self, event: OptionList.OptionSelected
    ):
        curso_id = int(event.option.id)

        for curso in self.cursos:
            if curso[0] == curso_id:
                self.app.push_screen(
                    TelaDetalhesCurso(curso)
                )
                break

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

    #titulo {
        width: 100%;
        text-align: center;
        margin: 1 0;
    }

    #detalhes {
        width: 70;
        height: auto;
        padding: 2;
        border: round cyan;
    }

    Input {
        width: 100%;
        margin: 1 0;
    }

    Button {
        width: 100%;
        margin: 1 0;
    }
    """

    def compose(self):
        with Vertical(id="detalhes"):
            yield Static("Cadastro do usuário", id="titulo")
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

    #detalhes {
        width: 70;
        height: auto;
        padding: 2;
        border: round cyan;
    }


    #titulo {
        width: 100%;
        text-align: center;
        text-style: bold;
        margin-bottom: 2;
    }

    Input {
        width: 100%;
        margin-bottom: 1;
    }

    Button {
        width: 100%;
        margin-bottom: 1;
        align: center middle;
    }

    #mensagem {
        width: 100%;
        text-align: center;
        margin-bottom: 1;
    }
    """

    def compose(self):
        with Vertical(id="detalhes"):
            yield Static("Login", id="titulo")
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
    TelaAtualizar {
        align: center middle;
    }

    #titulo {
        width: 100%;
        text-align: center;
        margin: 1 0;
    }

    #detalhes {
        width: 70;
        padding: 2;
        height: auto;
        border: round cyan;
    }

    Input {
        width: 100%;
        margin-bottom: 1;
        align: center middle;
    }

    Button {
        width: 100%;
        margin-bottom: 1;
        align: center middle;
    }

    #mensagem {
        width: 100%;
        text-align: center;
        margin-top: 1;
    }
    """

    def compose(self):
        with Vertical(id="detalhes"):
            yield Static("Alterar dados da conta", id="titulo")
            yield Input(placeholder="E-mail atual", id="email")
            yield Input(placeholder="Nome de usuário atual", id="nome_atual")
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

    #titulo {
        width: 100%;
        text-align: center;
        margin: 1 0;
    }

    #detalhes {
        width: 70;
        height: auto;
        padding: 2;
        border: round cyan;
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
        with Vertical(id="detalhes"):
            yield Static("Remover conta", id="titulo")
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

class TelaDetalhesCurso(Screen):

    CSS = """
    TelaDetalhesCurso {
        align: center middle;
    }

    #detalhes {
        width: 70;
        height: auto;
        padding: 2;
        border: round cyan;
    }

    Button {
        width: 100%;
        margin-top: 1;
    }
    """

    def __init__(self, curso):
        super().__init__()
        self.curso = curso

    def compose(self):
        curso = self.curso

        gratuito = "Sim" if curso[5] else "Não"

        with Vertical(id="detalhes"):
            yield Static(
                f"[bold]{curso[1]}[/]",
                markup=True
            )
            yield Static(f"Plataforma: {curso[2]}")
            yield Static(f"Linguagem: {curso[3]}")
            yield Static(f"Gratuito: {gratuito}")
            yield Static(f"\nDescrição:\n{curso[4]}")
            yield Button("← Voltar aos resultados", id="voltar")

    def on_button_pressed(self, event):
        if event.button.id == "voltar":
            self.app.pop_screen()
