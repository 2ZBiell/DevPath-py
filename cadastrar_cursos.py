from app.database import gerenciador_cursos

gerenciador_cursos.tabela_cursos()

cursos = [

    # ==========================
    # IFRS
    # ==========================

    (
        "Administrador de Banco de Dados",
        "IFRS",
        "Banco de Dados",
        "Curso de formação voltado à administração de bancos de dados, "
        "com conteúdos relacionados à organização e gerenciamento de dados.",
        1,
        "https://estude.ifrs.edu.br/cursos/administrador-de-banco-de-dados/"
    ),

    (
        "Banco de Dados 1: fundamentos",
        "IFRS",
        "Banco de Dados",
        "Apresenta conceitos fundamentais de bancos de dados e "
        "introduz conhecimentos necessários para trabalhar com dados.",
        1,
        "https://estude.ifrs.edu.br/cursos/banco-de-dados-1-fundamentos/"
    ),

    (
        "Estrutura de Dados",
        "IFRS",
        "Lógica de Programação",
        "Curso introdutório sobre estruturas de dados e organização "
        "de informações utilizadas em programas.",
        1,
        "https://estude.ifrs.edu.br/cursos/estrutura-de-dados/"
    ),

    (
        "Programação Básica com Java I",
        "IFRS",
        "Java",
        "Primeiro módulo da formação em Java, voltado aos fundamentos "
        "da linguagem e da programação.",
        1,
        "https://estude.ifrs.edu.br/cursos/programacao-basica-com-java-i/"
    ),

    (
        "Programação Básica com Java II",
        "IFRS",
        "Java",
        "Segundo módulo da formação em Java, dando continuidade "
        "ao aprendizado da linguagem.",
        1,
        "https://estude.ifrs.edu.br/cursos/programacao-basica-com-java-ii/"
    ),

    (
        "Programação Básica com Java III",
        "IFRS",
        "Java",
        "Terceiro módulo da formação em Java, aprofundando "
        "os conhecimentos da linguagem.",
        1,
        "https://estude.ifrs.edu.br/cursos/programacao-basica-com-java-iii/"
    ),

    (
        "Lógica de Programação: começando a desenvolver seus primeiros programas",
        "IFRS",
        "Lógica de Programação",
        "Introdução à lógica de programação e aos conceitos necessários "
        "para desenvolver os primeiros programas.",
        1,
        "https://estude.ifrs.edu.br/cursos/logica-de-programacao-comecando-a-desenvolver-seus-primeiros-programas/"
    ),

    (
        "Lógica de Programação: deixando os seus programas espertos",
        "IFRS",
        "Lógica de Programação",
        "Continuação dos estudos de lógica de programação, "
        "com conceitos para desenvolver programas mais elaborados.",
        1,
        "https://estude.ifrs.edu.br/cursos/logica-de-programacao-deixando-os-seus-programas-espertos/"
    ),

    (
        "Lógica de Programação: múltiplos valores e módulos",
        "IFRS",
        "Lógica de Programação",
        "Aborda o uso de múltiplos valores e módulos na construção "
        "e organização de programas.",
        1,
        "https://estude.ifrs.edu.br/cursos/logica-de-programacao-multiplos-valores-e-modulos/"
    ),

    (
        "JavaScript: Fundamentos para Desenvolvimento Web Interativo",
        "IFRS",
        "JavaScript",
        "Apresenta fundamentos de JavaScript aplicados à criação "
        "de páginas e funcionalidades interativas na web.",
        1,
        "https://estude.ifrs.edu.br/cursos/javascript/"
    ),

    (
        "Desenvolvimento Backend com PHP: POO e Integração com MySQL",
        "IFRS",
        "PHP",
        "Curso sobre desenvolvimento backend com PHP, programação "
        "orientada a objetos e integração com bancos MySQL.",
        1,
        "https://estude.ifrs.edu.br/cursos/desenvolvimento-backend-com-php-poo-e-integracao-com-mysql/"
    ),

    # ==========================
    # EV.G
    # ==========================

    (
        "IA e Transformação Digital",
        "EV.G",
        "Inteligência Artificial",
        "Apresenta conceitos de inteligência artificial e transformação "
        "digital, incluindo ética, governança e serviços digitais.",
        1,
        "https://www.escolavirtual.gov.br/curso/1588"
    ),

    (
        "Eixo 1 - Analisando dados e evidências",
        "EV.G",
        "Ciência de Dados",
        "Trilha de aprendizagem sobre letramento em dados, análise "
        "de evidências e resolução de problemas com base em dados.",
        1,
        "https://www.escolavirtual.gov.br/curso/1225"
    ),

    # ==========================
    # CORUJINHAS
    # ==========================

    (
        "Introdução à Programação com Python",
        "Corujinhas",
        "Python",
        "Curso introdutório sobre fundamentos de Python, estruturas "
        "de controle, funções, strings e orientação a objetos.",
        1,
        "https://corujinhas.com.br/curso/introducao-programacao-python"
    ),

    # ==========================
    # CURSA
    # ==========================

    (
        "Programação orientada a objeto usando Java",
        "CURSA",
        "Java",
        "Curso sobre classes, objetos, encapsulamento, herança "
        "e polimorfismo utilizando Java.",
        1,
        "https://cursa.app/pt/curso-gratuito/programacao-orientada-a-objeto-usando-java-bdhe"
    ),
    (
        "Programação em C",
        "CURSA",
        "C",
        "Introdução à linguagem C, incluindo variáveis, operadores, "
        "condicionais, repetição, ponteiros e estruturas.",
        1,
        "https://cursa.app/pt/curso-gratuito/programacao-em-c-hhd"
    ),
    (
        "Python do Zero ao Avançado",
        "CURSA",
        "Python",
        "Curso de Python que aborda fundamentos, estruturas de dados, "
        "orientação a objetos e recursos avançados.",
        1,
        "https://cursa.app/pt/curso-gratuito/python-do-zero-ao-avancado-ejba"
    ),
    (
        "Java",
        "CURSA",
        "Java",
        "Curso introdutório de programação com Java, com aulas "
        "e exercícios para desenvolver conhecimentos na linguagem.",
        1,
        "https://cursa.app/pt/curso-gratuito/java-bbj"
    ),
    (
        "Programação em Python",
        "CURSA",
        "Python",
        "Curso sobre fundamentos da linguagem Python e construção "
        "de programas.",
        1,
        "https://cursa.app/pt/curso-gratuito/programacao-em-python-dibh"
    ),
    (
        "Programação com Python",
        "CURSA",
        "Python",
        "Conteúdo introdutório e prático sobre programação utilizando "
        "Python.",
        1,
        "https://cursa.app/pt/curso-gratuito/python-bfd"
    ),
    (
        "Engenharia de Software",
        "CURSA",
        "Engenharia de Software",
        "Aborda processos de desenvolvimento, requisitos, arquitetura, "
        "modelagem e testes de software.",
        1,
        "https://cursa.app/pt/curso-gratuito/engenharia-de-software-jdi"
    ),
    (
        "Programação em C#",
        "CURSA",
        "C#",
        "Introdução à linguagem C#, com variáveis, operadores, "
        "condicionais e desenvolvimento de programas.",
        1,
        "https://cursa.app/pt/curso-gratuito/programacao-em-csharp-ee"
    ),
    (
        "Programação Java",
        "CURSA",
        "Java",
        "Curso de programação Java com conteúdos teóricos e exercícios "
        "para praticar os fundamentos da linguagem.",
        1,
        "https://cursa.app/pt/curso-gratuito/programacao-java-dghc"
    ),
    (
        "Maratona Java",
        "CURSA",
        "Java",
        "Curso de Java com conteúdo extenso e exercícios para "
        "aprofundar os conhecimentos na linguagem.",
        1,
        "https://cursa.app/pt/curso-gratuito/maratona-java-dida"
    ),
    (
        "Java para Iniciantes",
        "CURSA",
        "Java",
        "Curso introdutório voltado a quem deseja aprender os primeiros "
        "conceitos da linguagem Java.",
        1,
        "https://cursa.app/pt/curso-gratuito/java-para-iniciantes-bdhd"
    ),
    (
        "Desenvolvimento FullStack com React, Node e MongoDB",
        "CURSA",
        "Desenvolvimento Web",
        "Curso sobre desenvolvimento Full Stack utilizando React, "
        "Node.js e MongoDB.",
        1,
        "https://cursa.app/pt/curso-gratuito/desenvolvimento-fullstack-com-react-node-e-mongodb-faad"
    ),
    (
        "Introdução à Programação e Lógica com Lua",
        "CURSA",
        "Lógica de Programação",
        "Introdução à lógica de programação com Lua, orientação "
        "a objetos e desenvolvimento de jogos.",
        1,
        "https://cursa.app/pt/curso-gratuito/introducao-a-programacao-e-logica-com-lua-do-zero-ao-oop-e-game-dev-faij"
    ),
    (
        "Aprenda a programar em GO",
        "CURSA",
        "Go",
        "Introdução à linguagem Go, com fundamentos e exercícios "
        "para desenvolver programas.",
        1,
        "https://cursa.app/pt/curso-gratuito/aprenda-a-programar-em-go-eifc"
    ),
    (
        "Ruby on Rails para Iniciantes",
        "CURSA",
        "Desenvolvimento Web",
        "Introdução ao desenvolvimento web com Ruby on Rails, "
        "utilizando rotas, MVC e Active Record.",
        1,
        "https://cursa.app/pt/curso-gratuito/ruby-on-rails-para-iniciantes-gjc"
    ),
    (
        "Java Completo",
        "CURSA",
        "Java",
        "Curso de programação Java com aulas e exercícios "
        "para aprofundar os conhecimentos na linguagem.",
        1,
        "https://cursa.app/pt/curso-gratuito/java-completo-didj"
    ),

    # ==========================
    # IFRS
    # Os links levam ao catálogo oficial.
    # ==========================

    (
        "Node.js: Introdução ao Desenvolvimento de APIs Modernas",
        "IFRS",
        "Desenvolvimento Web",
        "Introdução ao Node.js e ao desenvolvimento de APIs modernas.",
        1,
        "https://estude.ifrs.edu.br/cursos/"
    ),
    (
        "React Native: Criação de Aplicativos Móveis Modernos",
        "IFRS",
        "Desenvolvimento Web",
        "Curso sobre criação de aplicativos móveis utilizando "
        "React Native.",
        1,
        "https://estude.ifrs.edu.br/cursos/"
    ),
    (
        "React: Construindo Single Page Applications Dinâmicas",
        "IFRS",
        "Desenvolvimento Web",
        "Apresenta o desenvolvimento de aplicações web de página única "
        "utilizando React.",
        1,
        "https://estude.ifrs.edu.br/cursos/"
    ),
    (
        "React: Construindo Single Page Applications Dinâmicas e Interativas",
        "IFRS",
        "Desenvolvimento Web",
        "Aprofunda o desenvolvimento de aplicações interativas "
        "utilizando React.",
        1,
        "https://estude.ifrs.edu.br/cursos/"
    ),
    (
        "Banco de Dados: Oracle PL/SQL",
        "IFRS",
        "Banco de Dados",
        "Introdução à linguagem PL/SQL e ao trabalho com bancos "
        "de dados Oracle.",
        1,
        "https://estude.ifrs.edu.br/cursos/"
    ),
    (
        "Programador Web",
        "IFRS",
        "Desenvolvimento Web",
        "Formação profissional voltada ao desenvolvimento de aplicações "
        "e páginas para a internet.",
        1,
        "https://estude.ifrs.edu.br/cursos/"
    ),
    (
        "Projeto de Sistemas Web",
        "IFRS",
        "Desenvolvimento Web",
        "Apresenta conceitos relacionados ao planejamento e "
        "desenvolvimento de sistemas web.",
        1,
        "https://estude.ifrs.edu.br/cursos/"
    ),
    (
        "Raspberry PI Básico para IoT",
        "IFRS",
        "Informática",
        "Introdução ao Raspberry Pi e suas aplicações em projetos "
        "de Internet das Coisas.",
        1,
        "https://estude.ifrs.edu.br/cursos/"
    ),
    (
        "Raspberry PI e Aplicações",
        "IFRS",
        "Informática",
        "Apresenta aplicações práticas utilizando a plataforma "
        "Raspberry Pi.",
        1,
        "https://estude.ifrs.edu.br/cursos/"
    ),
    (
        "Web Design",
        "IFRS",
        "HTML e CSS",
        "Introdução aos conceitos de design para páginas e interfaces web.",
        1,
        "https://estude.ifrs.edu.br/cursos/"
    ),
    (
        "Windows Server 2016: Active Directory",
        "IFRS",
        "Informática",
        "Curso sobre administração de diretórios e gerenciamento "
        "de usuários no Windows Server.",
        1,
        "https://estude.ifrs.edu.br/cursos/"
    ),
    (
        "Windows Server 2016: Instalação e Administração",
        "IFRS",
        "Informática",
        "Apresenta os procedimentos de instalação e administração "
        "do Windows Server 2016.",
        1,
        "https://estude.ifrs.edu.br/cursos/"
    ),

    # ==========================
    # CURSO EM VÍDEO
    # Links para o catálogo oficial.
    # ==========================

    (
        "Python 3 - Mundo 2",
        "Curso em Vídeo",
        "Python",
        "Continuação do curso de Python, abordando estruturas "
        "condicionais e repetição.",
        1,
        "https://www.cursoemvideo.com/curso-categoria/python/"
    ),
    (
        "Python 3 - Mundo 3",
        "Curso em Vídeo",
        "Python",
        "Aprofunda os conhecimentos em Python, com estruturas "
        "de dados e recursos da linguagem.",
        1,
        "https://www.cursoemvideo.com/curso-categoria/python/"
    ),
    (
        "JavaScript",
        "Curso em Vídeo",
        "JavaScript",
        "Curso de introdução ao JavaScript, linguagem utilizada "
        "para desenvolver funcionalidades interativas na web.",
        1,
        "https://www.cursoemvideo.com/cursos"
    ),
    (
        "HTML5 e CSS3 - Módulo 5",
        "Curso em Vídeo",
        "HTML e CSS",
        "Continuação da formação em HTML5 e CSS3, com recursos "
        "para criação de páginas web.",
        1,
        "https://www.cursoemvideo.com/cursos"
    ),
    (
        "Java Básico",
        "Curso em Vídeo",
        "Java",
        "Introdução à programação com Java, abordando fundamentos "
        "da linguagem.",
        1,
        "https://www.cursoemvideo.com/cursos"
    ),
    (
        "MySQL",
        "Curso em Vídeo",
        "Banco de Dados",
        "Curso introdutório sobre bancos de dados relacionais "
        "e gerenciamento utilizando MySQL.",
        1,
        "https://www.cursoemvideo.com/cursos"
    ),

    # ==========================
    # EV.G
    # ==========================

    (
        "Aprendendo com Python",
        "EV.G",
        "Python",
        "Curso de Python com variáveis, operações, condições, "
        "laços, funções, estruturas de dados e orientação a objetos.",
        1,
        "https://www.escolavirtual.gov.br/curso/629"
    ),
    (
        "Fundamentos da Visão Computacional - IA do Azure",
        "EV.G",
        "Inteligência Artificial",
        "Apresenta conceitos de visão computacional e aplicações "
        "de inteligência artificial utilizando tecnologias Azure.",
        1,
        "https://www.escolavirtual.gov.br/programa/313"
    ),
    (
        "Visão Geral da IA no Azure",
        "EV.G",
        "Inteligência Artificial",
        "Introdução à inteligência artificial, aprendizado de máquina "
        "e recursos disponíveis na plataforma Azure.",
        1,
        "https://www.escolavirtual.gov.br/programa/313"
    ),
    (
        "Soluções Preditivas Baseadas em Dados com R e Python",
        "EV.G",
        "Ciência de Dados",
        "Curso sobre aprendizado de máquina, algoritmos e "
        "desenvolvimento de soluções preditivas com R e Python.",
        1,
        "https://www.escolavirtual.gov.br/"
    ),
    (
        "Gerenciar Dados com o Microsoft 365",
        "EV.G",
        "Ciência de Dados",
        "Apresenta ferramentas de coleta, automação e análise "
        "de dados utilizando Microsoft Forms, Power Automate, Excel e Power BI.",
        1,
        "https://www.escolavirtual.gov.br/"
    )
]

for curso in cursos:
    gerenciador_cursos.inserir_curso(*curso)

print(f"{len(cursos)} cursos cadastrados!")
