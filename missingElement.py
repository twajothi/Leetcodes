"""
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.
"""
def solution(A):
	if A[-1] !=len(A):
		return len(A)
	elif A[0] !=0: 
		return 0 
	else: 
		for i in range(1, len(A)):
			if A[i]!=A[i-1] + 1:
				return A[i-1] + 1