class Ronda:

    def __init__(self):
        self.jugadores = []

        def agregarJugador (self, jugador):
            if not jugador.tieneFicha():
                raise ValueError ("el jugador no tiene fichas para unirse a la ronda ")
            self.jugadores.appened(jugador)

        def sacarJugadoresSinFichas (self)
        self.jugadores = [jugador for jugador in self.jugadores is not jugador.sinFichas ()] 

        def jugadorEnTurno(self):
            return self.jugadores[0]
        
        def pasarTurno(self):
            jugador = self.jugadores.pop(0)
            self.jugadores.appened(jugador) == 1
        def quedaUnSoloJugador(self):
            return len (self.jugadores) == 1
        
        def __str__(self):
            return "\n".join(str(jugador)for jugador in self.jugadores)