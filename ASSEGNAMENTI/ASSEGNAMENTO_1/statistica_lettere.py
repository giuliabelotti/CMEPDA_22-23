'''
Module: basic Python
Assignment #1 (September 30, 2019)


Download a book (not covered by copyright) in plain-text format, e.g., from
https://www.gutenberg.org/

(If you have a hard time picking one, we suggest this English translation
of "The Republic" by Plato: http://www.gutenberg.org/cache/epub/1497/pg1497.txt)


--- Goal
Write a Python program that prints the relative frequence of each letter
of the alphabet (without distinguishing between lower and upper case) in the
book.

--- Specifications
- the program should have a --help option summarizing the usage
- the program should accept the path to the input file from the command line
- the program should print out the total elapsed time
- the program should have an option to display a histogram of the frequences
- [optional] the program should have an option to skip the parts of the text
  that do not pertain to the book (e.g., preamble and license)
- [optional] the program should have an option to print out the basic book
  stats (e.g., number of characters, number of words, number of lines, etc.)
'''
import logging
import argparse
import time
import matplotlib.pyplot as plt

logging.basicConfig(level=logging.INFO)
start=time.time()

index = []
f = []

def conteggio_lettere(file_path):
    """ Funzione che conta le lettere
    """
    logging.info('Opening file %s', file_path)
    with open(file_path) as book:
        b=book.read()
    logging.info('Done')


    lettere="abcdefghijklmnopqrstuwxyz"
    freq={}
    for i in lettere:
        freq[i]=0

    for i in b.lower():
        if i in lettere:
            freq[i]+=1

    for i,freq in freq.items():
        print(f'{i}: {freq}')
        index.append(i)
        f.append(freq)

def histogram():
    """ Funzione che disegna l'istogramma delle frequenze
    """
    plt.bar(index,f)

def statistica(file_path):
    """ Funzione che stampa la statistica del libro
    """
    tmp=[]

    with open(file_path) as book:
        b=book.read()

    characters=len(b)
    lines=len(b.split('\n'))

    for i in b.split('n'):
        for j in i.split(" "):
            if j!="":
                tmp.append(i.split(" "))
    n_of_words=len(tmp)

    logging.info('%d character found.', characters)
    logging.info('%d words found.', n_of_words)
    logging.info('%d lines found.', lines)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Lettura file')
    parser.add_argument('infile', help='path to the input file')
    parser.add_argument('--histogram', help='Draw the frequency histogram', action="store_true")
    parser.add_argument('--stats', \
    help='Book stats (number of characters, number of words, number of lines)', action="store_true")
    args = parser.parse_args()
    conteggio_lettere(args.infile)
    if args.histogram:
        histogram()
    if args.stats:
        statistica(args.infile)
    end=time.time()
    logging.info('Elapsed time %f s', end-start)
    plt.show()
