def execute_commands(s, cmds):
    for cmd in cmds:
        if "pop" in cmd:
            s.pop()

        elif "remove" in cmd:
            _, n = cmd.split()
            s.remove(int(n))

        elif "discard" in cmd:
            _, n = cmd.split()
            s.discard(int(n))

    return s


if __name__ == "__main__":
    n_set = int(input())
    items = set(map(int, input().split()))
    n_cmd = int(input())
    cmds = []
    for _ in range(n_cmd):
        cmds.append(input())

    result = execute_commands(items, cmds)
    print(sum(result))
