from time import sleep
import neat
import pickle
from Tetris import Tetris
import os


print("current working directory: ", os.getcwd())
sleep(1)

def type_to_float(type):
    if type == "I": return 0
    if type == "J": return 1
    if type == "L": return 2
    if type == "O": return 3
    if type == "S": return 4
    if type == "T": return 5
    if type == "Z": return 6

def neat_in_tetris(chosen_game_input):
    if chosen_game_input == 0:
        return "Q"
    elif chosen_game_input == 1:
        return "W"
    elif chosen_game_input == 2:
        return "E"
    elif chosen_game_input == 3:
        return "A"
    elif chosen_game_input == 4:
        return "S"
    elif chosen_game_input == 5:
        return "D"
    elif chosen_game_input == 6:
        return "SS"

def anzahl_Löcher(board):
    anzahl = 0
    for col in range(10):
        last_field = 0
        for row in board:
            if last_field == 1 and row[col] == 0:
                anzahl += 1
            last_field = row[col]
    return anzahl

        


def determineFitness(genomes, lconfig):
    highscore_fitness = 0
    for genome_id, genome in genomes:
        network = neat.nn.FeedForwardNetwork.create(genome, lconfig)

        tetris = Tetris()

        genome_fitness = 0

        for move in range(200):

            anzahl = anzahl_Löcher(tetris.gamestate()['board'])

            gameInput = (
                *[float(cell) for row in tetris.gamestate()['fullBoard'] for cell in row],
                type_to_float(tetris.gamestate()['current']['type']),
                type_to_float(tetris.gamestate()['next']),
                type_to_float(tetris.gamestate()['held']),
                float(tetris.gamestate()['canHold']),
                float(tetris.gamestate()['score']),
                float(anzahl)
            )
        


            print(anzahl)
            
            if anzahl > 0:
                genome_fitness -= anzahl * 0.5
            else:
                genome_fitness += 2

            if tetris.gamestate()['cleared'] != 0:
                print(f"cleared: {tetris.gamestate()['cleared']} score: {tetris.gamestate()['score']}") 
                sleep(10)

#            if tetris.gamestate()['board'][16] == [0]*10:
#                genome_fitness += 1
#                print("über Zeile 4")

            output = network.activate(gameInput)

            chosen_game_input = output.index(max(output))
            print(f"neat macht: {chosen_game_input}")
            
            tetris.input(neat_in_tetris(chosen_game_input))

            
            if tetris.death_reason is not None:
                break
            else:
                tetris.printboard(tetris.gamestate()['fullBoard'])
                print(f'Score: {tetris.gamestate()['score']} fitness: {genome_fitness}')
            
            tetris.input('S')

        genome_fitness += tetris.gamestate()['score']

        if genome_fitness > highscore_fitness:
            highscore_fitness = genome_fitness
        genome.fitness = genome_fitness

        print(f'Current: {genome_fitness} Max:{highscore_fitness}')        

config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                     neat.DefaultSpeciesSet, neat.DefaultStagnation,
                     'config')

population = neat.Population(config)
population.add_reporter(neat.StdOutReporter(True))

checkpoint = neat.Checkpointer(generation_interval=20, time_interval_seconds = None, filename_prefix="tetris_neat_checkpoint-")
population.add_reporter(checkpoint)

winner = population.run(determineFitness)

with open("tetris_neat_winner.pkl", "wb") as f:
    pickle.dump(winner, f)
print("winner saved to tetris_neat_winner.pkl")

#https://neat-python.readthedocs.io/en/latest/troubleshooting.html
