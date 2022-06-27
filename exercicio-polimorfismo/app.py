from classes.catalogo import Catalogo
from classes.transporteTerrestre import TransporteTerrestre
from classes.transporteAquatico import TransporteAquatico
from classes.transporteAereo import TransporteAereo

carro = TransporteTerrestre('Carro', 1.8, 5, .5, 160.5, 'GTX-130', 'Liga leve')
moto = TransporteTerrestre('Moto', 1.05, 2, .250, 250.75, 'Quad Core', 'Super Esporte')
caminhao = TransporteTerrestre('Caminhão', 3.5, 15, 22, 120, 'Ultra Max', 'Largas')

aviao = TransporteAereo('Avião', 5, 50, 5, 300, 7.5, 75)
balao = TransporteAereo('Balão', 21.5, 5, .3, 6, 6, 10)

submarino = TransporteAquatico('Submarino', 7, 75, 3.66, 60, 15, 2)
navio = TransporteAquatico('Navio', 25, 250, 80, 25.65, 35, 17)

transportes = [carro, moto, caminhao, aviao, balao, submarino, navio]

system = Catalogo('TranSystem', transportes)

system.iniciar()
