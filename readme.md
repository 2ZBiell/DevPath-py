# 🚀 DevPath

O **DevPath** é uma plataforma desenvolvida em Python para auxiliar estudantes e programadores iniciantes na busca por cursos e conteúdos relacionados à área de desenvolvimento de software.

O projeto reúne cursos de diferentes plataformas em um único ambiente, permitindo pesquisar, aplicar filtros, consultar informações, acessar os sites oficiais e salvar cursos favoritos.

---

## 📌 Sobre o Projeto

O DevPath surgiu com o objetivo de facilitar o acesso a oportunidades de aprendizado na área de tecnologia, centralizando informações sobre cursos de programação e desenvolvimento.

Além da busca por cursos, a plataforma possui um sistema de contas com diferentes níveis de permissão, permitindo que usuários, gerentes e administradores tenham acesso a funcionalidades específicas.

---

## ✨ Funcionalidades

### 🔎 Busca e consulta de cursos
- Pesquisa de cursos pelo nome.
- Filtros por plataforma, tecnologia e preço.
- Visualização dos detalhes dos cursos.
- Acesso ao site oficial de cada curso.

### 👤 Gerenciamento de contas
- Cadastro de usuários.
- Login e autenticação.
- Alteração de e-mail com código de verificação.
- Alteração de senha com código de verificação.
- Alteração do nome de usuário.
- Exclusão de conta.

**Observação:** nesta versão acadêmica, o envio dos códigos de verificação por e-mail é simulado. Os códigos são apresentados no terminal e utilizados na interface para demonstrar o processo.

### ⭐ Sistema de favoritos
- Adicionar cursos aos favoritos.
- Remover cursos dos favoritos.
- Consultar a lista de cursos favoritos.
- Associação dos favoritos à conta do usuário.

### 🛠️ Gerenciamento administrativo
O sistema possui três níveis de acesso:

- **Usuário:** pode pesquisar cursos, consultar detalhes e gerenciar seus favoritos.
- **Gerente:** possui permissão para cadastrar novos cursos.
- **Administrador:** pode autorizar ou remover permissões de gerente e também gerenciar cursos.

---

## 🚀 Releases

### Release 1.0 — Versão Inicial

Implementação das funcionalidades fundamentais do DevPath, incluindo gerenciamento de contas e consulta de cursos.

**Requisitos implementados:**
- RF01 — Cadastro de Conta (C).
- RF02 — Login (R).
- RF03 — Atualizar Informações (U).
- RF04 — Deletar Informações (D).
- RF05 — Buscar Cursos.
- RF06 — Exibição dos Cursos.

### Release 2.0 — Expansão da Plataforma

Ampliação das funcionalidades do sistema, com recursos de interação com os cursos e gerenciamento de diferentes níveis de acesso.

**Requisitos implementados:**
- RF07 _ Filtrar Cursos.
- RF08 — Favoritar Curso.
- RF09 — Visitar curso no site oficial.
- RF10 — Ver detalhes do curso.
- RF11 — Cadastro de Conta Administrador e Gerente.
- RF12 — Painel Administrativo.

---

## 🛠️ Tecnologias utilizadas

| Tecnologia | Utilização |
|---|---|
| Python | Linguagem principal |
| Textual | Construção da interface de terminal |
| SQLite | Armazenamento dos dados |
| Git e GitHub | Controle de versão e colaboração |

### Bibliotecas
- `textual`: criação das telas, botões, campos de entrada e eventos.
- `sqlite3`: conexão e manipulação dos bancos de dados.
- `secrets`: geração de códigos de verificação.
- `re`: validação de formatos de e-mail.

---

## 📁 Estrutura do Projeto

```text
DevPath/
│
├── main.py
├── cadastrar_cursos.py
├── requirements.txt
├── readme.md
│
├── app/
│   ├── database.py
│   ├── buscar.py
│   ├── cadastro_conta.py
│   ├── alterar_dados_da_contav2.py
│   ├── deletar_dados.py
│   ├── favoritos.py
│   │
│   └── ui/
│       └── interface.py
│
└── data/
    ├── cursos.db
    └── usuarios.db
```

### Organização dos módulos

- `main.py`: inicialização da aplicação e criação das tabelas necessárias.
- `database.py`: conexão com o banco de cursos e gerenciamento dos registros.
- `buscar.py`: organização das operações de busca de cursos.
- `cadastro_conta.py`: cadastro, autenticação e gerenciamento de permissões dos usuários.
- `alterar_dados_da_contav2.py`: operações de alteração de dados e verificação por código.
- `deletar_dados.py`: exclusão de contas.
- `favoritos.py`: gerenciamento dos cursos favoritos.
- `interface.py`: telas e interação com o usuário.
- `cadastrar_cursos.py`: script para inserção inicial de cursos no banco de dados.
- `data/`: armazenamento dos bancos de dados SQLite.

---

## ▶️ Como executar o projeto

### 1. Clonar o repositório

```bash
git clone https://github.com/2ZBiell/DevPath-py.git
```

### 2. Entrar na pasta do projeto

```bash
cd DevPath-py
```

### 3. Criar um ambiente virtual

```bash
python -m venv .venv
```

### 4. Ativar o ambiente virtual

No Windows:

```powershell
.venv\Scripts\activate
```

### 5. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 6. Executar a aplicação

```bash
python main.py
```

**Cadastro inicial de cursos:** caso seja necessário popular um banco de cursos vazio, execute o script abaixo uma única vez:

```bash
python cadastrar_cursos.py
```

---

## 👨‍💻 Desenvolvedores

| Nome | Função |
|---|---|
| Eduardo Freitas | Desenvolvimento |
| Gabriel Ferreira | Desenvolvimento |
| Ricardo Soares | Desenvolvimento |

---

**DevPath — Seu caminho para aprender programação! 🚀**
