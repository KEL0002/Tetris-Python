import neat
from Tetris import Tetris

def determineFitness(genomes, lconfig):
    for genome_id, genome in genomes:
        network = neat.nn.FeedForwardNetwork.create(genome, lconfig)


        # Netzwerk testen

        tetris = Tetris()

        gameInput = (
            float(tetris.gamestate()['fullBoard']),
            float(tetris.gamestate()['current']['type']),
            float(tetris.gamestate()['next']),
            float(tetris.gamestate()['held']),
            float(tetris.gamestate()['canHold']),
            float(tetris.gamestate()['score']),
        )

        genome_fitness = 0

        #...




config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                     neat.DefaultSpeciesSet, neat.DefaultStagnation,
                     'config')

population = neat.Population(config)
population.add_reporter(neat.StdOutReporter(True))

winner = population.run(determineFitness, 300)