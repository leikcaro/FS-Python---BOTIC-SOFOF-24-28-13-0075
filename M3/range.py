lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
n=5
for i in range(len(lista)):
    # This will iterate over the indices of the list
    
    if i < n:
        print(i)
    if i == n:
        print("acá me detengo")
# This code will print numbers from 0 to 4, one per line.