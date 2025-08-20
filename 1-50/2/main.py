
def brute_force(max_num=4_000_000):
	sum = 0
	a,b = 0,1
	while a <= max_num:
		if b % 2 == 0:
			sum += b
		a, b = b, a + b
	return sum

def elegant(max_nums=4_000_000):
	sum = 0
	a,b = 2,8
	while a <= max_nums:
		sum += a
		a,b = b, 4*b + a
	return sum

if __name__ == "__main__":
	a = brute_force()
	b = elegant()
	
	assert a == b, "Solutions are not equal"
	print(f"Solution: {b}")

	
