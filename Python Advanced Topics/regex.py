#!/usr/bin/env python3
import re
import os
from itertools import count

fname = '/Users/abhigaut/Desktop/regex_dataset.txt'
if os.path.exists(fname):
    with open(fname, 'rt') as f:
        data =  f.read()

# will match all phone numbers, any separator
phone_numbers = re.compile(r'\d{3}.\d{3}.\d{4}')

# will match emails with usernames existing of underscores, hyphens and dots
email = re.compile(r'[A-Za-z0-9.\_\-]+@[A-Za-z]+\.(com|org|gov|edu)')

# finds all matches and returns an iterator
phone_numbers_matches = phone_numbers.finditer(data)
email_matches = email.finditer(data)

# finds all and collects in a list
matches_no_iter = phone_numbers.findall(data)

# finds just one match across all data, and returns the first hit
just_one_match_across_all = phone_numbers.search(data)

# finds just the first element in the give data
just_the_first_element_in_the_beginning = phone_numbers.match(data)

sentence = 'Start a sentence with 100 and then bring it to an end to a 0 Ha HaHa'
more_phone_numbers = """
316-431-9774
316.431.9773
(316) 431-9772
800-117-9900
800-889-6879
900-889-3345
900.334.8576
"""

urls = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''

# matches first Ha after 0 and first half of HaHa as it space is a word boundary
pattern = re.compile(r'\bHa')

# will match Start at the beginning of the string. If ^ switched with $, won't match anything
pattern2 = re.compile(r'^Start')

# will match start as it ignores the case
pattern6 = re.compile(r'start', re.IGNORECASE)

# will match all phone numbers in more_phone_numbers
pattern3 = re.compile(r'\(?\d{3}\)?[-.\s]\d{3}[-.]\d{4}')

# will match all phone number starting with 800 or 900
pattern4 = re.compile(r'[89]00[-.]\d{3}[-.]\d{4}')

# will scrape domain names and TLDs in URLs using 'group' separation
pattern5 = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')

domain_and_tlds = pattern5.finditer(urls)
for match in domain_and_tlds:
    print (' '.join(match.group(2,3)))

# substituting using groups
subbed_urls = pattern5.sub(r'\2\3',  urls)

print (subbed_urls)
