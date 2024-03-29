from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout #trazendo o layout do aplicativo, por ele podemos organizar as coisas na tela
from kivy.uix.label import Label


class Main(App):
    def build(self):
        box = BoxLayout(orientation = 'vertical') #criando uma variavel que vai receber o BoxLayout que no caso é essa variavel chamada box
        #com a orientation é possível mudar a orientação de como os layouts estarao na tela
        botao = Button(text = 'botao 1') #criei uma variavel chamada botao, essa variavel vai receber o botao com o texto escrito
        texto = Label(text = 'texto 1') #criando uma variavek chamada texto, essa variavel vai receber, passando o label e inserindo na tela quando solicitado
        box.add_widget(botao) #chamando o metodo add_widget que vai fazer a inserção do botao na variavel que recebeu o nosso button
        box.add_widget(texto) #chamando o metodo add_widget, para ele adicionar isso a um widget e ser chamado quando chamado a variavel box

        box2 = BoxLayout()
        botao2 = Button(text = 'botao 2')
        texto2 = Label(text = 'texto')
        box2.add_widget(botao2)
        box2.add_widget(texto2)
        box.add_widget(box2)
        return box

Main().run()