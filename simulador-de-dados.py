# simular um uso de um dado, gerando um valor de 1 a 6
import random
import PySimpleGUI as sg


class SimuladorDado:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        # layout
        self.layout = [
            [sg.Text('Jogar o dado?')],
            [sg.Button('sim'), sg.Button('não')]
        ]

    def Iniciar(self):
        # criar uma Janela
        self.janela = sg.Window('Simulador de dado', Layout=self.layout)
        # Ler os valores da tela
        self.eventos, self.valores = self.janela.Read()
        # Fazer alguma coisa com esses valores
        while True:

            try:
                if self.eventos == 'sim' or self.eventos == 's':
                    self.GerarValorDoDado()
                elif self.eventos == 'não' or self.eventos == 'n':
                    print('Agradecemos a participação!')
                else:
                    print('Por favor digitar sim ou não')
            except:
                print('Ocorreu um erro ao receber a resposta')

    def GerarValorDoDado(self):
        print(random.randint(self.valor_minimo, self.valor_maximo))


simulador = SimuladorDado()
simulador.Iniciar()
