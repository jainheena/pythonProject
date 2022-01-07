class Apple:
    fruit_type = 'sweet fruit'

    def __init__(self, color, calories):
        self.color = color
        self.calories = calories


a1 = Apple('red', 40)
a2 = Apple('green', 60)
print(a1.fruit_type)
Apple.fruit_type = 'fruit'
print(a1.fruit_type)

