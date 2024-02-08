from connection import connect
from models import Qoutes, Authors

def select_tag():
    new_input = input('Enter tag: ')
    quotes = Qoutes.objects(tags=new_input)
    for q in quotes:
        print(q.quote)


def select_tags():
    new_input = input('Enter tags: ')
    quotes = Qoutes.objects(tags__in=new_input.split(' '))
    for q in quotes:
        print(q.quote)


def select_name():
    new_input = input('Enter name: ')
    author = Authors.objects(fullname=new_input)
    for a in author:
        id = a.id
    quotes = Qoutes.objects(author=id)
    for q in quotes:
        print(q.quote)

if __name__ == '__main__':
    while True:
        user_input = input('Please enter command: ')
        if user_input == 'exit':
            break
        elif user_input == 'tag':
            select_tag()
        elif user_input == 'tags':
            select_tags()
        elif user_input == 'name':
            select_name()
