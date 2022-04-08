class harmonia():

    def __init__(self):
        self.chords = ""
        self.instruments = [0,0,0]

    def set_instruments(self):
        self.instruments[0] = "guitar"
        self.instruments[1] = "bass"
        self.instruments[2] = "piano"

    def add_chords(self, chord):
        self.chords += chord + " "

class melodia():
    def __init__(self):
        self.melody = [0,0,0,0,0,0,0,0,0]
        self.instruments = [0,0,0]

    def set_instruments(self):
        self.instruments[0] = "voice"
        self.instruments[1] = "Keyboard"

    def set_melody(self,melody):
        self.melody = melody



class ritmo():
    def __init__(self):
        self.instruments = [0,0,0]

    def set_instruments(self):
        self.instruments[0] = "Drums"
        self.instruments[1] = "Clap"

    def set_bpm(self, new_bpm):
        self.bpm = new_bpm
    pass


class jazz(harmonia,melodia,ritmo):

    def choose_instruments(self):
        return super().set_instruments()

    def print_inst(self):
        print(self.instruments)

    def def_melody(self, mel):
        super().set_melody(mel)

    def def_chords(self, chords):
        super().add_chords(chords)


musica1 = jazz()
print(musica1.__class__.__mro__)
musica1.choose_instruments()
#O retorno é da classe de maior prioridade, que é a "harmonia"
musica1.print_inst()
musica1.def_melody(["do","re","mi","re","do"])
print(musica1.melody)
musica1.def_chords("Am")
musica1.def_chords("C")
musica1.def_chords("F")
musica1.def_chords("G")
print(musica1.chords)
