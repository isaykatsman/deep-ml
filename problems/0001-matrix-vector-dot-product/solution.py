def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	# If the number of columns in 'a' does not match the length of 'b', return -1.
	a_r = len(a)
	a_c = len(a[0])

	# the matrix-vector product doesn't type/size check
	if a_c != len(b):
		return -1

	# perform the product
	res = []

	for r in range(a_r):
		full_dot = sum([u*v for u,v in zip(a[r], b)])
		res.append(full_dot)
	return res
