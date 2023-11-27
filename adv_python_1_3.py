import abc


class PokemonTrainInterface(abc.ABC):
    @abc.abstractmethod
    def increase_experience(self, value):
        pass

    @property
    @abc.abstractmethod
    def experience(self):
        pass


class Pokemon(PokemonTrainInterface):
    def __init__(self, name: str, poketype: str):
        self.name = name
        self.poketype = poketype
        self._experience = 100

    def increase_experience(self, value):
        self.experience = self.experience + value

    @property
    def experience(self):
        return self._experience

    @experience.setter
    def experience(self, value):
        self._experience = value


if __name__ == '__main__':
    pokemon = Pokemon(name='Pikachu', poketype='electric')
    pokemon.increase_experience(100)
    assert pokemon.experience == 200, 'Try harder, Neeman'
    print(pokemon.experience)
    pokemon.increase_experience(100)
    print(pokemon.experience)
