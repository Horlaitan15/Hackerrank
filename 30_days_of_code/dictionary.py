def solve():
    phonebook = dict()
    for _ in range(int(input())):
        name, phone = input().split()
        phonebook[name] = phone

    while True:
        try:
            query_name = input()
            if query_name in phonebook:
                print(f"{query_name}={phonebook[query_name]}")
            else:
                print("Not found")
        except:
            break


if __name__ == "__main__":
    solve()