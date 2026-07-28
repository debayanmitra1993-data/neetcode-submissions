class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1copy = nums1[:m]
        nums1idx, nums2idx = 0, 0
        idx = 0

        while nums1idx < m and nums2idx < n:
            if nums2[nums2idx] < nums1copy[nums1idx]:
                nums1[idx] = nums2[nums2idx]
                nums2idx += 1
            else:
                nums1[idx] = nums1copy[nums1idx]
                nums1idx += 1
            idx += 1
        
        while nums1idx < m:
            nums1[idx] = nums1copy[nums1idx]
            idx += 1
            nums1idx += 1
        
        while nums2idx < n:
            nums1[idx] = nums2[nums2idx]
            idx += 1
            nums2idx += 1
        

        

        
        