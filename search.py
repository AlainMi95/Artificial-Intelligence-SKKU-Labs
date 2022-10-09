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

    def expand(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (child,
        action, stepCost), where 'child' is a child to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that child.
        """
        util.raiseNotDefined()

    def getActions(self, state):
        """
          state: Search state

        For a given state, this should return a list of possible actions.
        """
        util.raiseNotDefined()

    def getActionCost(self, state, action, next_state):
        """
          state: Search state
          action: action taken at state.
          next_state: next Search state after taking action.

        For a given state, this should return the cost of the (s, a, s') transition.
        """
        util.raiseNotDefined()

    def getNextState(self, state, action):
        """
          state: Search state
          action: action taken at state

        For a given state, this should return the next state after taking action from state.
        """
        util.raiseNotDefined()

    def getCostOfActionSequence(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    
    
    
    """
    Author: Alain Michienzi 
    
    Description: 
        The idea is to push a state, the moves and the cost to this specific state on a stack.
        First we check if the start state is our goal, and if yes we return an empty actionList.
        If its not the goal, get with the expand function child, action, stepCost
        with this information we can calculate the actions to the next node (action to node + action to next node = total actions).
        So we know the actions to every state.
        Then we push the node to the stack.
        We do this until the stack is empty and we visited every node.
        
        For it to be a DFS and work we need to use a Stack, otherwise it does not work     
    """
    
    actionList = []                         #this list holds all the actions taken to the goal
    visitedNodeList = []                    #This list holds all the visited nodes
    
    startState = problem.getStartState()    #start state from problem (maze) e.g. (34, 15)
    startNode = (startState, [], 0)         #startNode(state, actionList) is the first node where pacman starts
    
    nodeStack = util.Stack()                #The nodeStack holds nodes(state, actionList) to move to
    nodeStack.push(startNode)               #push the first node to the stack
    
    while(not nodeStack.isEmpty()):         #loop thru all nodes in stack until its empty
        node, actionList, cost = nodeStack.pop()  #pop top node on stack, and get the state and actionList
  
        if(problem.isGoalState(node)):      #check if the current node is on the goal, and 
            return actionList               #if its true then return its actionList
    
        if(node not in visitedNodeList):    #check if the node is not in the visitedNodeList
            visitedNodeList.append(node)    #if not then add node to visitedNodeList
            
            neighbours = problem.expand(node)    #get next neighbours e.g. [((34, 15), 'South', 1), ((33, 16), 'West', 1)]
            
            for child, action, stepCost in neighbours:      #loop neighbours to get child, action, stepCost from node
                if(child not in visitedNodeList):           #check if the node is not in the visitedNodeList
                    move = actionList+[action]              #calculate the move with action and actionList
                    costForNextNode = cost + stepCost       #Calculate the cost for the next node with the previous cost and the cost to this node
                    nextNode = child, move, costForNextNode #next node is the child of the current node with the move
                    nodeStack.push(nextNode)                #push next node to the queue
    
    return actionList

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    
    
    
    """
    Author: Alain Michienzi 
    
    Description: 
        The idea is to push a state, the moves and the cost to this specific state on a queue.
        First we check if the start state is our goal, and if yes we return an empty actionList.
        If its not the goal, get with the expand function child, action, stepCost
        with this information we can calculate the actions to the next node (action to node + action to next node = total actions).
        So we know the actions and cost to every state.
        Then we push the node to the queue.
        We do this until the queue is empty and we visited every node.
        
        For it to be a BFS and work we need to use a Queue, otherwise it does not work
    """
    
    actionList = []                         #this list holds all the actions taken to the goal
    visitedNodeList = []                    #This list holds all the visited nodes
    
    startState = problem.getStartState()    #start state from problem (maze) e.g. (34, 15)
    startNode = (startState, [], 0)         #startNode(state, actionList, cost) is the first node where pacman starts
    
    nodeQueue = util.Queue()                #The nodeQueue holds nodes(state, actionList) to move to
    nodeQueue.push(startNode)               #push the first node to the queue
    

    
    while(not nodeQueue.isEmpty()):         #loop thru all nodes in queue until its empty
        node, actionList, cost = nodeQueue.pop()  #pop front element of queue, and get the state, actionList and cost of node
  
        if(problem.isGoalState(node)):      #check if the current node is on the goal, and 
            return actionList               #if its true then return its actionList
    
        if(node not in visitedNodeList):    #check if the node is not in the visitedNodeList
            visitedNodeList.append(node)    #if not then add node to visitedNodeList
            
            neighbours = problem.expand(node)    #get next neighbours e.g. [((34, 15), 'South', 1), ((33, 16), 'West', 1)]

            for child, action, stepCost in neighbours:      #loop neighbours to get child, action, stepCost from node
                if(child not in visitedNodeList):           #check if the node is not in the visitedNodeList
                    move = actionList+[action]              #calculate the move with action and actionList
                    costForNextNode = cost + stepCost       #Calculate the cost for the next node with the previous cost and the cost to this node
                    nextNode = child, move, costForNextNode #next node is the child of the current node with the move
                    nodeQueue.push(nextNode)                #push next node to the queue
    
    return actionList
    

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    
    
    """
    Author: Alain Michienzi 
    
    Description: 
        !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        This Function fails with autograder, but works when its startet with pacman.
        
        The Problem is, that my solution only searchs for one path, and doesnt check if there is a better one.
        So my priority heuristic doesnt work as intended.
        
        So to fix the function i need to analyse my backtracking and search for the fastest rout.
        
        !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        
        The idea is to push a state, the moves, the cost and the priority to this specific state on a PriorityQueue.
        First we check if the start state is our goal, and if yes we return an empty actionList.
        If its not the goal, get with the expand function child, action, stepCost
        with this information we can calculate the actions to the next node (action to node + action to next node = total actions).
        So we know the actions and cost to every state.
        Then we push the node to the PriorityQueue with the Heuristic.
        We do this until the PriorityQueue is empty and we visited every node.
        
        For it to be a A* Search and work we need to use a PriorityQueue, otherwise it does not work
    """
    
    actionList = []                         #this list holds all the actions taken to the goal
    visitedNodeList = []                    #This list holds all the visited nodes
   # allPossibleRouts = []      Not in use, but for (rout,cost) to determin the best rout
    
    startState = problem.getStartState()    #start state from problem (maze) e.g. (34, 15)
    startNode = (startState, [], 0)         #startNode(state, actionList, cost) is the first node where pacman starts
    
    nodePriorityQueue = util.PriorityQueue()#The nodeQueue holds nodes(state, actionList) to move to
    nodePriorityQueue.push(startNode, 0)    #push the first node to the PriorityQueue with prio 0
    

    
    while(not nodePriorityQueue.isEmpty()): #loop thru all nodes in PriorityQueue until its empty
        node, actionList, cost = nodePriorityQueue.pop()  #pop PriorityQueue, and get the state, actionList and cost of node
  
        if(problem.isGoalState(node)):      #check if the current node is on the goal, and 
            return actionList               #if its true then return its actionList
    
        if(node not in visitedNodeList):    #check if the node is not in the visitedNodeList
            visitedNodeList.append(node)    #if not then add node to visitedNodeList
            
            neighbours = problem.expand(node)    #get next neighbours e.g. [((34, 15), 'South', 1), ((33, 16), 'West', 1)]

            for child, action, stepCost in neighbours:      #loop neighbours to get child, action, stepCost from node
                if(child not in visitedNodeList):           #check if the node is not in the visitedNodeList
                    move = actionList+[action]              #calculate the move with action and actionList
                    costForNextNode = cost + stepCost       #Calculate the cost for the next node with the previous cost and the cost to this node
                    nextNode = child, move, costForNextNode #next node is the child of the current node with the move
                    nodePriorityQueue.push(nextNode, heuristic)   #push next node to the PriorityQueue with the heuristic as priority
                    
                    """
                    My Idea: 
                        add to allPossibleRouts and chack afterwards if it is the fastest rout,
                        by comparing it to other routs.
                    """
         
    return actionList

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
