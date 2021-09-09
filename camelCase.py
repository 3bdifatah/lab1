def get_sentence():
    print('Enter a sentence to convert to camelCase: ')
    sentence=input()
    return sentence

def split_sentence(sentence):
    words=sentence.split()
    return words

def modify(words):
    camelCase=[]
    for word in words:
        camelCase.append(word.capitalize())
    return camelCase

def display_sentence(camelcase):
    string=''
    for word in camelcase:
        string+=word
    print(string)

def display_banner():
    """displays program name in banner"""
    msg = 'AWESOME camelCaseGenerator PROGRAM'
    stars = '*' *len(msg)
    print(f'\n {stars} \n {msg} \n {stars}')

def main():
    display_banner()
    sentence=get_sentence()
    words=split_sentence(sentence) 
    camelCase=modify(words)
    display_sentence(camelCase)
main()