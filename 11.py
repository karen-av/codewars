"""
Given an array (arr) as an argument complete the function countSmileys that should return the total number of smiling faces.

Rules for a smiling face:
Each smiley face must contain a valid pair of eyes. Eyes can be marked as : or ;
A smiley face can have a nose but it does not have to. Valid characters for a nose are - or ~
Every smiling face must have a smiling mouth that should be marked with either ) or D
No additional characters are allowed except for those mentioned.

Valid smiley face examples: :) :D ;-D :~)
Invalid smiley faces:  ;( :> :} :]

Example
countSmileys([':)', ';(', ';}', ':-D']);       // should return 2;
countSmileys([';D', ':-(', ':-)', ';~)']);     // should return 3;
countSmileys([';]', ':[', ';*', ':$', ';-D']); // should return 1;

Note
In case of an empty array return 0. You will not be tested with invalid input (input will always be an array). 
Order of the face (eyes, nose, mouth) elements will always be the same.
"""

def count_smileys(arr):
    counter = 0
    for c in arr:
        if len(c) == 2 and (c[0] == ':' or c[0] == ";") and (c[1] == ')' or c[1] == 'D'):
            counter += 1
            print(c)
        elif len(c) == 3 and (c[0] == ':' or c[0] == ";") and (c[1] == '-' or c[1] == '~') and (c[2] == 'D' or c[2] == ')'):
            counter += 1
            print(c)
    return counter #the number of valid smiley faces in array/list


x = [':D',':~)',';~D',':)']
print(count_smileys(x))