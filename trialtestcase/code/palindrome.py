class palindrome:

    def palindrome1(string):
        
        n=len(string)
        flag = 0
        
        for i in range(0,n//2,1):
            if (string[i]!=string[n-1-i]):
                flag=1
                break
        if (flag==1):
            print("string is not palindrome")
        else:
            print("palindrome")
        return flag
        
        