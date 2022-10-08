#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def countingSort(arr):
    # Write your code here
    size = max(arr) + 1
    count = [0] * (size)

    # print(count)

    # Store the count of each element at 
    # their respective index in count array
    for i in range(0, len(arr)):
       count[arr[i]] += 1
    #    print(arr[i])

    return count

if __name__ == '__main__':
    
    arr = [1, 4, 5, 6, 7, 1, 9, 9, 8, 2, 4, 3]

    result = countingSort(arr)
    print(result)