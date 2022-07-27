def main():
    a_list = [2, 4, 6, 8]
    result = some_function(a_list, 3)
    print(result)
def some_function(a_list, multiplier):
    a_list.reverse()
    for a in a_list:
        a = a * multiplier

main()
