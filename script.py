from read_dataset import create_list, filter_list, show

def main():
    exit_or_not = ''
    while exit_or_not != 'y':
        char = ''
        alist = create_list(f"{dataset}")
        while True:
            char += input("\nQuale autore desideri leggere? Digita una lettera per filtrare nel nostro ampio catalogo. " + char)
            alist = filter_list(alist, char)
            print(char)
            print(alist)
            if not alist:
                char = ''
                alist = create_list(f"{dataset}")
                print("\nC'è un errore... Non esiste nessun autore nel nostro catalogo che contiene la serie di caratteri da te scelta. ")
                continue
            if len(alist) == 1:
                choice = input("\nContento? Digita 'y' se hai scelto o 'n' se vuoi rifare una ricerca. ")
                print(choice)
                choice = ask_again(choice)
                if choice == 'y':
                    show(f"{dataset}", alist[0])
                    break
                else:
                    alist = create_list(f"{dataset}")
                    char = ''
                    continue
        exit_or_not = input("\nSe vuoi uscire digita 'y', se invece vuoi continuare a cercare premi 'n'. ")
        exit_or_not = ask_again(exit_or_not)

    print('\nA presto!\n')

def ask_again(var):
    while var != 'n' and var != 'y':
        var = ''
        var = input("\nDevi inserire 'y' o 'n'. ")
        print(var)
    return var

dataset = "books.csv"   

main()