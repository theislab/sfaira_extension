import os
import pandas


class GenomeContainer:
    available_genomes = []

    def __init__(self):
        self.genomes = {

        }
        self.genome_sizes = {

        }

    def read_local_csv(self, genome):
        return pandas.read_csv(os.path.join(str(os.path.dirname(__file__)), self.genomes[genome]))
