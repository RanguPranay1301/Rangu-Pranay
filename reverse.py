'''
Write a program to find the reverse of thr given number.
'''
'''num=int(input("Enter a number :"))
rev=0
while num>0:
    rev=rev*10 + num%10
    num=num//10
print("The result is :",rev)'''
def reverse(num):
    rev=0
    while num>0:
        rev=rev*10+num%10
        num//=10
    return rev

def isPalindrome(num):
    return num ==reverse(num)
print(reverse(123))
print(isPalindrome(121))
