"""
This file demonstrates two different styles of tests (one doctest and one
unittest). These will both pass when you run "manage.py test".

Replace these with more appropriate tests for your application.
"""

from django.test import TestCase
from moip import MoIP

class MoIPLibTest(TestCase):

    def test_basic_usage(self):
        moip = MoIP(razao="Razao",valor="150.00")
        self.failUnlessEqual(moip.get_xml(),'<EnviarInstrucao><InstrucaoUnica><Razao>Razao</Razao><Valores><Valor moeda="BRL">150.00</Valor></Valores></InstrucaoUnica></EnviarInstrucao>')


#class SimpleTest(TestCase):
    #def test_basic_addition(self):
        #"""
        #Tests that 1 + 1 always equals 2.
        #"""
        #self.failUnlessEqual(1 + 1, 2)

#__test__ = {"doctest": """
#Another way to test that 1 + 1 is equal to 2.

#>>> 1 + 1 == 2
#True
#"""}

