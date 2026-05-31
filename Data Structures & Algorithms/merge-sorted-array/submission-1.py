class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        ## [10,20,20,40,0,0] [1, 35]
        ## [10, 20, 20, 40, 0, 0] last = 5 i = 3 j = 1
        ## [10, 20, 20, 0, 0, 40] last = 4 i = 2 j = 1
        ## [10, 20, 20, 0, 35, 40] last = 3 i = 2 j = 0
        ## [10, 20, 0, 20, 35, 40] last = 2 i = 1 j = 0
        ## [10, 0, 20, 20, 35, 40] last = 1 i = 0 j = 0
        ## [0, 10, 20, 20, 35, 40] last = 1 i = -1 j = 0
        i = m - 1
        j = n - 1
        last = m + n - 1

        while j >= 0:
            if(i >= 0 and nums1[i] > nums2[j]):
                nums1[last] = nums1[i]
                i -= 1
            else:
                nums1[last] = nums2[j]
                j -= 1
            last -= 1




            

        