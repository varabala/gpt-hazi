import PySimpleGUI as sg
from PIL import Image


sg.theme('LightBlue2')

logo_path = 'recipe_finder_logo.png'
info_text = 'info.txt'

receptek = ["Recept 1", "Recept 2", "Recept 3"]

image = Image.open(logo_path)
image.thumbnail((130, 130))
temp_path = 'temp_logo.png'
image.save(temp_path)



image_column = [
    [sg.Image(temp_path)]
]



ingredients_search_layout = [
    [sg.Text("Enter ingredients:", size=(16, 1)), sg.InputText(size=(38, 1)), sg.Button("Add")],
    [sg.Listbox(values=receptek, size=(60, 18), key='INGREDIENTS_LIST')]
]

disliked_ingredients_search_layout = [
    [sg.Text("Enter ingredients you don't like:", size=(25, 1)), sg.InputText(size=(28, 1)), sg.Button("Add")],
    [sg.Listbox(values=receptek, size=(60, 18), key='DISLIKED_INGREDIENTS_LIST')],
    [sg.Text('', size=(55, 1)), sg.Button("Search")]
]

column1 = [
    [sg.Text("Pick a recipe:", size=(16, 1), font=("Helvetica", 14, 'bold'))],
    [ sg.Listbox(values=receptek, size=(60, 18), key='RESULTS_LIST')]
]

column2 = [[sg.Multiline(default_text="Recipe details:", size=(80, 20), key='RECIPE_DETAILS')]
]

info_tab = [
    [sg.Multiline(info_text, size=(750, 550), font=("Helvetica", 14), key='-INFO-', disabled=True)]
]
search_tab = [[sg.Column(ingredients_search_layout, justification='center')],
              [sg.Column(disliked_ingredients_search_layout, justification='center')],
]

result_tab = [[sg.Column(column1)], [sg.Column(column2)]]

tab_group_layout = [[
    sg.Tab('Search', search_tab),
    sg.Tab('Results', result_tab, key='-RESULTS_TAB-'),
    sg.Tab('Info', info_tab, key='-INFO_TAB-')
]]

layout = [
    #[sg.Column([[sg.Text("Recipe Finder", font=("Helvetica", 36), justification='center')]], justification='center')],
    [sg.Column(image_column, justification='center')],
    [sg.TabGroup(tab_group_layout, size=(1000, 550), enable_events=True, key='-TABGROUP-')],
    [sg.Button("Save"), sg.Button("Share"), sg.Button("Exit")]
]


window = sg.Window("Recipe Finder App", layout, size=(1024, 768))


while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    elif event == 'Search':
        # Itt végezheted el a keresési logikát és frissítheted a listát
        pass
    elif event == 'RESULTS_LIST':
        # A kiválasztott recept részleteinek megjelenítése
        selected_recipe = values['RESULTS_LIST'][0]  # Például a kiválasztott recept neve
        window['RECIPE_DETAILS'].update(f"A kiválasztott recept részletei: {selected_recipe}")

window.close()

