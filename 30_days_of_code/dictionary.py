def solve():
    # Creates a dictionary object to store phonebook.
    phonebook = dict()

    # Iterates through the number of contacts to be stored.
    for _ in range(int(input())):
        name, phone = input().split()
        phonebook[name] = phone

    # Since there is no actual number of queries, i decided to check the end of the queries with a while loop.
    while True:
        try:
            # Takes the query name.
            query_name = input()

            # Searches phonebook for the query name.
            if query_name in phonebook:
                print(f"{query_name}={phonebook[query_name]}")
            else:
                print("Not found")
        except:
            break


if __name__ == "__main__":
    solve()