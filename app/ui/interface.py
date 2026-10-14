from textual.app import ComposeResult
from textual.containers import Vertical, Center
from textual.screen import Screen
from textual.widgets import Input, Button, Static
from app.buscar import BuscarCursos
from app.cadastro_conta import Cadastrar_Conta, ValidarLogin
from textual.containers import Vertical
from app.alterar_dados_da_contav2 import Solicitar_alteracao_email, Confirmar_codigo_email, Confirmar_codigo_senha, Solicitar_alteracao_senha, Alterar_nome_de_usuario
from app.deletar_dados import Deletar_Usuario

# Interface textual para o aplicativo DevPath
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
        yield Static("BUSCAR CURSOS")
        yield Input(placeholder="Digite o nome do curso. . .", id="nome")
        yield Static("", id="resultados") 
        yield Button("Buscar", id="busca")
        yield Button("← Voltar", id="voltar")

    def on_button_pressed(self, event):
        if event.button.id == "voltar":
            self.app.pop_screen()
            return

        if event.button.id == "busca":
            nome = self.query_one("#nome", Input).value.strip()

            resultados = BuscarCursos(nome_do_curso=nome)

            area_resultados = self.query_one("#resultados", Static)

            if resultados:
                texto = "\n\n".join(
                    " | ".join(str(valor) for valor in curso)
                    for curso in resultados
                )

                area_resultados.update(texto)

            else:
                area_resultados.update("Nenhum curso encontrado.")


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
    TelaAtualizar {
        align: center middle;
    }

    #caixa_menu {
        width: 45;
        height: auto;
        align: center middle;
    }

    Button {
        width: 45;
        margin-bottom: 1;
    }

    #titulo {
        width: 45;
        text-align: center;
        text-style: bold;
        margin-bottom: 2;
    }
    """

    def compose(self):
        yield Static("O QUE VOCÊ DESEJA ALTERAR?", id="titulo")
        yield Button("Alterar E-mail", id="nav_email")
        yield Button("Alterar Nome de Usuário", id="nav_nome")
        yield Button("Alterar Senha", id="nav_senha")
        yield Button("← Voltar", id="voltar")

    def on_button_pressed(self, event):
        if event.button.id == "voltar":
            self.app.pop_screen()
            
        elif event.button.id == "nav_email":
            # Abre a tela específica que vai coletar os dados do email
            self.app.push_screen(TelaAlterarEmail())
            
        elif event.button.id == "nav_nome":
            # Abre a tela específica pra o username
            self.app.push_screen(TelaAlterarNome())

        elif event.button.id == "nav_senha":
           # Abre a tela específica da senha
           self.app.push_screen(TelaAlterarSenha())

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

class TelaAlterarEmail(Screen):
    CSS = """
    TelaAlterarEmail {
        align: center middle;
    }

    #caixa_alterar_email {
        width: 45;
        height: auto;
    }

    Input, Button {
        width: 100%;
        margin-bottom: 1;
    }

    #titulo_email, #mensagem_email {
        width: 100%;
        text-align: center;
        margin-bottom: 1;
    }
    """

    def compose(self):
        with Vertical(id="caixa_alterar_email"):
            yield Static("[bold]SOLICITAR ALTERAÇÃO DE E-MAIL[/bold]", markup=True)
        
            # Onde vao ser coletados os dados
            yield Input(placeholder="E-mail atual", id="email_atual")
            yield Input(placeholder="Senha", password=True, id="senha")
            yield Input(placeholder="Novo E-mail desejado", id="novo_email")
        
            yield Button("Solicitar Código", id="btn_solicitar", variant="primary")
            yield Button("← Cancelar", id="btn_cancelar")
        
            yield Static("", id="mensagem_email")

    def on_button_pressed(self, event):
        if event.button.id == "btn_cancelar":
            self.app.pop_screen() # Volta para o menu anterior
            return

        if event.button.id == "btn_solicitar":
            # Extrai os valores que o usuario digitou nos Inputs
            email = self.query_one("#email_atual", Input).value.strip()
            senha = self.query_one("#senha", Input).value
            novo_email = self.query_one("#novo_email", Input).value.strip()

            # Chama a função do backend 
            sucesso, mensagem, user_id = Solicitar_alteracao_email(email, senha, novo_email)

            if sucesso:
                # Se os dados estiverem corretos e o e-mail for enviado, 
                # abre a tela do código e envia o 'user_id'.
                self.app.push_screen(TelaConfirmarEmail(user_id=user_id))
            else:
                # senha errada, e-mail inválido, mostra o erro no ecrã.
                self.query_one("#mensagem_email", Static).update(f"[red]{mensagem}[/red]")

class TelaConfirmarEmail(Screen):
    CSS = """
    TelaConfirmarEmail {
        align: center middle; /* Centraliza o caixote no meio do ecrã */
    }

    #caixa_central {
        width: 45; /* O caixote tem tamanho fixo */
        height: auto;
    }

    Input, Button {
        width: 100%; /* Ocupam todo o espaço do caixote (45), sem ir até à borda do terminal */
        margin-bottom: 1;
    }

    #titulo_codigo, #descricao_codigo, #mensagem_codigo {
        width: 100%;
        text-align: center;
        margin-bottom: 1;
    }
    """

    # O __init__ é obrigatório nesta tela para receber o ID do usuário
    def __init__(self, user_id):
        super().__init__()
        self.user_id = user_id

    def compose(self):
        with Vertical(id="caixa_central"):
            yield Static("[bold]CÓDIGO DE VERIFICAÇÃO[/bold]", markup=True)
            yield Static("Enviamos um código de 6 dígitos para o seu novo e-mail.\nVerifique também a caixa de spam.")
            yield Input(placeholder="Digite o código (Ex: 123456)", id="codigo")
        
            yield Button("Confirmar Alteração", id="btn_confirmar", variant="primary")
            yield Button("← Cancelar", id="btn_cancelar", variant="error")
        
            yield Static("", id="mensagem_codigo")

    def on_button_pressed(self, event):
        if event.button.id == "btn_cancelar":
            self.app.pop_screen() # Cancela e volta para a tela de preencher os dados
            return

        if event.button.id == "btn_confirmar":
            codigo = self.query_one("#codigo", Input).value.strip()
            
            # Chama a função do banco de dados (Etapa 2) passando o ID e o código
            sucesso, mensagem = Confirmar_codigo_email(self.user_id, codigo)

            if sucesso:
                # Se a alteração for feita com sucesso, fechamos as telas de e-mail
                self.app.pop_screen() # Fecha a tela atual (ConfirmarEmail)
                self.app.pop_screen() # Fecha a tela de trás (AlterarEmail)
                
                # Mostra uma mensagem de sucesso na TelaAtualizar (o menu)
                try:
                    self.app.screen.query_one("#titulo", Static).update(f"[green]E-mail alterado com sucesso![/green]")
                except:
                    pass # Evita erro caso o ID #titulo não seja encontrado na tela de baixo
            else:
                # Se o código estiver errado, mostra o erro em vermelho
                self.query_one("#mensagem_codigo", Static).update(f"[red]{mensagem}[/red]")

class TelaAlterarSenha(Screen):
    CSS = """
    TelaAlterarSenha {
        align: center middle;
    }

    #caixa_alterar_senha {
        width: 45;
        height: auto;
    }

    Input, Button {
        width: 100%;
        margin-bottom: 1;
    }

    #titulo_senha, #mensagem_senha {
        width: 100%;
        text-align: center;
        margin-bottom: 1;
    }
    """

    def compose(self):
        with Vertical(id="caixa_alterar_senha"):
            yield Static("[bold]SOLICITAR ALTERAÇÃO DE SENHA[/bold]", id="titulo_senha", markup=True)
            yield Input(placeholder="E-mail atual", id="email_atual")
            yield Input(placeholder="Senha atual", password=True, id="senha_atual")
            yield Input(placeholder="Nova Senha desejada", password=True, id="nova_senha")
            yield Button("Solicitar Código", id="btn_solicitar", variant="primary")
            yield Button("← Cancelar", id="btn_cancelar")
            yield Static("", id="mensagem_senha")

    def on_button_pressed(self, event):
        if event.button.id == "btn_cancelar":
            self.app.pop_screen()
            return

        if event.button.id == "btn_solicitar":
            email = self.query_one("#email_atual", Input).value.strip()
            senha = self.query_one("#senha_atual", Input).value
            nova_senha = self.query_one("#nova_senha", Input).value

            # Chama a função que criámos acima
            sucesso, mensagem, user_id = Solicitar_alteracao_senha(email, senha, nova_senha)

            if sucesso:
                self.app.push_screen(TelaConfirmarSenha(user_id=user_id))
            else:
                self.query_one("#mensagem_senha", Static).update(f"[red]{mensagem}[/red]")

class TelaConfirmarSenha(Screen):


    CSS = """
    TelaConfirmarSenha {
        align: center middle;
    }

    #caixa_confirmar_senha {
        width: 45;
        height: auto;
    }

    Input, Button {
        width: 100%;
        margin-bottom: 1;
    }

    #titulo_codigo_senha, #descricao_codigo_senha, #mensagem_codigo_senha {
        width: 100%;
        text-align: center;
        margin-bottom: 1;
    }
    """

    def __init__(self, user_id):
        super().__init__()
        self.user_id = user_id

    def compose(self):
        with Vertical(id="caixa_confirmar_senha"):
            yield Static("[bold]CÓDIGO DE VERIFICAÇÃO[/bold]", id="titulo_codigo_senha", markup=True)
            yield Static("Enviámos um código de 6 dígitos para o seu e-mail.\nVerifique também a caixa de spam.", id="descricao_codigo_senha")
            yield Input(placeholder="Digite o código (Ex: 123456)", id="codigo")
            yield Button("Confirmar Alteração", id="btn_confirmar", variant="primary")
            yield Button("← Cancelar", id="btn_cancelar", variant="error")
            yield Static("", id="mensagem_codigo_senha")

    def on_button_pressed(self, event):
        if event.button.id == "btn_cancelar":
            self.app.pop_screen()
            return

        if event.button.id == "btn_confirmar":
            codigo = self.query_one("#codigo", Input).value.strip()
            
            sucesso, mensagem = Confirmar_codigo_senha(self.user_id, codigo)

            if sucesso:
                self.app.pop_screen()
                self.app.pop_screen()
                
                try:
                    self.app.screen.query_one("#titulo", Static).update(f"[green]Senha alterada com sucesso![/green]")
                except:
                    pass
            else:
                self.query_one("#mensagem_codigo_senha", Static).update(f"[red]{mensagem}[/red]")

class TelaAlterarNome(Screen):
    CSS = """
    TelaAlterarNome {
        align: center middle;
    }

    #caixa_alterar_nome {
        width: 45;
        height: auto;
    }

    Input, Button {
        width: 100%;
        margin-bottom: 1;
    }

    #titulo_nome, #mensagem_nome {
        width: 100%;
        text-align: center;
        margin-bottom: 1;
    }
    """

    def compose(self):
        with Vertical(id="caixa_alterar_nome"):
            yield Static("[bold]ALTERAR NOME DE USUÁRIO[/bold]", id="titulo_nome", markup=True)
            yield Input(placeholder="Nome de usuário atual", id="nome_atual")
            yield Input(placeholder="Senha", password=True, id="senha")
            yield Input(placeholder="Novo Nome de usuário", id="nome_novo")
            yield Button("Confirmar Alteração", id="btn_confirmar", variant="primary")
            yield Button("← Cancelar", id="btn_cancelar")
            yield Static("", id="mensagem_nome")

    def on_button_pressed(self, event):
        if event.button.id == "btn_cancelar":
            self.app.pop_screen()
            return

        if event.button.id == "btn_confirmar":
            nome_atual = self.query_one("#nome_atual", Input).value.strip()
            senha = self.query_one("#senha", Input).value
            nome_novo = self.query_one("#nome_novo", Input).value.strip()

        
            sucesso, mensagem = Alterar_nome_de_usuario(nome_atual, senha, nome_novo)

            if sucesso:
                self.app.pop_screen() # Fecha a tela e volta pro menu
                
                # Exibe a mensagem de sucesso.
                try:
                    self.app.screen.query_one("#titulo", Static).update(f"[green]{mensagem}[/green]")
                except:
                    pass
            else:
                # Exibe o erro (ex: senha incorreta ou nome já existe)
                self.query_one("#mensagem_nome", Static).update(f"[red]{mensagem}[/red]")
