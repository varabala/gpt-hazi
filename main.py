import PySimpleGUI as sg
from PIL import Image
from data_manager import DataManager
from recipe import Recipe
import data_manager

class MainApplication:
    def __init__(self):
        self.data_manager = DataManager()
        self.ingredients = []
        self.disliked_ingredients = []
        self.results = []
        self.setup_window()
    def update_recipe_list(self):
        liked = self.ingredients
        disliked = self.disliked_ingredients
        recipes = self.data_manager.get_recept_by_ingredients(liked, disliked)
        self.window['RESULTS_LIST'].update(recipes)
    def setup_window(self):
        sg.theme('LightBlue2')

        logo_path = 'recipe_finder_logo.png'
        info_filename = 'info.txt'

        with open(info_filename, 'r', encoding='utf-8') as file:
            info_text = file.read()



        image = Image.open(logo_path)
        image.thumbnail((130, 130))
        temp_path = 'temp_logo.png'
        image.save(temp_path)

        image_column = [
            [sg.Image(temp_path)]
        ]
        ingredients_search_layout = [
            [sg.Text("Enter ingredients:", size=(16, 1), font=("Helvetica", 10, 'bold')),
             sg.InputText(size=(38, 1), key="INGREDIENT"), sg.Button("Add", key='ADD_INGREDIENT')],
            [sg.Listbox(values=self.ingredients, size=(60, 18), key='INGREDIENTS_LIST')]
        ]
        disliked_ingredients_search_layout = [
            [sg.Text("Enter ingredients you don't like:", size=(25, 1), font=("Helvetica", 9, 'bold')),
             sg.InputText(size=(28, 1), key="DISINGREDIENT"), sg.Button("Add", key='ADD_DISLIKED')],
            [sg.Listbox(values=self.disliked_ingredients, size=(60, 18), key='DISLIKED_INGREDIENTS_LIST')],
            [sg.Text('', size=(53, 1)), sg.Button("Search", key='SEARCH')]
        ]
        column1 = [
            [sg.Text("Pick a recipe:", size=(16, 1), font=("Helvetica", 14, 'bold'))],
            [sg.Listbox(values=self.results, size=(160, 18), key='RESULTS_LIST')]
        ]

        column2 = [
            [sg.Text("Recipe details:", size=(16, 1), font=("Helvetica", 14, 'bold'))],
            [sg.Multiline(size=(180, 20), key='RECIPE_DETAILS')],
            [sg.Text('', size=(153, 2)), sg.Button("Save", key='SAVE')]
        ]

        info_tab = [
            [sg.Multiline(info_text, size=(750, 550), font=("Helvetica", 14), key='-INFO-', disabled=True)]
        ]
        search_tab = [[sg.Column(ingredients_search_layout, justification='center')],
                      [sg.Column(disliked_ingredients_search_layout, justification='center')],
                      ]

        result_tab = [[sg.Column(column1, justification='center')], [sg.Column(column2, justification='center')]]

        tab_group_layout = [[
            sg.Tab('Search', search_tab),
            sg.Tab('Results', result_tab, key='-RESULTS_TAB-'),
            sg.Tab('Info', info_tab, key='-INFO_TAB-')
        ]]

        layout = [
            [sg.Column(image_column, justification='center')],
            [sg.TabGroup(tab_group_layout, size=(1000, 550), enable_events=True, key='-TABGROUP-')],
            [sg.Text('', size=(150, 2)), sg.Button("Clear", key='CLEAR_SEARCH'), sg.Button("Exit")]
        ]

        self.window = sg.Window("Recipe Finder App", layout, size=(1024, 768))

    def run(self):
        while True:
            event, values = self.window.read()
            if event == sg.WIN_CLOSED or event == 'Exit':
                break
            elif event == 'ADD_INGREDIENT':
                ingredient = values['INGREDIENT']
                self.ingredients.append(ingredient)
                self.window['INGREDIENT'].update('')
                self.window['INGREDIENTS_LIST'].update(self.ingredients)
            elif event == 'ADD_DISLIKED':
                disliked_ingredient = values['DISINGREDIENT']
                self.disliked_ingredients.append(disliked_ingredient)
                self.window['INGREDIENT'].update('')
                self.window['DISLIKED_INGREDIENTS_LIST'].update(self.disliked_ingredients)
            elif event == 'CLEAR_SEARCH':
                self.window['INGREDIENTS_LIST'].update([])
                self.window['DISLIKED_INGREDIENTS_LIST'].update([])
                self.window['RESULTS_LIST'].update([])
                self.window['RECIPE_DETAILS'].update([])
            elif event == 'SEARCH':
                self.update_recipe_list()
            elif event == 'SAVE':
                pass

if __name__ == "__main__":
    app = MainApplication()
    app.run()
