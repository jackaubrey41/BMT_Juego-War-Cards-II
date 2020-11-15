"""
SEASON 2
WAR CARDS exercice ROUND II
"""
# Immport random library
# https://www.w3schools.com/python/module_random.asp
import random
# to use shuffle metod
# https://www.w3schools.com/python/ref_random_shuffle.asp

# Definición variables globales (set up juego)

# suits
suits = ("Hearts", "Diamonds", "Spades", "Clubs")

# Ranks
ranks = ("Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "As")

# Rank > Value
# Definimos un diccionario
values = {
	"Two": 2,
	"Three": 3, 
	"Four": 4, 
	"Five": 5, 
	"Six": 6, 
	"Seven": 7, 
	"Eight": 8, 
	"Nine": 9, 
	"Ten": 10, 
	"Jack": 11, 
	"Queen": 12, 
	"King": 13, 
	"As": 14
}

# iniciar el juego


# crear carta: palo (suit), rank (nombre), valor (value)
class Card():

	def __init__(self, suit, rank):
		self.suit = suit
		self.rank = rank
		self.value = values[rank]

	def __str__(self):
		return self.rank + " of " + self.suit


#carta = Card("Hearts", "As")
#print(carta.suit)
#print(carta.rank)
#print(carta)
#as_de_corazones = Card("Hearts", "As")
#tres_de_diamantes = Card("Diamonds", "Three")
#print(as_de_corazones.value)
#print(tres_de_diamantes.value)
#print(as_de_corazones.value >= tres_de_diamantes.value)

class Deck():
  def __init__(self):
    self.all_cards = []
    
    for suit in suits:
        for rank in ranks: 
          created_card = Card(suit, rank)
          self.all_cards.append(created_card)

  def __len__(self):
	  return len(self.all_cards)
	
  def __str__(self):
	  return f'This deck has {len(self.all_cards)} cards.'

  def shuffle(self):
    random.shuffle(self.all_cards)
    
  def deal_one(self):
    return self.all_cards.pop()

"""
#test de baraja
baraja = Deck()
print("Sacar carta:")
my_card = baraja.deal_one()
print(my_card)
print(len(baraja))
"""

# crear jugadores
class Player():
  def __init__(self, name):
    self.name = name
    self.my_all_cards = []
#https://www.w3schools.com/python/python_lists.asp
#metodo no funciona correctamente
  def remove_one():
#it takes the last card at list self.my_all_cards
    return self.my_all_cards.pop()
#no funciona
# def add_cards():
#    return self.my_all_cards.append()
#prueba alternativa
#modificado método añadiendo card de argumento
#sino no sabemos que hemos de añadir
  def add_cards(card):
    return self.my_all_cards.append(card)

  def __len__(self):
    return len(self.my_all_cards)
    
  def __str__(self):
    return f'Player {self.name} has {len(self.my_all_cards)} cards.'



#repartimos a cada jugador hasta agotar las cartas
def repartimos_cartas(baraja_a_repartir, jugadores_en_mesa):
  
  barajax = baraja_a_repartir
  lista_jugadoresx = jugadores_en_mesa

  while len(barajax) != 0:
    for jugadorx in lista_jugadoresx:
      #nos aseguramos de tener cartas a repartir al jugador
      if len(barajax) != 0:
    # sacamos la última carta
        carta_juego = barajax.all_cards[len(barajax)-1] 
      # sacamos la carta de la baraja
        barajax.deal_one()
    # la entregamos al jugador
        jugadorx.my_all_cards.append(carta_juego)
    # si hemos finalizado las cartas nos salimos
        print(carta_juego)
        print(jugadorx)
      else:
        print ("No card for you my friend")
  return
  
"""
# ¡¡¡¡ OJO ¡¡¡¡¡
# no funciona con el metodo
# jugador1.add_cards(carta_juego)
"""

# war Play

def play_war_two_players(lista_juagadores_en_war):
  lista_empate = []
  jugador1 = lista_juagadores_en_war[0]
  jugador2 = lista_juagadores_en_war[1]
  carta_en_juego1 = jugador1.my_all_cards[len(jugador1)-1]
  carta_en_juego2 = jugador2.my_all_cards[len(jugador2)-1]

  while carta_en_juego1.value == carta_en_juego2.value:
    # acumulamos cartas en caso de EMPATE en una lista
    
    lista_empate.append(carta_en_juego1)
    lista_empate.append(carta_en_juego2)
    print ("EMPATE")
    #el metodo remove_one() no funciona correctamente
    jugador1.my_all_cards.pop()
    jugador2.my_all_cards.pop()
    #for jugadorx in lista_jugadores:
    #jugadorx.remove_one
    #jugamos las siguientes cartas
    carta_en_juego1 = jugador1.my_all_cards[len(jugador1)-1]
    carta_en_juego2 = jugador2.my_all_cards[len(jugador2)-1]

  if carta_en_juego1.value > carta_en_juego2.value:
    print ("1 GANA")
    jugador1.my_all_cards.insert(0,carta_en_juego2)
    jugador1.my_all_cards.extend(lista_empate)
    jugador2.my_all_cards.pop()

  else:
    print ("2 GANA")
    jugador2.my_all_cards.insert(0,carta_en_juego1)
    jugador2.my_all_cards.extend(lista_empate)
    jugador1.my_all_cards.pop()
  
  #es necesario?? o ya se modifican al modificar jugador1 y jugador2
  #player1.my_all_cards = jugador1.my_all_cards
  #player2.my_all_cards = jugador2.my_all_cards
  print(jugador1)
  print(jugador2)

  return


"""
INICIAMOS LA PARTIDA
"""

#creamos baraja
baraja1 = Deck()

#inicializamos una lista de jugadores
lista_jugadores = [Player("Mike"), Player("Jordi")]

# barajamos
baraja1.shuffle()

#repartimos cartas de la baraja creada en la lista de jugadores
repartimos_cartas(baraja1,lista_jugadores)

# comprobamos que el juego no ha finalizado
#alguine tiene 0 cartas ?

#inicializamos variables?
follow_game = True
i = 0

while follow_game == True:
  #primero recorre la lista de jugadores para ver si tienen cartas
  for jugadorx in lista_jugadores:
    if len(jugadorx) == 0:
      follow_game = False 
      print (jugadorx.name,"PIERDE")
  
  #si todos los jugadores tienen carta, entonces jugamos
  if follow_game == True:
    i += 1
    play_war_two_players(lista_jugadores)
    print("sigue juego", i, "veces")
  