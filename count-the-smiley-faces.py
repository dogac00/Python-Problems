# Given an array (arr) as an argument complete the function countSmileys that should return the total number of smiling faces.

# Rules for a smiling face:
# -Each smiley face must contain a valid pair of eyes. Eyes can be marked as : or ;
# -A smiley face can have a nose but it does not have to. Valid characters for a nose are - or ~
# -Every smiling face must have a smiling mouth that should be marked with either ) or D.
# No additional characters are allowed except for those mentioned.
# Valid smiley face examples:
# :) :D ;-D :~)
# Invalid smiley faces:
# ;( :> :} :] 

# Example cases:

# countSmileys([':)', ';(', ';}', ':-D']);       // should return 2;
# countSmileys([';D', ':-(', ':-)', ';~)']);     // should return 3;
# countSmileys([';]', ':[', ';*', ':$', ';-D']); // should return 1;

# Note: In case of an empty array return 0. You will not be tested with invalid input (input will always be an array). 
# Order of the face (eyes, nose, mouth) elements will always be the same

def count_smileys(arr):
    count = 0
    eye = [":",";"]
    nose = ["-","~"]
    mouth = [")", "D"]
    smileys = []
    for i in eye:
        for j in mouth:
            smileys.append(i+j)
            for k in nose:
                smileys.append(i+k+j)
    for i in arr:
        if i in smileys:
            count += 1
    return count
    
# Or with regular expressions

from re import findall
def count_smileys(arr):
    return len(list(findall(r"[:;][-~]?[)D]", " ".join(arr))))
