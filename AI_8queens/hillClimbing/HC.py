from State import State
import copy
class HillClimbing:

    def __init__(self,problemState):
        self.problemState = State(problemState,None)

    def findNextNeighbor(self,current):
        neighbor =copy.deepcopy( current)

        for i in  range (0,len(current.state)):

            temp = copy.deepcopy(current.state)
            x = temp[i]

            for j in range (0,len(temp)):

                if not (x == j):
                    temp[i] = j
                    tempState = State(temp,current)
                    if tempState.value < neighbor.value :
                        neighbor = tempState

        return neighbor


    def climb(self):
        current = self.problemState

        while True :
            neighbor = self.findNextNeighbor(current)
            if(self.equal(neighbor,current)):
                self.printRoad(current)
                break;
            else:
                current = neighbor

    def printRoad(self,state):

        while True:
            self.printState(state)
            if state.parentState:
                state = state.parentState
            else:
                break

    def printState(self,state):
        print("state: "+str(state.state))
        print("value: "+str(state.value))
        print("   ",end="")
        for i in range(0, len(state.state)):
            print(" "+str(i)+" ", end="")

        print("")
        for i in range(0,len(state.state)):
            print(" "+str(i)+" ", end="")
            for j in range(0, len(state.state)):
                if state.state[j] == i :
                    print(" q ", end="")
                else :
                    print("   ", end="")
            print("")


    def equal(self,state1,state2):
        returnVal = True
        for i in range(0,len(state1.state)):
            if not (state1.state[i] == state2.state[i]) :
                returnVal = False
                break
        return returnVal