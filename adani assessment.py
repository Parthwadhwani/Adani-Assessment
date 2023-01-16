import numpy as np
def sortRowWise(arr):
	# loop for rows of matrix
	for i in range(len(arr)):
		# loop for column of matrix
		for j in range(len(arr[i])):
			# loop for comparison and swapping
			for k in range(len(arr[i]) - j - 1):
				if (arr[i][k] > arr[i][k + 1]):
					# swapping of elements
					t = arr[i][k]
					arr[i][k] = arr[i][k + 1]
					arr[i][k + 1] = t
					
	# printing the sorted matrix
	for i in range(len(arr)):
		for j in range(len(arr[i])):
			print(arr[i][j], end=" ")
		print()

# Driver code
arr = np.random.randint(100 ,size=(5,5))
print(arr)
sortRowWise(arr)
