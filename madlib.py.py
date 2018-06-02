sentence = '''
Stop {}ing your {} {} {}s!
'''

def main():
    noun = input("Type a noun: ")
    verb = input("Type a verb: ")

    adjs = []
    adjs.append(input("Type an adjective: "))
    adjs.append(input("Type another adjective: "))

    madlib = sentence.format(verb,
                             adjs[0],
                             adjs[1],
                             noun)
    print(madlib)

main()
