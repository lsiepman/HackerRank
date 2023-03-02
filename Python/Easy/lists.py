def execute_commands(command, vals, lst):
    """Execute commands given in the input

    Args:
        command (str): One of "print, insert, remove, append,
            pop, reverse, sort"
        vals (list): all input trailing behind the command
        lst (list): List that needs to be altered

    Raises:
        ValueError: When an unknown command is used

    Returns:
        list: list that was altered
    """
    if command == "print":
        print(lst)
    elif command == "insert":
        lst.insert(int(vals[0]), int(vals[1]))
    elif command == "remove":
        lst.remove(int(vals[0]))
    elif command == "append":
        lst.append(int(vals[0]))
    elif command == "pop":
        lst.pop()
    elif command == "reverse":
        lst.reverse()
    elif command == "sort":
        lst.sort()
    else:
        raise ValueError("Unknown command")

    return lst


if __name__ == "__main__":
    lst = []
    N = int(input())
    for _ in range(N):
        cmd, *val = input().split()
        lst = execute_commands(cmd, val, lst)
