from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Input, Button, Static, OptionList, Select
from textual.widgets.option_list import Option
from app.cadastro_conta import Cadastrar_Conta, ValidarLogin, gerenciador_usuarios
from textual.containers import Vertical, Center
from app.alterar_dados_da_contav2 import Solicitar_alteracao_email, Confirmar_codigo_email, Alterar_nome_de_usuario, Solicitar_alteracao_senha, Confirmar_codigo_senha
from app.deletar_dados import Deletar_Usuario
from app.buscar import busca_cursos
from app.favoritos import gerenciador_favoritos
from app.database import gerenciador_cursos


# widgets: Input, Select, Button, DataTable, etc
# queryone
# compose()
# Todo aplicativo textual geralmente é uma calsse que herda de App

# a ideia é ter uma tela para cada ação no menu principal
# menu - cadastro/ login/ alterar dados/ remover usuario
# obs: quando o cadastro for feito libera o acesso a buscar cursos

CSS_COMUM = """
TelaCursos,
TelaMenu,
TelaCadastro,
TelaLogin,
TelaSucesso,
TelaAtualizar,
TelaRemover,
TelaDetalhesCurso,
TelaAlterarEmail,
TelaConfirmarEmail,
TelaAlterarSenha,
TelaConfirmarSenha,
TelaAlterarNome,
TelaPainelAdmin,
TelaFavoritos,
TelaGerenciarCursos, {
    align: center middle;
    }

/* Caixas principais */
#detalhes,
#caixa_menu,
#caixa_alterar_email,
#caixa_central {
    width: 70;
    height: auto;
    padding: 2;
    border: round cyan;
}

/* Campos e botões */
Input,
Button {
    align: center middle;
    width: 100%;
    margin-bottom: 1;
}

/* Títulos */
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

/* Mensagens */
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

    #titulo_preco {
        margin-top: 1;
        margin-bottom: 0;
        text-style: bold;
    }

    """

    def compose(self):
        with Vertical(id="detalhes"):
            yield Static("BUSCAR CURSOS", id="titulo")
            yield Input(placeholder="Digite o nome do curso...",id="nome")

            yield Select(
                [
                    ("Todas as plataformas", ""),
                    ("Curso em Vídeo", "Curso em Vídeo"),
                    ("freeCodeCamp", "freeCodeCamp"),
                    ("Corujinhas", "Corujinhas"),
                    ("CURSA", "CURSA"),
                    ("EV.G", "EV.G"),
                    ("IFRS", "IFRS")
                ],
                prompt="Selecione a plataforma",
                value="",
                id="plataforma"
            )

            yield Select(
                [
                    ("Todas as tecnologias", ""),
                    ("Python", "Python"),
                    ("C++", "C++"),
                    ("Java", "Java"),
                    ("JavaScript", "JavaScript"),
                    ("PHP", "PHP"),
                    ("HTML e CSS", "HTML e CSS"),
                    ("Git", "Git"),
                    ("GitHub", "GitHub"),
                    ("SQL", "SQL"),
                    ("Banco de Dados", "Banco de Dados"),
                    ("Lógica de Programação", "Lógica de Programação"),
                    ("Desenvolvimento Web", "Desenvolvimento Web"),
                    ("Informática", "Informática"),
                    ("Ciência de Dados", "Ciência de Dados"),
                    ("Inteligência Artificial", "Inteligência Artificial")
                ],
                prompt="Selecione a tecnologia",
                value="",
                id="linguagem"
            )

            yield Select(
                [
                    ("Todos os preços", "todos"),
                    ("Gratuitos", "gratuito"),
                    ("Pagos", "pago")
                ],
                prompt="Selecione o preço",
                value="todos",
                id="gratuito"
            )

            yield Button("Buscar", id="busca")
            yield Button("Limpar filtros", id="limpar")
            yield Static("", id="mensagem")
            yield OptionList(id="resultados")
            yield Button("← Voltar", id="voltar")

    def on_button_pressed(self, event):

        

        if event.button.id == "limpar":
            self.query_one("#nome", Input).value = ""
            self.query_one("#plataforma", Select).value = ""
            self.query_one("#linguagem", Select).value = ""
            self.query_one("#gratuito", Select).value = "todos"
            self.query_one("#resultados", OptionList).clear_options()
            self.query_one("#mensagem", Static).update("Filtros limpos. Faça uma nova busca.")
            self.cursos = []

            return

        if event.button.id == "voltar":
            self.app.pop_screen()
            return

        if event.button.id == "busca":

            nome = self.query_one("#nome", Input).value.strip()

            plataforma = self.query_one("#plataforma", Select).value
            linguagem = self.query_one("#linguagem", Select).value
            gratuito = self.query_one("#gratuito", Select).value

            # Conversão do filtro de preço
            if gratuito == "gratuito":
                gratuito = 1

            elif gratuito == "pago":
                gratuito = 0

            else:
                gratuito = None

            # Conversão dos demais filtros
            if plataforma == "":
                plataforma = None

            if linguagem == "":
                linguagem = None

            # Corrige valores não selecionados do Textual
            if plataforma is Select.NULL:
                plataforma = None

            if linguagem is Select.NULL:
                linguagem = None

            resultados = busca_cursos.buscar(
                nome_do_curso=nome,
                plataforma=plataforma,
                linguagem=linguagem,
                gratuito=gratuito
            )

            lista = self.query_one("#resultados", OptionList)
            mensagem = self.query_one("#mensagem", Static)

            lista.clear_options()
            self.cursos = resultados

            if resultados:
                for curso in resultados:

                    nome_curso = curso[1]
                    plataforma_curso = curso[2]

                    lista.add_option(
                        Option(
                            f"{nome_curso} | {plataforma_curso}",
                            id=str(curso[0])
                        )
                    )

                mensagem.update("Selecione um curso e aperte Enter.")

            else:
                mensagem.update("Nenhum curso encontrado.")

    def on_option_list_option_selected(self, event: OptionList.OptionSelected):

        # Recupera o ID do curso selecionado
        curso_id = event.option.id

        # Procura o curso correspondente na lista de resultados
        for curso in self.cursos:

            if str(curso[0]) == curso_id:

                # Abre a tela de detalhes enviando os dados do curso
                self.app.push_screen(TelaDetalhesCurso(curso))
                break

