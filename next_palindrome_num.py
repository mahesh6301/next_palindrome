s_num = input("Enter a Palindrome Number ")

num = s_num[::-1]
if s_num==num:
    temp = int(s_num)
    while True:
        temp = temp+1
        if str(temp) == str(temp)[::-1]:
            print("{} is the next palindrome number.".format(temp))
            break
else:
    print("{} is not a palindrome number.".format(s_num))
    
        
