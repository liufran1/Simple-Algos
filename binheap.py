"""Implementation of BinHeap thanks to http://interactivepython.org/courselib/static/pythonds/Trees/BinaryHeapImplementation.html"""
"""Comments added to explain functions"""
"""accepts tuples as elements, python does dictionary comparison for tuples"""


class BinHeap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    """Function to restore heap property when an item is added. This heap is a minheap, so the root is the smallest object. For maxheap flip all signs"""
    def percUp(self,i):
        while i // 2 > 0:
          """Compare parent and child. If heap property violated, swap"""
          if self.heapList[i] < self.heapList[i // 2]:
             tmp = self.heapList[i // 2]
             self.heapList[i // 2] = self.heapList[i]
             self.heapList[i] = tmp
          i = i // 2
    
    """Insert new item by first appending to end of array then percolating into place"""
    def insert(self,k):
      self.heapList.append(k)
      self.currentSize = self.currentSize + 1
      self.percUp(self.currentSize)

    """Find minimum child of item i"""
    def minChild(self,i):
      """If i is at the middle index, then it only has one child so return it"""
      if i * 2 + 1 > self.currentSize:
          """handles index out of bounds"""
          if(i * 2 <= self.currentSize):
              return i * 2
          else:
              return i
      else:
          """Else check both children and return the smaller one"""
          if self.heapList[i*2] < self.heapList[i*2+1]:
              return i * 2
          else:
              return i * 2 + 1

    """Restore heap property for when an item is deleted"""
    def percDown(self,i):
      while (i * 2) <= self.currentSize:
          """Look successively at index of min child"""
          mc = self.minChild(i)
          
          """Check that heap property is satisfied. If not, swap"""
          if self.heapList[i] > self.heapList[mc]:
              tmp = self.heapList[i]
              self.heapList[i] = self.heapList[mc]
              self.heapList[mc] = tmp
          """Move on to next child"""
          i = mc

    """Delete min val from minheap"""
    def delMin(self):
      """Store current minvalue"""
      retval = self.heapList[1]
      
      """Set min value to max value because this is about to pop the max. Effectively swapping min and max so that you can 'pop' the min"""
      self.heapList[1] = self.heapList[self.currentSize]

      """Set heap to new size"""
      self.currentSize = self.currentSize - 1
      
      """Remove the 'min' value"""
      self.heapList.pop()
      
      """Max value is at the top now. Bubble it down into position"""
      self.percDown(1)
      return retval

    def buildHeap(self,alist):
      """Start halfway up the list. Don't have to start at the end because percDown looks forward at the children above the median index"""
      i = len(alist) // 2
      
      """Initialize size of heap"""
      self.currentSize = len(alist)
      
      """Add 0 to beginning of array in order for the array index math to work correctly (it has to be 1 indexed)"""
      self.heapList = [0] + alist[:]
      while (i > 0):
          self.percDown(i)
          i = i - 1
