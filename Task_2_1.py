class Animal:

    def __init__(self, name, color, voice):

        self.name = name
        self.color = color
        self.voice = voice

    def get_voice(self):
        string = 'It says ' + self.voice + '.'
        return string


def animal_description(animal):
    print(f'{animal.name} is {animal.color}. {animal.get_voice()}')