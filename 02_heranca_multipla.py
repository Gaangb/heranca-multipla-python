# Aqui eu demonstro o uso de herança multipla usando a linguagem python.
# Neste exemplo a classe Ornintorrinco está herdando de Ave e Mamifero. 

class Animal:
    def __init__(self, nro_patas):
        self.nro_patas = nro_patas
    
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"



class Mamifero(Animal):
    def __init__(self, cor_pelo, **kw):
        self.cor_pelo = cor_pelo
        super().__init__(**kw)

class Ave(Animal):
    def __init__(self, cor_bico, **kw):
        self.cor_bico = cor_bico
        super().__init__(**kw)

class Falar:
    def falar(self):
        return("Olá pessoal")

class Cachorro(Mamifero, Falar):
    pass

class Gato(Mamifero, Falar):
    pass

class Leao(Mamifero, Falar):
    pass


class Ornintorrinco(Mamifero, Ave, Falar):
    def __init__(self, cor_bico, cor_pelo, nro_patas):
        self.cor_bico = cor_bico
        super().__init__(cor_pelo=cor_pelo, cor_bico=cor_bico, nro_patas=nro_patas)



    

gato = Gato(nro_patas=4, cor_pelo="preto")

ornintorrinco = Ornintorrinco(nro_patas=4, cor_pelo="Marrom", cor_bico="preto")