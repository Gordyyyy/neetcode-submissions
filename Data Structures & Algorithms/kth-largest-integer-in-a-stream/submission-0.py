class KthLargest:

    # This class finds the kth largest integer in a stream of values
    # including duplicates.

    def __init__(self, k: int, nums: List[int]):
        self.k = k # kth largest number should be returned
        self.nums = nums # nums is a list that contains all the integers


    def add(self, val: int) -> int:
        # Adds integer into the stream and returns the kth largest num
        self.nums.append(val)
        return sorted(self.nums)[-self.k]
            
