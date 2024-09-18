"""
This code is adapted from the AIMA website so that it
interfaces with the Berkley Pacman code and allows
for a problem to be explored with nonuniformed costs.

Molloy Dec 2022

"""

import sys
import util
import search

class MapState:
    romania_map = dict(
    Arad=dict(Zerind=75, Sibiu=140, Timisoara=118),
    Bucharest=dict(Urziceni=85, Pitesti=101, Giurgiu=90, Fagaras=211),
    Craiova=dict(Drobeta=120, Rimnicu=146, Pitesti=138),
    Drobeta=dict(Craiova=120, Mehadia=75),
    Eforie=dict(Hirsova=86),
    Fagaras=dict(Bucharest=211, Sibiu=99),
    Hirsova=dict(Eforie=86, Urziceni=98),
    Iasi=dict(Vaslui=92, Neamt=87),
    Lugoj=dict(Timisoara=111, Mehadia=70),
    Oradea=dict(Zerind=71, Sibiu=151),
    Pitesti=dict(Bucharest=101,Craiova=146,Rimnicu=97),
    Rimnicu=dict(Craiova=146, Pitesti=97,Sibiu=80),
    Giurgiu=dict(Bucharest=90),
    Mehadia=dict(Lugoj=70, Drobeta=75),
    Sibiu=dict(Arad=140,Oradea=151,Fagaras=99,Rimnicu=80),
    Neamt=dict(Iasi=87),
    Timisoara=dict(Arad=118, Lugoj=111),
    Urziceni=dict(Bucharest=85, Hirsova=98, Vaslui=142),
    Vaslui=dict(Iasi=92, Urziceni=142),
    Zerind = dict(Arad=75,Oradea=71))


    """
    """
    def __init__( self, city ):
        if city in self.romania_map:
            self.city = city
        else:
            print("Illegal city state", city)
            sys.exit(-1)

    def __eq__ (self, other):
        return self.city == other.city

    def __hash__(self):
        return hash(self.city)


    def legalMoves( self ):
        return [moves for moves in self.romania_map[self.city]]

    def result(self, move):
        if move in self.romania_map[self.city]:
            return MapState(move), self.romania_map[self.city][move]
        else:
            print("Illegal move:", self.city, move)
            sys.exit(-1)



class MapPuzzleProblem(search.SearchProblem):
    """
      Implementation of a SearchProblem for the  Romania Map

      Each state is represented by an instance MapState (a city)
    """
    def __init__(self, startingCity, goalCity):
        self.startState = MapState(startingCity)
        self.goalState = MapState(goalCity)

    def getStartState(self):
        return self.startState

    def isGoalState(self, state):
        return self.goalState == state

    def getSuccessors(self,state):
        """
          Returns list of (successor, action, stepCost) pairs where
          each succesor is either left, right, up, or down
          from the original state and the cost is 1.0 for each
        """
        succ = []
        for a in state.legalMoves():
            nextState, cost = state.result(a)
            succ.append((nextState, a, cost))
        return succ

def main():
    problem = MapPuzzleProblem("Arad","Bucharest")

    path, cost, explored, pushed = search.depthFirstSearch(problem)
    print("DFS", path, cost, explored, pushed)

    print() 

    path, cost, explored, pushed = search.breadthFirstSearch(problem)
    print("BFS", path, cost, explored, pushed)

if __name__ == '__main__':
    main()

