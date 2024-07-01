class Livros:
    
    def __init__ (self,nome_livro,autor,editora):
        
        self.__nome_livro= nome_livro
        self.__autor=autor
        self.__editora=editora
    
    
    def get_nomeLivros(self):
        
        return self.__nome_livro
    
    def set_nomeLivros(self,novoLivro):
        
        self.__nome_livro=novoLivro
        
    def get_autor(self):
        
        return print(self.__autor)
    
    def set_autor(self,novoAutor):
        
        self.__autor=novoAutor
        
    def get_editora(self):
        
        return print(self.__editora)
    
    def set_editora(self,novaEditora):
        
        self.__editora=novaEditora
        
class Usuario:
    
    def __ini__ (self, nomeUsuario,id):
        
        self.__nomeUsuario=nomeUsuario
        self.__id=id
        
    
    def get_nomeUsuario(self):
        
        return self.__nomeUsuario
    
    def set_nomeUsuario(self,novonomeUsuario):
    
        self.__nomeUsuario=novonomeUsuario
        
        
    def get_id(self):
        
        return self.__id
    
    
    def set_id(self, nv_id):
        
        self.__id=nv_id
                
        
class Biblioteca(Livros):
    
    def __init__(self, nome_livro, autor, editora):
        
        self.livro={}
        
        super().__init__(nome_livro, autor, editora)
        
    
    def adicionar_livros(self):
        
        self.livro={
            
            'Nome':self.get_nomeLivros(),
            'Autor':self.get_autor(),
            'Editora':self.get_editora()
                        
        }    
        
    def dados_livros(self):
        
        for chave,valor in self.livro.items():
            
            print(f'{chave}:{valor}')
            
            
    def excluir_livros(self):
        
        x=input("Deseja exlcuir qual livro ?")
        
        if x==self.livro['Nome']:
            
            del self.livro['Nome']
            print("Livro exlcuído com sucesso!")
        
        
    
    
            
