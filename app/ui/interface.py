from textual.screen import Screen
from textual.widgets import Input, Button, Static, OptionList
from textual.widgets.option_list import Option
from textual.containers import Vertical

from app.cadastro_conta import Cadastrar_Conta, ValidarLogin
from app.alterar_dados_da_contav2 import (
    Solicitar_alteracao_email,
    Confirmar_codigo_email,
    Alterar_nome_de_usuario,
    Solicitar_alteracao_senha,
    Confirmar_codigo_senha,
)
from app.deletar_dados import Deletar_Usuario
from app.buscar import busca_cursos


CSS_COMUM = """\nScreen {
    align: center middle;
}


#detalhes,
#caixa_menu,
#caixa_alterar_email,
#caixa_central {
    width: 70;
    height: auto;
    padding: 2;
    border: round cyan;
}


Input,
Button {
    width: 100%;
    margin-bottom: 1;
}


#titulo,
#titulo_email,
#titulo_codigo,
#titulo_senha,
#titulo_nome,
#titulo_codigo_senha {
    width: 100%;
    text-align: center;
    margin: 1 0;
}


#mensagem,
#mensagem_email,
#mensagem_codigo,
#mensagem_senha,
#mensagem_nome,
#mensagem_codigo_senha {
    width: 100%;
    text-align: center;
    margin-bottom: 1;
}
"""


class TelaCursos(Screen):
    CSS = CSS_COMUM + """
    #titulo {
        margin: 1 0;
    }

    Input,
    Button {
        margin: 1 0;
    }
    """

    def compose(self):
        with Vertical(id="detalhes"):
            yield Static("BUSCAR CURSOS", id="titulo")
            yield Input(placeholder="Digite o nome do curso...", id="nome")
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
            resultados = busca_cursos.buscar(nome_do_curso=nome)

            lista = self.query_one("#resultados", OptionList)
            mensagem = self.query_one("#mensagem", Static)
            lista.clear_options()
            self.cursos = resultados

            if resultados:
                for curso in resultados:
                    nome_curso = curso[1]
                    plataforma = curso[2]
                    lista.add_option(Option(f"{nome_curso} | {plataforma}", id=str(curso[0])))
                mensagem.update("Selecione um curso e aperte Enter.")
            else:
                mensagem.update("Nenhum curso encontrado.")

    def on_option_list_option_selected(self, event: OptionList.OptionSelected):
        curso_id = int(event.option.id)
        for curso in self.cursos:
            if curso[0] == curso_id:
                self.app.push_screen(TelaDetalhesCurso(curso))
                break


