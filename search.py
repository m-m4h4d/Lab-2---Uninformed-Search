# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util
import sys
import queue

from  collections import namedtuple

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()

class Node:
    def __init__(self, state, parent=None, action=None, path_cost=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost

    def get_path(self):
        """Returns the list of actions to reach this node."""
        node, path = self, []
        while node.parent is not None:
            path.append(node.action)
            node = node.parent
        return list(reversed(path))


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def whateverFirstSearch(problem, frontier):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Implement the graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))

    Argument:
       problem -- an obj of type SearchProblem (or a subclass of) to solve.

       frontier - The object to use for holding the frontier.  This
       dictates the type of search performed.
    Returns
       A tuple containing:
         - list of actions that reach the goal or None if goal not found
         - cost of actions or None if goal not found
         - number of items removed from the frontier
         - number of items added to the frontier.
    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


def depthFirstSearchStats(problem):
    """ Perform Depth-First Search and return the path and stats. """

    frontier = util.Stack()
    start_state = problem.getStartState()
    start_node = Node(state=start_state)
    frontier.push(start_node)
    explored = set()
    items_removed = 0
    items_added = 1

    while not frontier.isEmpty():
        current_node = frontier.pop()
        items_removed += 1
        state = current_node.state
        if problem.isGoalState(state):
            return (current_node.get_path(), current_node.path_cost, items_removed, items_added)
        if state not in explored:
            explored.add(state)
            for successor, action, step_cost in problem.getSuccessors(state):
                if successor not in explored:
                    new_node = Node(state=successor, parent=current_node, action=action, path_cost=current_node.path_cost + step_cost)
                    frontier.push(new_node)
                    items_added += 1
                    
    return ([], 0, items_removed, items_added)



def depthFirstSearch(problem):
    """
    Do not change this function

    Search the deepest nodes in the search tree first.
    """
    return depthFirstSearchStats(problem)[0] # return the list of actions only


def breadthFirstSearchStats(problem):
    """ Perform Breadth-First Search and return the path and stats. """

    frontier = util.Queue()
    start_state = problem.getStartState()
    start_node = Node(state=start_state)
    frontier.push(start_node)
    explored = set()
    items_removed = 0
    items_added = 1

    while not frontier.isEmpty():
        current_node = frontier.pop()
        items_removed += 1
        state = current_node.state
        if problem.isGoalState(state):
            return (current_node.get_path(), current_node.path_cost, items_removed, items_added)
        if state not in explored:
            explored.add(state)
            for successor, action, step_cost in problem.getSuccessors(state):
                if successor not in explored:
                    new_node = Node(state=successor, parent=current_node, action=action, path_cost=current_node.path_cost + step_cost)
                    frontier.push(new_node)
                    items_added += 1
    
    return ([], 0, items_removed, items_added)



def breadthFirstSearch(problem):
    """ Do not change this function"""
    return breadthFirstSearchStats(problem)[0] # return the list of actions only


def uniformCostSearchStats(problem):
    
    frontier = util.PriorityQueue()
    
    start_state = problem.getStartState()
    
    start_node = Node(state=start_state)
    frontier.push(start_node, 0)
    
    explored = set()
    
    items_removed = 0
    items_added = 1

    while not frontier.isEmpty():
        current_node = frontier.pop()
        items_removed += 1
        
        state = current_node.state
        
        if problem.isGoalState(state):
            return (current_node.get_path(), current_node.path_cost, items_removed, items_added)

        if state not in explored:
            explored.add(state)
            
            for successor, action, step_cost in problem.getSuccessors(state):
                if successor not in explored:
                    new_node = Node(state=successor, parent=current_node, action=action, path_cost=current_node.path_cost + step_cost)
                    
                    frontier.push(new_node, new_node.path_cost)
                    items_added += 1
    
    return ([], 0, items_removed, items_added)

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    return uniformCostSearchStats(problem)[0]


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearchStats(problem, heuristic=nullHeuristic):
    
    frontier = util.PriorityQueue()
    
    start_state = problem.getStartState()
    
    start_node = Node(state=start_state)
    frontier.push(start_node, start_node.path_cost + heuristic(start_state, problem))
    
    explored = set()
    
    items_removed = 0
    items_added = 1

    while not frontier.isEmpty():
        current_node = frontier.pop()
        items_removed += 1
        
        state = current_node.state
        
        if problem.isGoalState(state):
            return (current_node.get_path(), current_node.path_cost, items_removed, items_added)

        if state not in explored:
            explored.add(state)
            
            for successor, action, step_cost in problem.getSuccessors(state):
                if successor not in explored:
                    new_node = Node(state=successor, parent=current_node, action=action, path_cost=current_node.path_cost + step_cost)
                    
                    f_cost = new_node.path_cost + heuristic(successor, problem)
                    
                    frontier.push(new_node, f_cost)
                    items_added += 1
    
    return ([], 0, items_removed, items_added)

def aStarSearch(problem, heuristic=nullHeuristic):
    """ Do not change this function"""
    return aStarSearchStats(problem, heuristic)[0]

def GreedySearch(problem, heuristic=nullHeuristic):
    
    frontier = util.PriorityQueue()
    
    start_state = problem.getStartState()
    
    start_node = Node(state=start_state)
    frontier.push(start_node, heuristic(start_state, problem))
    
    explored = set()
    
    while not frontier.isEmpty():
        current_node = frontier.pop()
        
        state = current_node.state
        
        if problem.isGoalState(state):
            return current_node.get_path()
        
        if state not in explored:
            explored.add(state)
            
            for successor, action, step_cost in problem.getSuccessors(state):
                if successor not in explored:
                    new_node = Node(state=successor, parent=current_node, action=action)
                    
                    frontier.push(new_node, heuristic(successor, problem))
    
    return []

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
greedy = GreedySearch
