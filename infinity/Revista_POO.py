class Material:
    def __init__(self, titulo,autor,editora):
        self.titulo=titulo
        self.autor=autor
        self.editora=editora
        
    def exibir_informacoes(self):
        
        resumo={
            
            "Titulo":self.titulo,
            "Autor":self.autor,
            "Editora":self.editora            
        }
        
        for chave, valor in resumo.items():
            print(f"{chave}:{valor}")
            
class Livro(Material):
    def __init__(self, titulo, autor, editora,genero):
        self.genero=genero
        super().__init__(titulo, autor, editora)
        
    def exibir_informacoes(self):
        
        resumo={
            
            "Titulo":self.titulo,
            "Autor":self.autor,
            "Editora":self.editora,
            "Genero":self.genero            
        }
        
        for chave, valor in resumo.items():
                print(f"{chave}:{valor}")

class Revista(Material):
    def __init__(self, titulo, autor, editora,edicao):
        self.edicao=edicao
        super().__init__(titulo, autor, editora)
        
    def exibir_informacoes(self):
        
        resumo={
            
            "Titulo":self.titulo,
            "Autor":self.autor,
            "Editora":self.editora,
            "Edição":self.edicao     
        }
        
        for chave, valor in resumo.items():
                print(f"{chave}:{valor}")
            
                    