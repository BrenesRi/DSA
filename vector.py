#import 

#Normally, Integers will take 4 bytes (or 32 bits) and ASCII chars will only take 1 byte (4 bits).
#A list is usually allocated all together one after the other in order.

#Exercise #1: Remove Duplicates from Sorted Array
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        l = 1
        for r in range(1, len(nums)):
            if nums[r] != nums[r - 1]:
                nums[l] = nums[r]
                l = l+1
        return l
#Exercise #2: Remove an element in a sorted Array
class Solution2:
    def removeElement(self, nums: list[int], val: int) -> int:
        l = 0
        for i in range(0,len(nums)):
            if nums[i] != val:
                nums[l] = nums[i] 
                l += 1
        return l
    
#Common exercises and problems
list = [1, 2, 3, 4, 5]

#The two pointer way of solving problems can be used in a lot of ways
def invert_list(list):
    l = 0 
    e = len(list) - 1
    while l < e:
        list[l] = list[e] 
        list[e] = list[l]
        l += 1
        e -= 1
    return list
#print(invert_list(list))

def move_zeroes(list):
    pos = 0 
    for i in range(len(list)):
        if list[i] != 0:
            list[pos], list[i] = list[i], list[pos] #Both elements of the list get changed at the same time, avoiding problems
            pos += 1
    return list
#print(move_zeroes(list))

def two_sum(list, num):
    response = []
    for e in list:
        for i in list:
            if e + i == num:
                response.append(e)
                response.append(i)
                return response
#print(two_sum(list,7))

def solution(list):
    cont = 0
    candidate = None
    for num in list:
        if cont == 0:
            candidate = num
        cont += (1 if num == candidate else -1)
    return candidate if list.count(candidate) > len(list) // 2 else None

#list = [2, 2, 1, 1, 1, 2, 2]
#print(solution(list))

def reorganize_negative_positive(list):
    i, j = 0, 0
    while j < len(list):
        if list[j] < 0:
            list[i], list[j] = list[j], list[i]
            i += 1
        j += 1
    return list
#lista = [-1, 2, -3, 4, 5, -6]
#print(reorganize_negative_positive(lista))


