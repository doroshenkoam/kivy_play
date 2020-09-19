from datetime import timedelta

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen


class MainMenu(Screen):
    pass


class Creators(Screen):
    pass


class About(Screen):
    pass


class StartGame(Screen):
    pass


class MainApp(App):
    def build(self):
        # создаем менеджер экранов
        scren_manager = ScreenManager()
        scren_manager.add_widget(MainMenu(name="menu"))
        scren_manager.add_widget(Creators(name="creators"))
        scren_manager.add_widget(About(name="about"))
        scren_manager.add_widget(StartGame(name="start_game"))
        return scren_manager


if __name__ == "__main__":
    MainApp().run()
