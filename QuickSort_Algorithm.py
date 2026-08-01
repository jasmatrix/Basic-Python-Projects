def quick_sort(nums):
    if len(nums) == 0:
        return nums
    else:
        pivot_value = nums[0]
        # less than pivot value
        ltpv = []
        # more than pivot value
        mtpv = []
        # equal to pivot value
        etpv = []
        sorted_list = []
        for i in range(0, len(nums)):
            if nums[i] == pivot_value:
                etpv.append(nums[i])

            if nums[i] > pivot_value:
                mtpv.append(nums[i])

            if nums[i] < pivot_value:
                ltpv.append(nums[i])

        return quick_sort(ltpv) + etpv + quick_sort(mtpv)


print(quick_sort([20, 3, 14, 1, 5, 6, 8]))