class TelaMenu(Screen):
    CSS = CSS_COMUM + """
    #botoes {
        width: 50;
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
        width: 100%;
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
            yield Button("Meus Favoritos", id="favoritos")
            yield Button("Alterar dados", id="alterar")
            yield Button("Remover Usuário", id="remover")
            yield Button("Sair", id="sair")

    def on_button_pressed(self, event):

        if event.button.id == 'cadastrar':
            self.app.push_screen(TelaCadastro())

        elif event.button.id == 'login':
            self.app.push_screen(TelaLogin())

        elif event.button.id == 'favoritos':

            if not self.app.usuario_atual:
                self.app.destino_apos_login = "favoritos"
                self.app.push_screen(TelaLogin())
            else:
                self.app.push_screen(TelaFavoritos())

        elif event.button.id == 'alterar':
            self.app.push_screen(TelaAtualizar())

        elif event.button.id == 'remover':
            self.app.push_screen(TelaRemover())

        elif event.button.id == 'sair':
            self.app.exit()
            return

class TelaCadastro(Screen):

    CSS = CSS_COMUM

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

    CSS = CSS_COMUM

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

            usuario = gerenciador_usuarios.obter_usuario(
                email,
                senha
            )

            if usuario:
                self.app.usuario_atual = usuario

                destino = getattr(
                    self.app,
                    "destino_apos_login",
                    None
                )

                self.app.destino_apos_login = None

                if destino == "favoritos":
                    self.app.push_screen(TelaFavoritos())

                else:
                    tipo = usuario["tipo"]

                    if tipo == "administrador":
                        self.app.push_screen(TelaPainelAdmin())

                    elif tipo == "gerente":
                        self.app.push_screen(TelaGerenciarCursos())

                    else:
                        self.app.push_screen(TelaCursos())

            else:
                self.query_one("#mensagem", Static).update(
                    "Email ou senha incorretos."
                )

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
            # Abre a tela específica que vai coletar os dados do email
            self.app.push_screen(TelaAlterarEmail())
            
        elif event.button.id == "nav_nome":
            # Abre a tela específica pra o username
            self.app.push_screen(TelaAlterarNome())

        elif event.button.id == "nav_senha":
           # Abre a tela específica da senha
           self.app.push_screen(TelaAlterarSenha())

class TelaRemover(Screen):
    
    CSS = CSS_COMUM

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
            yield Static(
                f"[bold]{curso[1]}[/]",
                markup=True
            )

            yield Static(f"Plataforma: {curso[2]}")
            yield Static(f"Linguagem: {curso[3]}")
            yield Static(f"Gratuito: {gratuito}")
            yield Static(f"\nDescrição:\n{curso[4]}")

            yield Button(
                "♡ Favoritar curso",
                id="favoritar"
            )

            yield Static("", id="mensagem_favorito")

            yield Button(
                "🌐 Visitar site oficial",
                id="visitar"
            )

            yield Static("", id="mensagem_site")

            yield Button(
                "← Voltar aos resultados",
                id="voltar"
            )

    def on_mount(self):
        usuario = self.app.usuario_atual

        if not usuario:
            return

        usuario_id = usuario["id"]
        curso_id = self.curso[0]

        favorito = gerenciador_favoritos.verificar_favorito(
            usuario_id,
            curso_id
        )

        botao = self.query_one("#favoritar", Button)

        if favorito:
            botao.label = "♥ Remover dos favoritos"
        else:
            botao.label = "♡ Favoritar curso"

    def on_button_pressed(self, event):

        if event.button.id == "voltar":
            self.app.pop_screen()
            return

        elif event.button.id == "visitar":

            url = self.curso[6] if len(self.curso) > 6 else ""

            if url and url.strip().startswith(("https://", "http://")):
                self.app.open_url(url.strip())
            else:
                self.query_one(
                    "#mensagem_site",
                    Static
                ).update("Link oficial não cadastrado.")

            return

        elif event.button.id == "favoritar":

            usuario = self.app.usuario_atual

            if not usuario:
                self.query_one(
                    "#mensagem_favorito",
                    Static
                ).update("Faça login para favoritar cursos.")
                return

            usuario_id = usuario["id"]
            curso_id = self.curso[0]

            favorito = gerenciador_favoritos.verificar_favorito(
                usuario_id,
                curso_id
            )

            if favorito:
                sucesso, mensagem = (
                    gerenciador_favoritos.desfavoritar_curso(
                        usuario_id,
                        curso_id
                    )
                )
            else:
                sucesso, mensagem = (
                    gerenciador_favoritos.favoritar_curso(
                        usuario_id,
                        curso_id
                    )
                )

            self.query_one(
                "#mensagem_favorito",
                Static
            ).update(mensagem)

            if sucesso:
                botao = self.query_one("#favoritar", Button)

                if favorito:
                    botao.label = "♡ Favoritar curso"
                else:
                    botao.label = "♥ Remover dos favoritos"

class TelaAlterarEmail(Screen):
    CSS = CSS_COMUM

    def compose(self):
        with Vertical(id="caixa_alterar_email"):
            yield Static("[bold]SOLICITAR ALTERAÇÃO DE E-MAIL[/bold]",id='titulo', markup=True)
        
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
            sucesso, mensagem, user_id, codigo = Solicitar_alteracao_email(email, senha, novo_email)

            if sucesso:
                self.app.push_screen(
                    TelaConfirmarEmail(user_id=user_id, codigo=codigo)
                )
            else:
                self.query_one("#mensagem_email", Static).update(
                    f"[red]{mensagem}[/red]"
                )

class TelaConfirmarEmail(Screen):
    CSS = CSS_COMUM

    # O __init__ é obrigatório nesta tela para receber o ID do usuário
    def __init__(self, user_id, codigo):
        super().__init__()
        self.user_id = user_id
        self.codigo = codigo

    def compose(self):
        with Vertical(id="caixa_central"):
            yield Static("[bold]CÓDIGO DE VERIFICAÇÃO[/bold]", id='titulo',markup=True)
            yield Static(f"[bold yellow]CÓDIGO DE DEMONSTRAÇÃO: {self.codigo}[/bold yellow]",markup=True)
            yield Static("O envio do e-mail está simulado nesta versão.")
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
    CSS = CSS_COMUM

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

            # Chama a função que criámos acima
            sucesso, mensagem, user_id, codigo = Solicitar_alteracao_senha(email, senha, nova_senha)

            if sucesso:
                self.app.push_screen(
                    TelaConfirmarSenha(user_id=user_id, codigo=codigo)
                )
            else:
                self.query_one("#mensagem_senha", Static).update(
                    f"[red]{mensagem}[/red]"
                )

class TelaConfirmarSenha(Screen):
    CSS = CSS_COMUM

    def __init__(self, user_id, codigo):
        super().__init__()
        self.user_id = user_id
        self.codigo = codigo

    def compose(self):
        with Vertical(id="caixa_central"):
            yield Static("[bold]CÓDIGO DE VERIFICAÇÃO[/bold]", id="titulo_codigo_senha", markup=True)
            yield Static(f"[bold yellow]CÓDIGO DE DEMONSTRAÇÃO: {self.codigo}[/bold yellow]",markup=True)
            yield Static("O envio do e-mail está simulado nesta versão.")
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
    CSS = CSS_COMUM

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
                self.app.pop_screen() # Fecha a tela e volta pro menu
                
                # Exibe a mensagem de sucesso.
                try:
                    self.app.screen.query_one("#titulo", Static).update(f"[green]{mensagem}[/green]")
                except:
                    pass
            else:
                # Exibe o erro (ex: senha incorreta ou nome já existe)
                self.query_one("#mensagem_nome", Static).update(f"[red]{mensagem}[/red]")

class TelaPainelAdmin(Screen):

    CSS = CSS_COMUM + """
    #lista_usuarios {
        height: auto;
        margin: 1 0;
    }

    #mensagem_admin {
        margin: 1 0;
        text-align: center;
    }
    """

    def compose(self):
        with Vertical(id="detalhes"):
            yield Static("PAINEL ADMINISTRATIVO", id="titulo")
            yield Static("Usuários cadastrados:",id="subtitulo")
            yield Static("Carregando usuários...",id="lista_usuarios")
            yield Input(placeholder="E-mail do usuário",id="email_gerente")
            yield Button("Gerenciar cursos", id="gerenciar_cursos")
            yield Button("Autorizar como gerente",id="autorizar")
            yield Button("Remover permissão de gerente",id="remover_gerente")
            yield Static("", id="mensagem_admin")
            yield Button("← Voltar", id="voltar")

    def on_mount(self):
        # Impede que uma conta comum abra o painel
        usuario = self.app.usuario_atual

        if not usuario or usuario["tipo"] != "administrador":
            self.app.pop_screen()
            return

        self.atualizar_lista()

    def atualizar_lista(self):

        usuarios = gerenciador_usuarios.listar_usuarios()

        texto = ""

        for email, nome, tipo in usuarios:
            texto += f"{nome} | {email} | {tipo}\n"

        if not texto:
            texto = "Nenhum usuário cadastrado."

        self.query_one("#lista_usuarios", Static).update(texto)

    def on_button_pressed(self, event):

        if event.button.id == "gerenciar_cursos":
            self.app.push_screen(TelaGerenciarCursos())
            return

        if event.button.id == "voltar":
            self.app.pop_screen()
            return

        usuario = self.app.usuario_atual

        if not usuario or usuario["tipo"] != "administrador":
            self.query_one("#mensagem_admin", Static).update(
                "Acesso não autorizado."
            )
            return

        email_alvo = self.query_one(
            "#email_gerente", Input
        ).value.strip()

        email_admin = usuario["email"]

        if event.button.id == "autorizar":

            sucesso, mensagem = (
                gerenciador_usuarios.autorizar_gerente(
                    email_alvo,
                    email_admin
                )
            )

        elif event.button.id == "remover_gerente":

            sucesso, mensagem = (
                gerenciador_usuarios.remover_permissao_gerente(
                    email_alvo,
                    email_admin
                )
            )

        else:
            return

        self.query_one("#mensagem_admin", Static).update(mensagem)

        if sucesso:
            self.query_one("#email_gerente", Input).value = ""
            self.atualizar_lista()

class TelaFavoritos(Screen):

    CSS = CSS_COMUM + """
    #titulo {
        margin: 1 0;
    }

    Button {
        margin: 1 0;
    }
    """

    def compose(self):
        with Vertical(id="detalhes"):
            yield Static("MEUS FAVORITOS", id="titulo")
            yield Static("", id="mensagem")
            yield OptionList(id="resultados")
            yield Button("↻ Atualizar favoritos", id="atualizar")
            yield Button("← Voltar", id="voltar")

    def on_mount(self):
        self.atualizar_lista()

    def atualizar_lista(self):

        usuario = self.app.usuario_atual

        if not usuario:
            self.query_one("#mensagem", Static).update(
                "Faça login para visualizar seus favoritos."
            )
            return

        favoritos = gerenciador_favoritos.listar_favoritos(
            usuario["id"]
        )

        self.favoritos = favoritos

        lista = self.query_one("#resultados", OptionList)
        mensagem = self.query_one("#mensagem", Static)

        lista.clear_options()

        if favoritos:

            for curso in favoritos:
                lista.add_option(
                    Option(
                        f'{curso["nome"]} | {curso["plataforma"]}',
                        id=str(curso["id"])
                    )
                )

            mensagem.update(
                "Selecione um curso para visualizar os detalhes."
            )

        else:
            mensagem.update(
                "Você ainda não possui cursos favoritos."
            )

    def on_button_pressed(self, event):

        if event.button.id == "voltar":
            self.app.pop_screen()
            return

        if event.button.id == "atualizar":
            self.atualizar_lista()

    def on_option_list_option_selected(
        self, event: OptionList.OptionSelected
    ):

        curso_id = int(event.option.id)

        for curso in self.favoritos:

            if curso["id"] == curso_id:

                dados_curso = (
                    curso["id"],
                    curso["nome"],
                    curso["plataforma"],
                    curso["linguagem"],
                    curso["descricao"],
                    curso["gratuito"]
                )

                self.app.push_screen(
                    TelaDetalhesCurso(dados_curso)
                )

                break

class TelaGerenciarCursos(Screen):

    CSS = CSS_COMUM + """
    #titulo {
        margin: 1 0;
    }

    Input,
    Button {
        margin: 1 0;
    }

    #mensagem_gerencia {
        margin: 1 0;
        text-align: center;
    }
    """

    def compose(self):
        with Vertical(id="detalhes"):
            yield Static("GERENCIAMENTO DE CURSOS", id="titulo")
            yield Input(placeholder="Nome do curso...",id="nome")
            yield Input(placeholder="Plataforma (Ex: Udemy, Coursera...)",id="plataforma")
            yield Input(placeholder="Linguagem (Ex: Python, Java...)",id="linguagem")
            yield Input(placeholder="Descrição do curso...",id="descricao")
            yield Input(placeholder="Gratuito? Digite 1 para sim ou 0 para não",id="gratuito")
            yield Input(placeholder="Link oficial do curso (https://...)",id="url_site")
            yield Button("Cadastrar curso", id="cadastrar")
            yield Static("", id="mensagem_gerencia")
            yield Button("← Voltar", id="voltar")

    def on_mount(self):
        usuario = self.app.usuario_atual

        if not usuario or usuario.get("tipo") not in (
            "administrador",
            "gerente"
        ):
            self.app.pop_screen()

    def on_button_pressed(self, event):

        if event.button.id == "voltar":
            self.app.pop_screen()
            return

        if event.button.id == "cadastrar":

            nome = self.query_one("#nome", Input).value.strip()
            plataforma = self.query_one("#plataforma", Input).value.strip()
            linguagem = self.query_one("#linguagem", Input).value.strip()
            descricao = self.query_one("#descricao", Input).value.strip()
            gratuito_texto = self.query_one("#gratuito", Input).value.strip()
            url_site = self.query_one("#url_site", Input).value.strip()

            mensagem = self.query_one("#mensagem_gerencia", Static)

            if not nome or not plataforma or not linguagem or not descricao:
                mensagem.update("Preencha todos os campos obrigatórios.")
                return

            if gratuito_texto not in ("0", "1"):
                mensagem.update("Gratuito deve ser 1 (sim) ou 0 (não).")
                return

            if url_site and not url_site.startswith(("https://", "http://")):
                mensagem.update("Informe um link válido começando com http:// ou https://.")
                return

            gratuito = int(gratuito_texto)

            try:
                gerenciador_cursos.inserir_curso(
                    nome,
                    plataforma,
                    linguagem,
                    descricao,
                    gratuito,
                    url_site
                )

                mensagem.update("Curso cadastrado com sucesso!")

                # Limpa os campos após o cadastro
                self.query_one("#nome", Input).value = ""
                self.query_one("#plataforma", Input).value = ""
                self.query_one("#linguagem", Input).value = ""
                self.query_one("#descricao", Input).value = ""
                self.query_one("#gratuito", Input).value = "1"
                self.query_one("#url_site", Input).value = ""

            except Exception as erro:
                mensagem.update(f"Erro ao cadastrar curso: {erro}")
