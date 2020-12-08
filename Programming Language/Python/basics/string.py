# formatting
num = 27
print(f"my age: {num}")

# upper,lower, capitalize
name = "Night Crawler"
print(name.lower(), name.upper())
print(name.isupper())

# replace
print(name.replace("Crawler", "Walker"))

# string slicing [start:end:step]
print(name[:3]) 
print(name[2:])
print(name[::-1])

# Palindrome
query = input("Enter anything: ")
print("Palindrome!") if query == query[::-1] else print("Not palindrome")

