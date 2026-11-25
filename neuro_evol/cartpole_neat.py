"""Solve CartPole with NEAT neuro-evolution.

Install the extra dependency with ``pip install neat-python`` before running.
"""

from pathlib import Path

import neat

import CartPole_env as env


# Each genome becomes a neural network that receives the four CartPole
# observations and produces one score, mapped to discrete action 0 or 1.
def evaluate_genomes(genomes, config):
    for genome_id, genome in genomes:
        network = neat.nn.FeedForwardNetwork.create(genome, config)

        def policy(observation):
            return int(network.activate(observation)[0] > 0)

        # Average over a few episodes to make fitness less noisy without making
        # every generation too slow for a classroom demonstration.
        genome.fitness = env.evaluate_policy(
            policy,
            n_episodes=5,
            episode_len=500,
        )[0]


def main():
    config_path = Path(__file__).with_name("CartPole_neat.ini")
    config = neat.Config(
        neat.DefaultGenome,
        neat.DefaultReproduction,
        neat.DefaultSpeciesSet,
        neat.DefaultStagnation,
        str(config_path),
    )

    population = neat.Population(config)
    population.add_reporter(neat.StdOutReporter(True))
    population.add_reporter(neat.StatisticsReporter())

    # Stop after 50 generations or when the configured fitness threshold is met.
    winner = population.run(evaluate_genomes, 50)
    print("\nBest genome:\n", winner)

    winner_network = neat.nn.FeedForwardNetwork.create(winner, config)

    def best_policy(observation):
        return int(winner_network.activate(observation)[0] > 0)

    env.run_best_policy(best_policy)


if __name__ == "__main__":
    main()
