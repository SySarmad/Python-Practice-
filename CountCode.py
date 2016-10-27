"""
Created by Sarmad Syed 10/5/2016
CountCode: program to count the occurences
of the word code in a given string
"""

"""
@count_code: takes in a string as aparameter and checks it for
occurences of the word code returns and integer count
"""

def count_code(str):
    count = 0                       # @count: int variable to hold count
    for i in range(0, len(str)-1):  # iterate through string checking values
        if str[i] == 'c' and str[i+1] =='o' and str[i+3] == 'e' and i+1 != len(str):
            count +=1                 #increment count
    return count

"""
@cound_code_re: takes in string and uses
regex to count all occurences of the word
code in a string
"""


def count_code_re(str):
    pattern = 'coe'     # @pattern: a regex pattern of 'coe' d can be omitted as per the req.
    return len(re.findall(pattern, string_to_search)) #returns with regex the len of the array with all occurences of pattern

#Test statements for count_code
print count_code('aaacodebbb')
print count_code('codexxcode')
print count_code('cozexxcope')
print count_code('coyehhhshsftkcodeksksksksdjkfgcorejasdasdadasjklasdcoce')

