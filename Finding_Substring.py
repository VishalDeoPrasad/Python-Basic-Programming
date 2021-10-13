string = input("Enter a String : ")
substring = []
for i in range(len(string)):
	for j in range(i + 1, len(string) + 1 ):
		substring.append(string[i:j])
print("Total Number of Substring are : ",len(substring))
print("All Substrings")
print(substring)
