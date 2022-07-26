class QuickUnionByRank:
    def __init__(self, lengthOfGraph) -> None:
        self.amtNodes = lengthOfGraph
        self.nodesList = [i for i in range(lengthOfGraph)]
        self.rank = [1] * self.amtNodes

    def find(self, n):

        #travel up the 'tree' if possible
        while n != self.nodesList[n]:
            n = self.nodesList[n]

        return n

    def union(self, node1, node2):
        #the 'root' of 2 is node 1
        root_n1, root_n2 = self.find(node1), self.find(node2)
        rank_n1, rank_n2 = self.rank[root_n1], self.rank[root_n2]

        #ignore if roots are already joined (in a union)
        if root_n1 == root_n2: return

        if rank_n1 > rank_n2:
            #r1 gets to be main root since it is larger
            self.nodesList[root_n2] = root_n1
        elif rank_n2 > rank_n1:
            self.nodesList[root_n1] = root_n2
        else:
            self.nodesList[root_n2] = root_n1
            #for the next time this comparison is made
            self.rank[root_n1] += 1


    def connected(self, n1, n2):
        return self.find(n1) == self.find(n2)
