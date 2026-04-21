# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 10:38:14 2026

@author: Laraa
"""

from classes.airport import Airport
from classes.airline import Airline
from classes.terminal import Terminal
from classes.voo import Voo

# Define o caminho para a base de dados enviada
# (Ajuste o caminho 'data/' se o ficheiro estiver noutra pasta)
db_file = 'data/Airport airlines - original (com dados do csv).db'
# Lê a informação das classes a partir da base de dados
Airport.read(db_file)
Airline.read(db_file)
Terminal.read(db_file)
Voo.read(db_file)

# Cria três aeroportos, caso a tabela esteja vazia
if len(Airport.lst) == 0:
    a1 = Airport(0, "1990-01-01", "Aeroporto Francisco Sá Carneiro")
    a2 = Airport.from_string("0;1942-10-15;Aeroporto Humberto Delgado")
    a3 = Airport(0, "1965-07-11", "Aeroporto de Faro")
    
    Airport.insert(a1.id)
    Airport.insert(a2.id)
    Airport.insert(a3.id)

# Ordena os aeroportos por nome (ordem ascendente)
print('Aeroportos ordenados por nome:')
Airport.sort('_name')
for id in Airport.lst:
    print(Airport.obj[id])

# Cria duas companhias aéreas
if len(Airline.lst) == 0:
    al1 = Airline(0, 'TAP Air Portugal', 'Premium')
    al2 = Airline.from_string("0;Ryanair;Low Cost")
    
    Airline.insert(al1.id)
    Airline.insert(al2.id)

# Cria terminais para um aeroporto (garantindo que o aeroporto existe para a integridade referencial)
if len(Terminal.lst) == 0 and len(Airport.lst) > 0:
    # Usa o ID do primeiro aeroporto da lista para respeitar a integridade
    airport_id = Airport.lst[0] 
    t1 = Terminal(0, 'Terminal 1 - Partidas Principais', airport_id)
    t2 = Terminal(0, 'Terminal 2 - Chegadas', airport_id)
    
    Terminal.insert(t1.id)
    Terminal.insert(t2.id)

# Cria três voos (Voo)
if len(Voo.lst) == 0 and len(Airport.lst) > 0 and len(Airline.lst) > 0:
    # Pega em ids existentes
    airport_id = Airport.lst[0]
    airline_id = Airline.lst[0]
    airline2_id = Airline.lst[-1]
        
    v1 = Voo(0, airline_id, airport_id, '2026-05-15', 120)
    v2 = Voo(0, airline2_id, airport_id, '2026-05-16', 45)
    v3 = Voo(0, airline_id, airport_id, '2026-05-17', 250)
    Voo.insert(v1.id)
    Voo.insert(v2.id)
    Voo.insert(v3.id)

# Ordena voos por custo do bilhete
print('\nVoos ordenados por preço do bilhete (ticket_cost):')
Voo.sort('_ticket_cost')
for id in Voo.lst:
    print(Voo.obj[id])