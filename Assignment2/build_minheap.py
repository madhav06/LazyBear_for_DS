# python3

class HeapBuilder:
    # index = 0
    # global index

    def __init__(self, n):
        self.swaps = [None]*4*n # array of tuples or arrays
        self.data = []
        self.n = n
        self.index = 0

    def ReadData(self):
        # n = int(input())
        self._data = [int(s) for s in input().split()]
        assert self.n == len(self._data)

    def WriteResponse(self):
        print(self.index)
        for i in range(self.index):
            print(self._swaps[i][0],self._swaps[i][1])
        # print(len(self.swaps))
        # for swap in self._swaps:
        #     print(swap[0], swap[1])

    def swapup(self,i):
        if i != 0:
            # print(self._data[int((i-1)/2)], self._data[i])
            # print(self.index)
            if self._data[int((i-1)/2)] > self._data[i]:
                # print('2')
                self._swaps[self.index] = ((int((i-1)/2)),i)
                self.index += 1

                self._data[int((i-1)/2)], self._data[i] = self._data[i], self._data[int((i-1)/2)]
                self.swapup(int((i-1)/2))

    def GenerateSwaps(self):
    
    # The following naive implementation just sorts 
    # the given sequence using selection sort algorithm
    # and saves the resulting sequence of swaps.
    # This turns the given array into a heap, 
    # but in the worst case gives a quadratic number of swaps.
    #
    # TODO: replace by a more efficient implementation
    # efficient implementation is complete binary tree. but here you're not getting data 1 by 1, 
    # instead everything at once
    # so for i in range(0,n), implement swap up  ai < a2i+1  ai < a2i+2
        for i in range(len(self._data)-1,0,-1):
            self.swapup(i)

    def Solve(self):
        self.ReadData()
        self.GenerateSwaps()
        self.WriteResponse()

if __name__ == '__main__':
    n = int(input())
    heap_builder = HeapBuilder(n)
    heap_builder.Solve()


        

