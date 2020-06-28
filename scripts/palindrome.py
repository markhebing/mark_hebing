palindrome = input("Enter a word: ")
int_defined = len(palindrome)
x = 0
y = int_defined - 1
while palindrome[x] == palindrome[y]:
    x = x + 1
    y = y - 1
    if x == y or (y == x + 1 and palindrome[x] == palindrome[y]):
        print("This is a palindrome.")
        break
if palindrome[x] != palindrome[y]:
    print("This is not a palindrome.")
