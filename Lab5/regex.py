import re

#1 zeroOrMoreB()
def match_a_b():
    return bool(re.fullmatch(r'a[b]*', txt))


#2 twoORthree()
def match_a_bb():
    return bool(re.fullmatch(r'a{1}b{2,3}', txt))


#3 sequenceOfLowerLetters()
def find_lowercase_underscore():
    return re.findall(r'[a-z]+_[a-z]+', txt)  


#4 findAa()
def findAa():
    txt = input()
    x = re.findall("[A-Z][a-z]+", txt)
    print(x)


#5 startWithAEndWithB()
def startWithAEndWithB():
    txt = input()
    x = re.findall("^a.*b$", txt)
    print(x)


#6 replace()
def replace():
    txt = input("Enter a string: ")
    result = re.sub(r'[\s.,]', ":", txt)
    print(result)  


#7 snakeToCamel()
def snake_to_camel():
    txt = input("Enter: ")
    words = txt.split("_")
    camel_case = words[0] + "".join(word.capitalize() for word in words[1:])  
    print(camel_case) 


#8 splitUpper()
def split_at_uppercase(s):
    return re.split(r'(?=[A-Z])', s)


#9 splitUpper2()
def split_upper_case():
    txt = input("Enter a string: ")
    result = re.sub(r'([A-Z][a-z]*)', r' \1', txt).strip()
    print(result)


#10 camelToSnake()
def camel_to_snake():
    txt = input("Enter a CamelCase string: ")
    snake_case = re.sub(r'([a-z])([A-Z])', r'\1_\2', txt).lower() 
    print(snake_case)