class TelaMenu(Screen):
    CSS = CSS_COMUM + """
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
            yield Static("[bold #00D9FF]◆ Dev[/][bold white]Path ◆[/]", id="devpath", markup=True)
            yield Button("Cadastrar usuário", id="cadastrar")
            yield Button("Login", id="login")
            yield Button("Alterar dados", id="alterar")
            yield Button("Remover Usuário", id="remover")
            yield Button("Sair", id="sair")

    def on_button_pressed(self, event):
        if event.button.id == "cadastrar":
            self.app.push_screen(TelaCadastro())
        elif event.button.id == "login":
            self.app.push_screen(TelaLogin())
        elif event.button.id == "alterar":
            self.app.push_screen(TelaAtualizar())
        elif event.button.id == "remover":
            self.app.push_screen(TelaRemover())
        elif event.button.id == "sair":
            self.app.exit()


class TelaCadastro(Screen):
    def compose(self):
        with Vertical(id="detalhes"):
            yield Static("Cadastro do usuário", id="titulo")
            yield Input(placeholder="Digite o seu e-mail...", id="email")
            yield Input(placeholder="Digite o seu nome de usuário...", id="nome")
            yield Input(placeholder="Digite a sua senha...", password=True, id="senha")
            yield Button("Cadastrar", id="confirmar")
            yield Button("← Voltar", id="voltar")
            yield Static("", id="mensagem")

    def on_button_pressed(self, event):
        if event.button.id == "voltar":
            self.app.pop_screen()
            return

        if event.button.id == "confirmar":
            email = self.query_one("#email", Input).value.strip()
            nome = self.query_one("#nome", Input).value.strip()
            senha = self.query_one("#senha", Input).value
            sucesso, mensagem = Cadastrar_Conta(email, nome, senha)

            if sucesso:
                self.app.push_screen(TelaSucesso())
            else:
                self.query_one("#mensagem", Static).update(mensagem)


class TelaLogin(Screen):
    def compose(self):
        with Vertical(id="detalhes"):
            yield Static("Login", id="titulo")
            yield Input(placeholder="Digite seu email...", id="email")
            yield Input(placeholder="Digite sua senha...", password=True, id="senha")
            yield Button("Login", id="logar")
            yield Static("", id="mensagem")
            yield Button("← Voltar", id="voltar")

    def on_button_pressed(self, event):
        if event.button.id == "voltar":
            self.app.pop_screen()
            return

        if event.button.id == "logar":
            email = self.query_one("#email", Input).value.strip()
            senha = self.query_one("#senha", Input).value
            sucesso, mensagem = ValidarLogin(email, senha)

            if sucesso:
                self.app.push_screen(TelaCursos())
            else:
                self.query_one("#mensagem", Static).update(mensagem)


class TelaSucesso(Screen):
    CSS = CSS_COMUM + """
    #resultado {
        width: 40;
        height: auto;
        align: center middle;
        margin: 0;
    }
    #resultado > Button {
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
    CSS = CSS_COMUM + """
    #caixa_menu {
        align: center middle;
    }
    #titulo {
        text-style: bold;
        margin-bottom: 2;
    }
    """

    def compose(self):
        with Vertical(id="caixa_menu"):
            yield Static("O QUE VOCÊ DESEJA ALTERAR?", id="titulo")
            yield Button("Alterar E-mail", id="nav_email")
            yield Button("Alterar Nome de Usuário", id="nav_nome")
            yield Button("Alterar Senha", id="nav_senha")
            yield Button("← Voltar", id="voltar")

    def on_button_pressed(self, event):
        if event.button.id == "voltar":
            self.app.pop_screen()
        elif event.button.id == "nav_email":
            self.app.push_screen(TelaAlterarEmail())
        elif event.button.id == "nav_nome":
            self.app.push_screen(TelaAlterarNome())
        elif event.button.id == "nav_senha":
            self.app.push_screen(TelaAlterarSenha())


class TelaRemover(Screen):
    def compose(self):
        with Vertical(id="detalhes"):
            yield Static("Remover conta", id="titulo")
            yield Input(placeholder="Digite seu e-mail...", id="email")
            yield Input(placeholder="Digite sua senha", password=True, id="senha")
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
                self.app.switch_screen(TelaMenu())


