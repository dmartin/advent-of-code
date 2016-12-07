import hashlib

input_str = "bgvyzdsv"
solution = 1
while True:
	test_string = input_str + str(solution)
	result = hashlib.md5()
	result.update(test_string.encode("utf-8"))
	if (result.hexdigest()[:6] == "000000"):
		print(result.hexdigest())
		print("Solution: " + str(solution))
		break
	else:
		solution = solution + 1
