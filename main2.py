import PySimpleGUI as sg
from data_manager import DataManager
from recipe import Recept

class MainApplication:
    def __init__(self):
        self.data_manager = DataManager()
        self.setup_window()

    def setup_window(self):
        # Itt hozd létre a GUI elemeit és az ablakot
        pass

    def run(self):
        # Itt futtass egy eseménykezelő hurkot
        pass

if __name__ == "__main__":
    app = MainApplication()
    app.run()