class TelaDetalhesCurso(Screen):
    CSS = CSS_COMUM + """
    Button {
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
            yield Static(f"[bold]{curso[1]}[/]", markup=True)
            yield Static(f"Plataforma: {curso[2]}")
            yield Static(f"Linguagem: {curso[3]}")
            yield Static(f"Gratuito: {gratuito}")
            yield Static(f"\nDescrição:\n{curso[4]}")
            yield Button("← Voltar aos resultados", id="voltar")

    def on_button_pressed(self, event):
        if event.button.id == "voltar":
            self.app.pop_screen()


class TelaAlterarEmail(Screen):
    def compose(self):
        with Vertical(id="caixa_alterar_email"):
            yield Static("[bold]SOLICITAR ALTERAÇÃO DE E-MAIL[/bold]", id="titulo", markup=True)
            yield Input(placeholder="E-mail atual", id="email_atual")
            yield Input(placeholder="Senha", password=True, id="senha")
            yield Input(placeholder="Novo E-mail desejado", id="novo_email")
            yield Button("Solicitar Código", id="btn_solicitar", variant="primary")
            yield Button("← Cancelar", id="btn_cancelar")
            yield Static("", id="mensagem_email")

    def on_button_pressed(self, event):
        if event.button.id == "btn_cancelar":
            self.app.pop_screen()
            return


        if event.button.id == "btn_solicitar":
            email = self.query_one("#email_atual", Input).value.strip()
            senha = self.query_one("#senha", Input).value
            novo_email = self.query_one("#novo_email", Input).value.strip()
            sucesso, mensagem, user_id = Solicitar_alteracao_email(email, senha, novo_email)


            if sucesso:
                self.app.push_screen(TelaConfirmarEmail(user_id=user_id))
            else:
                self.query_one("#mensagem_email", Static).update(f"[red]{mensagem}[/red]")


class TelaConfirmarEmail(Screen):
    CSS = CSS_COMUM + """
    #descricao_codigo {
        width: 100%;
        text-align: center;
        margin-bottom: 1;
    }
    """

    def __init__(self, user_id):
        super().__init__()
        self.user_id = user_id



    def compose(self):
        with Vertical(id="caixa_central"):
            yield Static("[bold]CÓDIGO DE VERIFICAÇÃO[/bold]", id="titulo", markup=True)
            yield Static("Enviamos um código de 6 dígitos para o seu novo e-mail.\nVerifique também a caixa de spam.", id="descricao_codigo")
            yield Input(placeholder="Digite o código (Ex: 123456)", id="codigo")
            yield Button("Confirmar Alteração", id="btn_confirmar", variant="primary")
            yield Button("← Cancelar", id="btn_cancelar", variant="error")
            yield Static("", id="mensagem_codigo")

    def on_button_pressed(self, event):
        if event.button.id == "btn_cancelar":
            self.app.pop_screen()
            return


        if event.button.id == "btn_confirmar":
            codigo = self.query_one("#codigo", Input).value.strip()
            sucesso, mensagem = Confirmar_codigo_email(self.user_id, codigo)


            if sucesso:
                self.app.pop_screen()
                self.app.pop_screen()
                try:
                    self.app.screen.query_one("#titulo", Static).update("[green]E-mail alterado com sucesso![/green]")
                except Exception:
                    pass
            else:
                self.query_one("#mensagem_codigo", Static).update(f"[red]{mensagem}[/red]")


class TelaAlterarSenha(Screen):
    def compose(self):
        with Vertical(id="caixa_central"):
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
            sucesso, mensagem, user_id = Solicitar_alteracao_senha(email, senha, nova_senha)

            if sucesso:
                self.app.push_screen(TelaConfirmarSenha(user_id=user_id))
            else:
                self.query_one("#mensagem_senha", Static).update(f"[red]{mensagem}[/red]")


class TelaConfirmarSenha(Screen):
    def __init__(self, user_id):
        super().__init__()
        self.user_id = user_id



    def compose(self):
        with Vertical(id="caixa_central"):
            yield Static("[bold]CÓDIGO DE VERIFICAÇÃO[/bold]", id="titulo_codigo_senha", markup=True)
            yield Static("Enviamos um código de 6 dígitos para o seu e-mail.\nVerifique também a caixa de spam.", id="descricao_codigo_senha")
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
                    self.app.screen.query_one("#titulo", Static).update("[green]Senha alterada com sucesso![/green]")
                except Exception:
                    pass
            else:
                self.query_one("#mensagem_codigo_senha", Static).update(f"[red]{mensagem}[/red]")


class TelaAlterarNome(Screen):
    def compose(self):
        with Vertical(id="caixa_central"):
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
                self.app.pop_screen()
                try:
                    self.app.screen.query_one("#titulo", Static).update(f"[green]{mensagem}[/green]")
                except Exception:
                    pass
            else:
                self.query_one("#mensagem_nome", Static).update(f"[red]{mensagem}[/red]")
