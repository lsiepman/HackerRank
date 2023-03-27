from collections import deque


def execute_command(command, dq):
    if "appendleft" in command:
        cmd, val = command.split()
        dq.appendleft(int(val))
    elif "append" in command:
        cmd, val = command.split()
        dq.append(int(val))
    elif "popleft" in command:
        dq.popleft()
    elif "pop" in command:
        dq.pop()
    else:
        print("Unknown command")

    return dq


if __name__ == "__main__":
    N = int(input())
    dq = deque()
    for _ in range(N):
        inp = input()
        dq = execute_command(inp, dq)

    print(" ".join(map(str, dq)))
