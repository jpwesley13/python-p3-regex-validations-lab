import re

# NOTE: There are only a few tests included, so multiple solutions will work.
# Feel free to encourage students to find oversights and add tests to this lab!

name = r"[A-Z][']*([A-z][ \-']{0,1})+"
name_regex = re.compile(name)
# [A-Z]--Name starts with a capital letter.
# [']*--After first letter of name there may or may not be an apostrophe (O'neal). The ['] is oviously the apostrophe, but the * is saying "0 or more instances of the preceding element."
# [ \-']{0,1}--There can be 0-1 instances of a space, hyphen, or apostrophe after the first parts.
# ([A-z])+--Matches one or more letters after the optional '.
# ([A-z][ \-']{0,1})+--Matches one or more of a letter followed by 0-1 instances of a space, hyphen, or apostrophe (Dakota Kasanari, Jane-Doe, Jim O'Hare)

phone_number = r"\({0,1}[\d]{3}\){0,1}[- ]{0,1}[\d]{3}[-]*[\d]{4}"
phone_regex = re.compile(phone_number)
# Using \({0,1} uses backslash to stop ( from activating as a () statement. Then says 0 to 1 of these may happen. May be better to do something like -{0,1} than [-]* for explicit purposes?
# [- ] means there can be a hyphen OR a space there.

email_address = r"[A-z]([A-z0-9][\.]{0,1})+[A-z0-9]+@[A-z0-9]+\.[a-z]{2,}"
email_regex = re.compile(email_address)
# Starts with a letter, but the middle can be any alphanumeric or 0-1 period.
# It must not end in a period though so the final character must be alphanumeric.
# +@ for a domain, then back to alphanumerics for the domain.
# Ends at a \. (to stop . special properties like fish.catch()) and at least two lowercase letters for the domain ender (.com, .ru, .goog)