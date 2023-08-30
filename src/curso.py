from disciplina import Disciplina

class Curso:
    
    def __init__(self, componentes):
        self.componentes = componentes
        self.disciplinas = [ Disciplina(d, nivel) for nivel, d in componentes ]


    def busca(self, cod):
        retorno, i = None, 0
        while retorno == None and i < len(self.disciplinas):
            retorno = self.disciplinas[i] if self.disciplinas[i].cod == cod else None
            i += 1
        return retorno
    
    def buscaName(self, name):
        retorno, i = None, 0
        while retorno == None and i < len(self.disciplinas):
            retorno = self.disciplinas[i] if self.disciplinas[i].name.lower() == name.lower() else None
            i += 1
        return retorno

    def buscaPer(self, per:int): return [ i for i in self.disciplinas if i.nivel == per ]