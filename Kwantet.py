#!/Users/djimcasander/Documents/development_local/Python/Kwantet/Kwantet_venv/bin/python3
# Version: 1.2.0
import sys
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.logger import Logger, LOG_LEVELS
from kivy.uix.button import Button

def main() -> None:
	Logger.setLevel(LOG_LEVELS["critical"])
	AppKwantet().run()

	# arguments = sys.argv[1:]

	# for speler in spelers:
	# 	overview[speler] = {"onbekende_kaarten": 0, "bekende_kaarten": ({"kaart": "", "categorie": ""})}
	# overview = {}

	# beurt_count = 0
	# while True:
	# 	input_beurt = input() # vrager_naam | gevraagde_naam | kaart | categorie | resultaat
	# 	beurt_instance = Beurt(beurt_count)
	# 	beurt_count += 1

class GridLayoutKwantet(GridLayout):
	def __init__(self, **kwargs) -> None:
		super(GridLayoutKwantet, self).__init__(**kwargs)

		self.cols = 5

		self.add_widget(Label(text="Hello World"))
		self.name = TextInput(multiline=False)
		self.add_widget(self.name)

class AppKwantet(App):
	def build(self) -> None:
		return GridLayoutKwantet()

class Kaarten:
	def __init__(self, onbekende_kaarten) -> None:
		self.onbekende_kaarten = onbekende_kaarten
		self.bekende_kaarten: set(Kaart)

	def vraag(self, kaart) -> None:
		if kaart in self.bekende_kaarten:
			pass
		else:
			self.bekende_kaarten.add()


class Speler:
	def __init__(self, speler_name) -> None:
		self.speler_name = speler_name
		self.speler_hand = {}
		for speler in speler_count:
			speler_hand

class Categorie:
	def __init__(self, categorie_name) -> None:
		self.categorie_name = categorie_name
		self.categorie_kaarten: set(Kaart)
		self.kwartet_door: None | Speler
		self.kwartet_door = None

	def wordt_kwartet(self, speler) -> None:
		self.kwartet_door = speler
		speler.kwartetten.add(self)

class Kaart(Categorie):
	def __init__(self, categorie_name, kaart_name):
		super().__init__(categorie_name)
		self.kaart_name = kaart_name

class Beurt:
	def __init__(self, beurt_count, vrager_name, gevraagde_name, kaart, categorie, uitslag):
		self.beurt_count = beurt_count
		
		self.vrager_name = vrager_name
		self.gevraagde_name: Speler
		self.kaart: Kaart
		self.categorie: Categorie
		self.uitslag: bool

		beurt_count_check()
		

	def beurt_count_check(self):
		if beurt_count < self.known_kaarten:
			print("error")

	def vrager_name_check(self):
		pass

if __name__ == '__main__':
	AppKwantet().run()
		