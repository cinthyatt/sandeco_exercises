class Livro:
    def __init__(self, titulo, autor, numero_de_paginas):
        self.titulo = titulo
        self.autor = autor
        self.numero_de_paginas = numero_de_paginas

    def resumo(self):
        return f"O livro {self.titulo} foi escrito por {self.autor} e tem {self.numero_de_paginas} páginas."
    
livro1 = Livro("Alice", "George Owen", 156)
print(livro1.resumo())