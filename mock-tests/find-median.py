import math

def medianRange (arr):
    arr.sort()
    
    n = len(arr) / 2
    n = math.floor(n)
    
    print(arr[n])

if __name__ == "__main__":
    arr = [1, 5, 7, 9, 10, 3, 4, 8]
    medianRange(arr)