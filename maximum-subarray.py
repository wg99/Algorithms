"""Implementation of divide and conquer solution to maximum-subarray 
problem"""

def find_maximum_subarray(lst):
    '''Searches a sequence and finds the subarray with the largest sum.
    Uses a divide and conquer approach.

    Runtime: O(N * log(N))
    
    Args:
        lst: A list of numeric values.
    
    Returns: 
        A tuple of three integers representing the starting index, the 
        ending index, and the sum of all of the values in the 
        found subarray. 
    '''

    def find_max_crossing_subarray(lst, low, mid, high):
        left_sum = float('-inf')
        curr_sum = 0
        max_left = None
        for i in range(mid, low, -1):
            curr_sum += lst[i]
            if curr_sum > left_sum:
                left_sum = curr_sum
                max_left = i
        right_sum = float('-inf')
        curr_sum = 0
        max_right = None
        for i in range(mid + 1, high + 1):
            curr_sum += lst[i]
            if curr_sum > right_sum:
                right_sum = curr_sum
                max_right = i
        return (max_left, max_right, left_sum + right_sum)
 
    def find_max_helper(lst, low, high):
        if low == high:
            return (low, high, lst[low])
        else:
            mid = (low + high) // 2
            l = find_max_helper(lst, low, mid)
            r = find_max_helper(lst, mid + 1, high)
            c = find_max_crossing_subarray(lst, low, mid, high)
            if l[2] >= r[2] and l[2] >= c[2]:
                return l
            elif r[2] >= c[2] and r[2] >= l[2]:
                return r
            else:
                return c

    return find_max_helper(lst, 0, len(lst) - 1)


def main():
    lst = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
    print(find_maximum_subarray(lst))    	    	


if __name__ == '__main__':
    main()
