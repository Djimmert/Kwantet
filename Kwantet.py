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
		
class KwantumkwartetTracker:
		def **init**(self, players, pot_size):
		self.players = players
		self.pot_size = pot_size
		self.materialized_cards = {}  # card_name: current_owner
		self.card_history = []  # List of (turn, player, card, action, result)
		self.player_hands = {player: [] for player in players}
		self.completed_quartets = {player: [] for player in players}
		self.turn_count = 0
		
		```
		def ask_card(self, asking_player, asked_player, card_name, response):
		    """Record a card request and response"""
		    self.turn_count += 1
		    
		    # Check if card already exists
		    if card_name in self.materialized_cards:
		        current_owner = self.materialized_cards[card_name]
		        if response == "yes" and current_owner != asked_player:
		            return self._handle_paradox(card_name, current_owner, asked_player)
		        elif response == "no" and current_owner == asked_player:
		            return self._handle_paradox(card_name, current_owner, asked_player)
		    
		    # Record the action
		    self.card_history.append((self.turn_count, asking_player, asked_player, card_name, response))
		    
		    if response == "yes":
		        # Materialize the card and transfer it
		        self.materialized_cards[card_name] = asking_player
		        if card_name in self.player_hands[asked_player]:
		            self.player_hands[asked_player].remove(card_name)
		        self.player_hands[asking_player].append(card_name)
		        return {"status": "success", "message": f"{card_name} transferred to {asking_player}"}
		    
		    return {"status": "success", "message": f"{asked_player} doesn't have {card_name}"}
	
	def complete_quartet(self, player, quartet_cards):
	    """Attempt to complete a quartet"""
	    # Check if all cards are in player's hand
	    for card in quartet_cards:
	        if card not in self.player_hands[player]:
	            return {"status": "error", "message": f"{player} doesn't have {card}"}
	    
	    # Check if it's a valid quartet (you might want to add quartet validation logic here)
	    if len(quartet_cards) != 4:
	        return {"status": "error", "message": "A quartet must have exactly 4 cards"}
	    
	    # Remove cards from hand and add to completed quartets
	    for card in quartet_cards:
	        self.player_hands[player].remove(card)
	    self.completed_quartets[player].append(quartet_cards)
	    
	    return {"status": "success", "message": f"{player} completed quartet: {quartet_cards}"}
	
	def _handle_paradox(self, card_name, current_owner, claimed_owner):
	    """Handle quantum paradox by finding the problematic turn"""
	    paradox_info = {
	        "status": "paradox",
	        "card": card_name,
	        "current_owner": current_owner,
	        "claimed_owner": claimed_owner,
	        "problematic_turns": []
	    }
	    
	    # Find all turns involving this card
	    for turn_data in self.card_history:
	        turn, asking, asked, card, response = turn_data
	        if card == card_name:
	            paradox_info["problematic_turns"].append({
	                "turn": turn,
	                "asking_player": asking,
	                "asked_player": asked,
	                "response": response
	            })
	    
	    return paradox_info

	def get_game_state(self):
	    """Get current game state"""
	    return {
	        "turn": self.turn_count,
	        "materialized_cards": self.materialized_cards.copy(),
	        "player_hands": {p: hand.copy() for p, hand in self.player_hands.items()},
	        "completed_quartets": {p: quarts.copy() for p, quarts in self.completed_quartets.items()},
	        "total_cards_in_play": len(self.materialized_cards),
	        "pot_size": self.pot_size
	    }
	
	def check_pot_overflow(self):
	    """Check if we're approaching pot size limit"""
	    current_cards = len(self.materialized_cards)
	    if current_cards >= self.pot_size:
	        return {
	            "status": "warning",
	            "message": f"Pot is full ({current_cards}/{self.pot_size}). Consider saying 'no' to new cards."
	        }
	    return {"status": "ok"}
	
	def revert_to_turn(self, target_turn):
	    """Revert game state to a specific turn (for paradox resolution)"""
	    # Remove all actions after target_turn
	    self.card_history = [turn_data for turn_data in self.card_history if turn_data[0] <= target_turn]
	    
	    # Rebuild game state from history
	    self.materialized_cards = {}
	    self.player_hands = {player: [] for player in self.players}
	    self.completed_quartets = {player: [] for player in self.players}
	    
	    for turn_data in self.card_history:
	        turn, asking, asked, card, response = turn_data
	        if response == "yes":
	            self.materialized_cards[card] = asking
	            if card in self.player_hands[asked]:
	                self.player_hands[asked].remove(card)
	            self.player_hands[asking].append(card)
	    
	    self.turn_count = target_turn
	    return {"status": "success", "message": f"Reverted to turn {target_turn}"}
	```
	
	# Example usage and testing

def main2():
	# Initialize game
	players = [“Alice”, “Bob”, “Charlie”]
	pot_size = 16  # 4 players × 4 cards minimum
	game = KwantumkwartetTracker(players, pot_size)
	
	```
	print("=== Kwantumkwartet Consistency Tracker ===\n")
	
	# Example game sequence
	print("Turn 1: Alice asks Bob for 'Scientist Einstein'")
	result = game.ask_card("Alice", "Bob", "Scientist Einstein", "yes")
	print(f"Result: {result}\n")
	
	print("Turn 2: Bob asks Charlie for 'Scientist Newton'")
	result = game.ask_card("Bob", "Charlie", "Scientist Newton", "no")
	print(f"Result: {result}\n")
	
	print("Turn 3: Charlie asks Alice for 'Scientist Einstein'")
	result = game.ask_card("Charlie", "Alice", "Scientist Einstein", "yes")
	print(f"Result: {result}\n")
	
	# Try to create a paradox
	print("Turn 4: Alice asks Bob for 'Scientist Einstein' (paradox!)")
	result = game.ask_card("Alice", "Bob", "Scientist Einstein", "yes")
	print(f"Result: {result}\n")
	
	# Show game state
	print("Current game state:")
	state = game.get_game_state()
	for key, value in state.items():
	    print(f"  {key}: {value}")
	
	# Check pot status
	print(f"\nPot status: {game.check_pot_overflow()}")
	```

if __name__ == '__main__':
	AppKwantet().run()
		