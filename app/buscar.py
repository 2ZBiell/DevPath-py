from app.database import gerenciador_cursos


class BuscaCursos:

    def buscar(
        self,
        nome_do_curso="",
        plataforma=None,
        linguagem=None,
        gratuito=None
    ):
        return gerenciador_cursos.buscar_cursos(
            nome_do_curso,
            plataforma,
            linguagem,
            gratuito
        )

busca_cursos = BuscaCursos()
