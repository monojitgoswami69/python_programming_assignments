"""
13. RAINWATER HARVESTING
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining
"""

def calcWater(arr):
    n = len(arr)
    lmax = rmax = 0
    l = 0
    r = n - 1
    water = 0
    while l < r:
        lmax = max(lmax, arr[l])
        rmax = max(rmax, arr[r])
        if lmax <= rmax:
            water += lmax - arr[l]
            l += 1
        else:
            water += rmax - arr[r]
            r -= 1
    return water

array = list(map(int, input("Enter the elevation map: ").split()))
print("Elevation map:", array)
print("Water trapped:", calcWater(array))