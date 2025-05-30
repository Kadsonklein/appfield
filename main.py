from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
import requests
import os
import certifi


os.environ["SSL_CERT_FILE"] = certifi.where()

class HomePage(Screen):
    pass

class Config(Screen):
    pass

GUI = Builder.load_file("main.kv")
class MainApp(App):
    def build(self):
        return GUI
    def on_start(self):
        pass

    def mudar_tela(self, id_tela):
        gerenciador_telas = self.root.ids["screen_manager"]
        gerenciador_telas.current = id_tela

MainApp().run()
