from src.main.python.specie import Specie


class Pokemon(Specie):
    def __int__(self, *args, name, stats, lvl, moves):
        super(Pokemon, self).__int__()
        self.id = None
        self.name = name
        self.lvl = lvl
        self.moves = moves

    def do_damage(self, other_pokemon):
        pass

    def receive_damage(self, other_pokemon_move):
        pass

    def change_status(self, changed_status):
        pass

    def receive_potion(self, potion_received):
        pass
