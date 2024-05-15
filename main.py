def count_words(file_content):
    words = file_content.split()
    return(len(words))

def count_letters(file_content):
    dict = {}
    for i in file_content:
        if i.lower() not in dict.keys():
            dict[i.lower()]=1
        else:
            dict[i.lower()]+=1
    return dict

def create_report(letters,words):
    with open('report.txt','w') as f:
        f.write(f'{words} words found in the document\n')
        letters = dict(sorted(letters.items() , key= lambda item : item[1],reverse=True))
        for i,j in letters.items():
            if i.isalpha():
                f.write(f"The '{i}' character was found with {j} times\n")


with open('books/frankestine.txt') as f:
    file_contents = f.read()

letters = count_letters(file_contents)
words = count_words(file_contents)

create_report(letters,words)