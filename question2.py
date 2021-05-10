import csv
import pprint
import collections
import itertools

path_r = '/Users/keisu/Documents/GitHub/zone-energy/prime.txt'

# O(√N)
def is_prime(n):
    if n == 1:
        return True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a


def get_unique_list(seq):
    seen = []
    return [x for x in seq if x not in seen and not seen.append(x)]


def main():

    with open(path_r) as f:
            reader = csv.reader(f, delimiter=' ')
            l = [row for row in reader]
            print("l: ", l)
            print("l[1]: ", l[1])
            print("l[1][6]: ", l[1][6])

    # 二次元を一次元に
    list_l = list(itertools.chain.from_iterable(l))
    print("Flatten: ", list_l)

    '''
    # リストの重複した要素を削除し、新たなリストを生成
    removed_list_l = list(set(list_l))
    print("Remove duplicate elements: ", removed_list_l)
    '''

    length = len(list_l)
    print("Element number: ", length)

    prime_count = 0
    for i in range(length):
        s = list_l[i]
        p = is_prime(int(s))
        print(s, end='')
        if p == True:
            prime_count += 1
            print(" True")
        else:
            print(" False")
    
    print("Prime counter: ", prime_count)

    # 二次元リストの重複した要素を削除し、新たなリストを生成
    # print(get_unique_list(l))

    '''
    c = collections.Counter(prime_factorize(2))
    print(c)

    for i in range(20):
        for j in range(20):
            print("i=", i, "j=", j, "l[i][j]: ", l[i][j])
            c = collections.Counter(prime_factorize(int(l[i][j])))
            print(c)

            # 重複した要素を削除し、新たなリストを生成
            print(get_unique_list(l[i]))

    prime_count = 0
    for i in range(20):
        for j in range(20):
            p = is_prime(int(l[i][j]))
            if p == True:
                prime_count += 1
    
    print("Prime counter: ", prime_count)

    '''

if __name__ == '__main__':
    main()
    print("Done!")
