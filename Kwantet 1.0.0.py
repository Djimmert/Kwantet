#!/bin/python3

import sys

def main():
	arguments = sys.argv[1:]

	beurt = 0
	while True:
		input_beurt = input()
		beurt_instance = Beurt()
		beurt += 1

class Categorie:
	def __init__(self, name):
		self.name = name

class Kaart(Categorie):
	def __init__(self, name):
		super().__init__(name)

class Beurt:
	def __init__(self, beurt, vrager, gevraagde, ):
		self.beurt = beurt
		self.vrager
		self.gevraagde
		self.categorie
		self.kaart
		self.uitslag