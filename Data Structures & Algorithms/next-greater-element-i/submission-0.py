class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1out = [-1]*len(nums1)
        nums2out = [-1]*len(nums2)
        store = {}

        mystack = [(0, nums2[0])]
        for idx in range(1, len(nums2)):
            ele = nums2[idx]
            if len(mystack) == 0:
                mystack.append((idx, ele))
                continue 

            if ele <= mystack[-1][1]:
                mystack.append((idx, ele))
            else:
                while len(mystack) > 0:
                    if ele > mystack[-1][1]:
                        popped_idx, popped_ele = mystack.pop()
                        nums2out[popped_idx] = ele
                        store[nums2[popped_idx]] = ele
                    else:
                        break
                mystack.append((idx, ele))
        print("nums2out = ", nums2out)

        nums1out = [-1]*len(nums1)
        for idx in range(len(nums1)):
            ele = nums1[idx]
            nums1out[idx] = store.get(ele, -1)
        return nums1out
        