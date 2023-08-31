from bs4.element import Tag 

class Disciplina:

    # id = 0

    def __init__(
        self, 
        html:Tag = None,
        id:int=None,
        nivel:int=None, 
        cod:str=None, 
        name:str=None, 
        horas:int=None, 
        tipo:str=None, 
        pre:str=None,
        natureza:str=None
    ):
        self.id = id
        self.html = html
        self.nivel = nivel
        self.cod = cod
        self.name = name
        self.horas = horas
        self.tipo = tipo
        self.pre = pre
        self.natureza = natureza
        self.creditos = None
        # self.montaHtml()   


    def dic(self): return {k: v for k, v in self.__dict__.items() if k != "html"}

    def __str__(self): return "".join([f"{k}: {v}\n" for k, v in self.dic().items()])+'\n'

    def __repr__(self): return f"{self.id}, {self.cod}, {self.name}, {self.nivel}, {self.natureza}"


    def montaHtml(self):
        self.cod, n, h, self.tipo, p, _, self.natureza = [ i.text.strip().replace("\n", ";").replace("\t", "") for i in self.html.find_all("td") ]
        self.name = n.split(" - ")[0]
        self.horas, self.creditos = self.montaHoras(n, h)
        self.pre = self.montaPre(p)


    def montaHoras(self, n:str, h:str):
        # Exemplo:
        # n = "REDES DE COMPUTADORES I - 60h (4cr)"
        # h = "45h (3cr) aula ; 15h (1cr) lab."
        hrs = int(n.split(" - ")[1].split(" (")[0].replace("h", ""))
        creditos = int(n.split(" - ")[1].split(" (")[1].replace("cr)", ""))
        aula = int(h.split(" ; ")[0].split(" (")[0].replace("h", ""))
        lab = int(h.split(" ; ")[1].split(" (")[0].replace("h", ""))
        return hrs, {"creditos": creditos, "aula": aula, "lab": lab}
    

    def montaPre(self, pre:str):
        # ex = "( ( SINF/CSHNB007 OU SINF/CSHNB010  ) E ( CHN0730 ) )"
        # ex2 = "( ( SINF/CSHNB007 E SINF/CSHNB010 E SINF/CSHNB032 ) OU ( SINF/CSHNB019 E SINF/CSHNB030 ) )"
        # Transforma em:
        # ex: {"op":"E", "ds": [{"op": "OU", "ds":["SINF/CSHNB007", "SINF/CSHNB010"]}, "CHN0730"]}
        # ex2: {"op":"OU", "ds": [{"op": "E", "ds":["SINF/CSHNB007", "SINF/CSHNB010", "SINF/CSHNB032"]}, {"op": "E", "ds":["SINF/CSHNB019", "SINF/CSHNB030"]}]}
        pre = pre.replace("(", "").replace(")", "")
        if "OU" in pre:
            return {"op":"OU", "ds": [self.montaPre(i) for i in pre.split("OU")]}
        elif "E" in pre:
            return {"op":"E", "ds": [self.montaPre(i) for i in pre.split("E")]}
        else:
            return pre.strip()