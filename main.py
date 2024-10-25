def main():
    sorted_list = []
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count=number_of_words(text)
    letter_count = character_count(text)
    sorted_list = sorting(letter_count)
    for letter in sorted_list:
        if not letter["char"].isalpha():
            continue
        print(f"Character: {letter["char"]} was used total of: {letter["num"]}")
    #print(" --- Book report subject: Frankenstein ---\n")
    #print(f"Total amount of words in the book is: {word_count}\n")
    #print(F"Here is the numper of all characters used:\n")
    #char_print(letter_count)

def char_print(dict):
    for character in dict:
        count = dict[character]
        print(f"Character: `{character}` was used total of: {count} times")
    return

def sort_on(dict):
    return dict["num"]

def sorting(dict):
    list=[]
    for c in dict:
        list.append({"char": c, "num": dict[c]})
    list.sort(reverse=False, key=sort_on)
    return list

def character_count(text):
    char_count={}
    lower_text=text.lower()
    letters=list(lower_text)
    for letter in letters:
        if letter == " ":
            letter = "Space"
        if letter in char_count:
            char_count[letter]+=1
        else:
            char_count[letter]=1
    return char_count

def number_of_words(text):
    words=text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()
    

main()