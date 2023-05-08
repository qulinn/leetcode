def removeElement(nums, val):
    i = 0
    n = len(nums)
    while i < n:
        if nums[i] == val:
            print(nums[i],"==", val)
            nums[i] = nums[i-1]
            print(nums[i],"=", nums[i-1])
            n -= 1
            print("n=", n)
        else:
            print(nums[i], "!=", val)
            i += 1
    print(nums)
    print(n)
    return n

if __name__ == "__main__":
    nums = [3,2,2,3]
    val = 3
    removeElement(nums, val)
