class EmojiMixin:
    @staticmethod
    def replace(text):
        return text.replace('grass', '🌿').replace('fire', '🔥')\
            .replace('water', '🌊').replace('electric', '⚡')

    def __str__(self):
        return f'{self.name}/{self.replace(self.poketype)}'


class BasePokemon:
    def __init__(self, name: str, poketype: str):
        self.name = name
        self.poketype = poketype

    def __str__(self):
        return f'{self.name}/{self.poketype}'


class Pokemon(EmojiMixin, BasePokemon):
    pass


if __name__ == '__main__':
    pokemon = Pokemon(name='Pikachu', poketype='electric')
    print(pokemon)
