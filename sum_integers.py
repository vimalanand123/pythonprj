print("this is sum string numbers")

def sum_of_string(str1,str2):
    sum     =   0
    carry   =   0
    ans =""
    len_of_str1 = len(str1)
    len_of_str2 = len(str2)
    if(len_of_str1<len_of_str2):
        str1,str2 = str2,str1

    len_of_str1 = len(str1)
    len_of_str2 = len(str2)
    for i in range(1,len_of_str2+1):
        #print(str1[-i:-(i+1):-1])
        sum = (ord(str1[-i:-(i+1):-i])-ord('0')+ord(str2[-i:-(i+1):-i])-ord('0')+carry)%10
        carry = (ord(str1[-i:-(i+1):-i])-ord('0')+ord(str2[-i:-(i+1):-i])-ord('0')+carry)//10
        ans = str(sum)+ans
        print(ans,carry,sum)
    for i in range(len_of_str2+1,len_of_str1+1):
        sum = (ord(str1[-i:-(i + 1):-i]) - ord('0') + carry) % 10
        carry = (ord(str1[-i:-(i + 1):-i]) - ord('0') + carry) // 10
        ans = str(sum)+ans
        print(ans,carry,sum)
    if(carry):
        ans = str(carry) + ans
    print(ans, carry, sum)
    return ans

#sum_of_string("1","99")
#sum_of_string("99","1")
#sum_of_string("99","11")

def split_string(str,beg,len1,len2):
    str1 = str[beg:beg+len1]
    str2 = str[beg + len1:beg+len1+len2]
    str3 = sum_of_string(str1,str2)
    #check whether length of sum string exceeds actuall digits in string3
    if(len(str3)>(len(str)-beg-len1-len2)):
        print("size limit")
        return 0
    if(str3 == str[beg+len1+len2:beg+len1+len2+len(str3)]):
        if(len(str3)==(len(str)-beg-len1-len2)):
            return 1

        split_string(str,beg+len1,len2,len(str3))
    else:
        print("not a sum",str3,str[beg+len1+len2:beg+len1+len2+len(str3)])
        return 0
def isSumString(str,beg,len1,len2):
    for i in range(1,len1):
        for j in range(1,)
is_sum_string = split_string("1199110",0,2,2)
print(is_sum_string)
is_sum_string = split_string("1199110199",0,2,2)
print(is_sum_string)