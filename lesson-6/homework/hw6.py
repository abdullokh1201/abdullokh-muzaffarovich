#2. return uncommon elements of lists. (order of elements does not matter)
#from collections import Counter

def get_uncommon_elements(list1, list2):
    count1 = Counter(list1)
    count2 = Counter(list2)

  
    uncommon_from_list1 = []
    for item in count1:
        if item not in count2:
            uncommon_from_list1.extend([item] * count1[item])
        else:
        
            if count1[item] > count2[item]:
                uncommon_from_list1.extend([item] * (count1[item] - count2[item]))

    
    uncommon_from_list2 = []
    for item in count2:
        if item not in count1:
            uncommon_from_list2.extend([item] * count2[item])
        else:
        
            if count2[item] > count1[item]:
                uncommon_from_list2.extend([item] * (count2[item] - count1[item]))

    return uncommon_from_list1 + uncommon_from_list2
print(get_uncommon_elements([1, 1, 2], [2, 3, 4])) 


print(get_uncommon_elements([1, 2, 3], [4, 5, 6])) 




print(get_uncommon_elements([1, 1, 2, 3, 4, 2], [1, 3, 4, 5])) 

#3. txt nomli string saqlovchi o'zgaruvchi berilgan.

#txt dagi har uchinchi belgidan keyin pastki chiziqcha (underscore) qo'yilsin. Agar belgi unli harf yoki orqasidan ostki chiziqcha qo'yilgan harf bo'lsa, ostki chiziqcha keyingi harfdan keyin qo'yilsin. Agar belgi satrdagi ohirgi belgi bo'lsa chiziqcha qo'yilmasin.

input: hello

output: hel_lo

input:

assalom

output:

ass_alom

input: abcabcdabcdeabcdefabcdefg

output: abc_abcd_abcdeab_cdef_abcdefg

def insert_underscore(txt):
    result = []
    count = 0
    i = 0

    while i < len(txt):
        result.append(txt[i])
        count += 1

        
        if count % 3 == 0 and i != len(txt) - 1:
            current_char = txt[i]
            next_char = txt[i + 1] if i + 1 < len(txt) else ''

            if current_char.lower() in 'aeiou' or next_char == '_':
            
                if i + 1 < len(txt) - 1:
                    i += 1
                    result.append(txt[i])
                    result.append('_')
            else:
                result.append('_')

        i += 1

    return ''.join(result)
print(insert_underscore("hello"))          


print(insert_underscore("assalom"))        


print(insert_underscore("abcabcdabcdeabcdefabcdefg"))



