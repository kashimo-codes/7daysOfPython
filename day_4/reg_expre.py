# Regular expressions:
#  a powerful tool for working with text data
#  Enable you to search for and match specific
#  character patterns withing a string.
#  module used is re

import re

#  Search for a phone number in a string
text = 'My phone number is 555-7777'
match = re.search(r'\d{3}-\d{4}', text)

if match:
    print(match.group(0))

#  Extract email address from a string
text = 'My email is  example@7daypython.com, but I also use other@cloud.io'
matches = re.findall(r'\S+@\S+', text)
print(matches)