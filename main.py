import PySimpleGUI as sg


sg.theme('lightGreen4')

receptek = ["Recept 1", "Recept 2", "Recept 3"]

# Az alkalmazás felületének kialakítása
layout = [
    [sg.Column([[sg.Text("Recipe Finder", font=("Helvetica", 36), justification='center')]], justification='center')],
    [sg.Text("Enter ingredients:"), sg.InputText()],
    [sg.Button("Search")],
    [sg.Text("Results:"), sg.Listbox(values=receptek, size=(40, 10), key='RESULTS_LIST')],
    [sg.Multiline(default_text="", size=(40, 10), key='RECIPE_DETAILS')],
    [sg.Button("Exit")],
    [sg.Button("Save"), sg.Button("Share"), sg.Button("Exit")]
    # Itt adhatsz hozzá további elemeket, mint például input mezők, gombok, stb.n
]

# Az ablak létrehozása a fentebb definiált elrendezéssel
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









