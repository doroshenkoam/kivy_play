from datetime import datetime

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock


class MainMenu(Screen):
    pass


class Creators(Screen):
    pass


class About(Screen):
    pass


class StartGame(Screen):
    def count(self, *varargs):
        self.start = datetime.now()
        Clock.schedule_interval(self.on_timeout, 1)

    def on_timeout(self, *args):
        d = datetime.now() - self.start
        self.label_time.text = datetime.utcfromtimestamp(d.total_seconds()).strftime(
            "%H.%M.%S"
        )

    def on_pre_enter(self):
        self.count(1)


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
