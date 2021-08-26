def get_sentence():
    print('enter sentence: ')
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

def main():
    sentence=get_sentence()
    words=split_sentence(sentence) 
    camelCase=modify(words)
    display_sentence(camelCase)
main()