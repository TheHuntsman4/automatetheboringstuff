import re

file=open('madlibs.txt')
text = file.read()
file.close()

regex = re.compile(r'ADJECTIVE|NOUN|VERB|ADVERB')
matches = regex.findall(text)

for word in matches:
    user_input = input('Enter %s: ' % word)
  
    text = text.replace(word,user_input,1)
print(text)
