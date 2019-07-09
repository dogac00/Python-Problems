person = {'name': 'John', 'age': 24}

sentence = "My name is " + person['name'] + " and I am " + str(person['age']) + " years old."
print(sentence)

# not very readable, you have to open and close, and put spaces in the correct locations

sentence_format = "My name is {} and I am {} years old".format(person['name'],person['age'])
print(sentence_format)

# first value to first placeholder, and second to second above

sentence_format_placeholders = "My name is {0} and I am {1} years old.".format(person['name'],person['age'])
print(sentence_format_placeholders)

# still works, more useful for the placeholders for values that needs to be repeated

tag = 'h1'
text = 'This is a headline'

sentence_tag = "<{0}>{1}<{0}>".format(tag, text)

# output is <h1>This is a headline</h1>

sentence_pass_in = "My name is {0[name]} and I am {0[age]} years old.".format(person)
