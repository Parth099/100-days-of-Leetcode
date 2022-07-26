class UnionFind:
    def __init__(self, lengthOfGraph) -> None:
        self.amtNodes = lengthOfGraph
        self.nodesList = [i for i in range(lengthOfGraph)]

    def find(self, node):
        proposedRoot = node

        #travel up the 'tree' if possible
        while proposedRoot != self.nodesList[proposedRoot]:
            proposedRoot = self.nodesList[proposedRoot]

        return proposedRoot

    def union(self, node1, node2):
        #the 'root' of 2 is node 1
        self.nodesList[node2] = node1


    def connected(self, n1, n2):
        return self.find(n1) == self.find(n2)


#optimized v1
#faster find, slower union
class QuickFind:
    def __init__(self, lengthOfGraph) -> None:
        self.amtNodes = lengthOfGraph
        self.nodesList = [i for i in range(lengthOfGraph)]

    def find(self, node):
        #array entry represents the "root" of the graph's connected component
        return self.nodesList[node]


    def union(self, node1, node2):
        N1 = self.find(node1)
        N2 = self.find(node2)

        #if they are the same node or are already connected
        if N1 == N2: return
        for i in range(self.amtNodes):
            if self.nodesList[i] == N2:
                #replace all of those connected to a node to the new node
                self.nodesList[i] = N1

    def connected(self, node1, node2):
        return self.find(node1) == self.find(node2)

#with this approach each array element holds the root of it self in the index
class QuickUnion:#UnionFindv3
    def __init__(self, lengthOfGraph) -> None:
        self.amtNodes = lengthOfGraph
        #this array just represents the parent and not the literal root
        self.nodesList = [i for i in range(lengthOfGraph)]

    def find(self, node):
            proposedRoot = node

            #travel up the 'tree' if possible
            while proposedRoot != self.nodesList[proposedRoot]:
                proposedRoot = self.nodesList[proposedRoot]

            return proposedRoot


    def union(self, node1, node2):
        N1 = self.find(node1)
        N2 = self.find(node2)

        #if they are the same node or are already connected
        if N1 == N2: return
        self.nodesList[N2] = N1

    def connected(self, node1, node2):
        return self.find(node1) == self.find(node2)

