'''
from kivy.app import App
from kivy.uix.label import Label

class MainApp(App):
    def build(self):
        label = Label(text="K Y V I",size_hint=(0.5,0.5),pos_hint={'center_x':0.5,'center_y':0.5})
        return label

if __name__ == '__main__':
    app = MainApp()
    app.run()
'''

'''
from kivy.app import App
from kivy.uix.image import Image , AsyncImage

class MainApp(App):
    def build(self):
        image = AsyncImage(source='https://supermariorun.com/assets/img/stage/mario03.png',size_hint=(1,.5), pos_hint={'center_x':.5,'center_y':.5})
        return image

if __name__ == '__main__':
    app = MainApp()
    app.run()
'''

# Layouts usados comumente : BoxLayot , FloatLayout , GridLayout
# Argumentos  de layout : padding, spacing, orientation
'''
import random
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

red = [1,0,0,1]
green = [0,1,0,1]
blue = [0,0,1,1]
purple = [1,0,1,1]

class HBoxLayouExample(App):
    def build(self):
        layout = BoxLayout(padding=10)
        colors = [red,green,blue,purple]

        for i in range(1,6):
            btn = Button(text=f"Este é o botão #{i}",background_color=random.choice(colors))
            btn.bind(on_press = self.on_press_button)
            layout.add_widget(btn)
        return layout

    def on_press_button(self, instance):
        print(f"Você apertou o botão")



if __name__ == "__main__":
    app = HBoxLayouExample()
    app.run()
'''

# Linguagem de design KV: permite a separação da lógica e interface da aplicação (model-view-controller)
#basta criar um arquivo com extensão (kv) om o primeiro nome da classe em minúsculo, e então, definir os atributos


from kivy.app import App
from kivy.uix.button import Button

class ButtonApp(App):
    def build(self):
        return Button()
    def on_press_button(self):
        print('ok')

if __name__ == "__main__":
    app = ButtonApp()
    app.run()