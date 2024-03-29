import json
from models import Authors, Qoutes
from connection import connect


def load_json():
    with open('authors.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

        for itr in data:
            new_author = Authors()
            new_author.fullname = itr['fullname']
            new_author.born_date = itr['born_date']
            new_author.description = itr['description']
            new_author.born_location = itr['born_location']
            new_author.save()

    with open('quotes.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

        for itr in data:
            authors = Authors.objects(fullname=itr['author']).first()
            new_quotes = Qoutes()
            new_quotes.author = authors
            new_quotes.tags = itr['tags']
            new_quotes.quote = itr['quote']
            new_quotes.save()


if __name__ == '__main__':
    load_json()
    




    