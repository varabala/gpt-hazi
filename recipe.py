class Recipe:
    def __init__(self, id, title, instructions, image_name, ingredients):
        self.id = id
        self.title = title
        self.instructions = instructions
        self.image_name = image_name
        self.ingredients = ingredients

    def display(self):
        print(f"Cím: {self.title}")
        print(f"Utasítások: {self.instructions}")
        print("Hozzávalók:")
        for ingredient in self.ingredients:
            print(f" - {ingredient}")
