class DynamicArray:
    
    def __init__(self, capacity: int):
        self.arr = [0] * capacity
        self.size = 0
        self.capacity = capacity


    def get(self, i: int) -> int:
        # Return the element at index i. 
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        # set(int i, int n) will set the element at index i to n. Assume that index i is valid.
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        #  push the element n to the end of the array.
        if self.size == self.capacity:
            self.resize(); # Double the array
        self.arr[self.size] = n
        self.size += 1
        

    def popback(self) -> int:
        # will pop and return the element at the end of the array.
        val = self.arr[self.size - 1]
        self.size -= 1
        return val

    def resize(self) -> None:
            # 1. 容量翻倍
            self.capacity *= 2
            # 2. 创建一个物理长度翻倍的新列表
            new_arr = [0] * self.capacity
            # 3. 将原有的数据拷贝到新列表中
            for i in range(self.size):
                new_arr[i] = self.arr[i]
            # 4. 将 self.arr 指向这个新列表
            self.arr = new_arr

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity
