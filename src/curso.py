from disciplina import Disciplina

class Curso:
    
    def __init__(self, componentes=None, file=None):
        if componentes:
            print("componentes")
            self.componentes = componentes
            self.disciplinas = [ Disciplina(html=d, nivel=nivel) for nivel, d in componentes ]

        elif file:
            self.componentes = []
            self.disciplinas = [
                Disciplina(
                    None, 
                    d["id"], 
                    d["nivel"],
                    d["cod"], 
                    d["name"], 
                    d["horas"],
                    d["tipo"], 
                    d["pre"],
                    d["natureza"],
                    d["creditos"]
                ) for d in file 
            ]
        self.periodos = []


    def dic(self): 
        return [ x.dic() for x in self.disciplinas ]

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

    def nivel(self, nivel:int): return [ i for i in self.disciplinas if i.nivel == nivel ]
    def obrigatorias(self): return [i for i in self.disciplinas if i.natureza == "OBRIGATÓRIA"]
    def opcionais(self): return [i for i in self.disciplinas if i.natureza == "OPTATIVA"]
    def obriNivel(self, nivel): return [ i for i in self.nivel(nivel) if i.natureza == "OBRIGATÓRIA" ]
    def optaNivel(self, nivel): return [ i for i in self.nivel(nivel) if i.natureza == "OPTATIVA" ]
