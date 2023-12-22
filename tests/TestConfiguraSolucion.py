import unittest

from deap import tools
from deap import base, creator

import sys
sys.path.append('.')
sys.path.append('..')
sys.path.append('../evol_simple')

import evol_simple.DatosMochila as dm
import evol_simple.ConfiguracionSolucion as cs

class TestConfiguraSolucion(unittest.TestCase):

#    def __init__(self):
#        self.toolbox = base.Toolbox()
#        cs.configuraPoblacion(self.toolbox)

    def setUp(self):
        self.toolbox = base.Toolbox()
        cs.configuraPoblacion(self.toolbox)
        
    def test_generate_individual(self):
        ind = self.toolbox.individual()
        self.assertEqual(len(dm.__weights__), len(ind))

    def test_generate_population(self):
        n = 10
        pop = self.toolbox.population(n=n)
        self.assertEqual(n, len(pop))


if __name__ == '__main__':
    unittest.main()