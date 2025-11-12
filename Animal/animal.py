from abc import ABC, abstractmethod

class Animal:
    def __init__(self):
        self.is_alive = True

    def respirar(self):
        print("respirando")

    def morrer(self):
        self.is_alive = False
        print('Morreu')

    @abstractmethod #Obriga todos da herança a fazerem esse método
    def emitir_som(self):
        pass
