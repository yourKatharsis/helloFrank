from TxtCard import TxtCard


def main():
    f = open('data/examples/deck_file.txt', 'r')
    cards = []
    for r in f:
        cards.append(TxtCard(row=r))
    for c in cards:
        print(f"")



if __name__ == '__main__':
    main()
