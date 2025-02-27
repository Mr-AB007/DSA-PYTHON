
    """
    Do not return anything, modify nums1 in-place instead.
    """
def merge(nums1, m, nums2, n):
    # Pointers for nums1, nums2, and the last position in merged array
    p1, p2, p = m - 1, n - 1, m + n - 1

    # Merge from the back to avoid overwriting elements in nums1
    while p1 >= 0 and p2 >= 0:
        if nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1
        p -= 1

    # If any elements remain in nums2, copy them (remaining nums1 elements are already in place)
    while p2 >= 0:
        nums1[p] = nums2[p2]
        p2 -= 1
        p -= 1

nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3

merge(nums1, m, nums2, n)
print(nums1)  # Output: [1, 2, 2, 3, 5, 6]
