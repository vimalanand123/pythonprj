print("This is a Minimum sub-string sliding window ")

def MinimumSubString(input_str :str,sub_str :str):
    hash_str     = list(map(int, [0 for x in range(256)]))
    hash_sub_str = list(map(int ,[0 for x in range(256)]))

    print("hash_str is {} and hash_sub_str is {}".format(hash_str,hash_sub_str))

    str_len     = len(input_str)
    sub_str_len = len(sub_str)
    print(sub_str_len)

    if(str_len < sub_str_len):
        return ""

    for i in range(sub_str_len):
        hash_sub_str[ord(sub_str[i])] += 1
        print(sub_str[i])

    print("bhash_sub_str is {}".format(hash_sub_str))
    have , left , minimum_str_len ,min_sub_str = 0 ,0 , float('inf'),""

    for right in range(str_len):
        hash_str[ord(input_str[right])] += 1
        print("hash update is {} ; {}".format(hash_str[ord(input_str[right])],(input_str[right])))

        if(hash_str[ord(input_str[right])] <= hash_sub_str[ord(input_str[right])]):
            have += 1
            print("have {}".format(have))
            if(have == sub_str_len):
                print("have")
                while(have == sub_str_len):
                    if(minimum_str_len > right-left+1 ):
                        minimum_str_len = right - left +1
                        min_sub_str = input_str[left:right+1]
                        print("min_sub_str is {}".format(min_sub_str))

                    hash_str[ord(input_str[left])] -=1
                    if(hash_str[ord(input_str[left])] < hash_sub_str[ord(input_str[left])]):
                        have -= 1
                    left += 1
                    print("left is {}".format(left))


MinimumSubString("This is a test string","tist")
print("**********")
MinimumSubString("tsit","tist")


