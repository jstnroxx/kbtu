# Examples
import re

# Search
txt = "The rain in Spain"
x = re.search(r"\s", txt)
print("The first white-space character is located in position:", x.start())

x = re.search("Portugal", txt)
print(x)

# Findall
x = re.findall("ai", txt)
print(x)

x = re.findall("Portugal", txt)
print(x)

# Split
x = re.split(r"\s", txt)
print(x)

x = re.split(r"\s", txt, maxsplit = 1) # control the number of occurences
print(x)

# Sub
x = re.sub(r"\s", "9", txt)
print(x)

x = re.sub(r"\s", "9", txt, count = 2) # control the number of replacements
print(x)


# Exercises
# 1
text = "abbbb"
x = re.search("^ab*$", text)
if x:
    print("Match")
else:
    print("Not match")

# 2
text = "abbb"
x = re.search("^ab{2,3}$", text)
if x:
    print("Match")
else:
    print("Not match")

# 3
text = "The rapid_fox jumps over the lazy_dog in a python_script. Ignore THIS_THAT and 123_456."
x = re.findall("[a-z]+_[a-z]+", text)
print(" ".join(x))

# 4
x = re.findall(r"\b[A-Z][a-z]+", text)
print(" ".join(x))

# 5
text = "ab fsgsdgsd  gsdbb"
x = re.search("^a.*b$", text)
if x:
    print("Match")
else:
    print("Not match")

# 6
text = " ,. dasd s.asd, dsa."
x = re.sub("[ ,.]", ":", text)
print(x)

# 7
text = "some_snake_case_text"
x = re.sub("_[a-z]", lambda match : match.group()[1].upper(), text)
print(x)

# 8
text = "someCamelCaseText"
x = re.split("[A-Z]", text)
print(x)

# 9
text = "Some Words Starting With Capital Letters"
x = re.sub("[A-Z]", lambda match : " " + match.group(), text)
print(x)

# 10
text = "someCamelCaseTextToSnakify"
x = re.sub("[A-Z]", lambda match : "_" + match.group().lower(), text)
print(x)