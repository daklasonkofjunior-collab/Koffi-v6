from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class KoffiV6App(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=50, spacing=20)
        label = Label(text='KOFFI V6\nApp OK!', font_size=30, halign='center')
        btn = Button(text='Clique moi', size_hint=(1, 0.3))
        btn.bind(on_press=lambda x: setattr(label, 'text', 'CA MARCHE FREROT! 🔥'))
        layout.add_widget(label)
        layout.add_widget(btn)
        return layout

KoffiV6App().run()
