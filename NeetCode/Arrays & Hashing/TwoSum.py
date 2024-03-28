def two_sum(nums, target):
    num_indices = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_indices:
            return [num_indices[complement], i]
        num_indices[num] = i


nums1 = [2, 7, 11, 15]
target1 = 9
print(two_sum(nums1, target1))

nums2 = [3, 2, 4]
target2 = 6
print(two_sum(nums2, target2))

nums3 = [3, 3]
target3 = 6
print(two_sum(nums3, target3))
