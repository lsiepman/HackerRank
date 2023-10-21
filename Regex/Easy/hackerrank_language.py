import re


def check_lan(s):
    if re.search(
        "[0-9]+ (C|CPP|JAVA|PYTHON|PERL|PHP|RUBY|CSHARP|HASKELL|CLOJURE|BASH|SCALA|ERLANG|CLISP|LUA|BRAINFUCK|JAVASCRIPT|GO|D|OCAML|R|PASCAL|SBCL|DART|GROOVY|OBJECTIVEC)$",
        s,
    ):
        print("VALID")
    else:
        print("INVALID")


if __name__ == "__main__":
    N = int(input())
    for _ in range(N):
        check_lan(input())
