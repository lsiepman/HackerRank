from html.parser import HTMLParser


class FindSolution(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(f"Start : {tag}")
        for i in attrs:
            print(f"-> {i[0]} > {i[1]}")

    def handle_endtag(self, tag):
        print(f"End   : {tag}")

    def handle_startendtag(self, tag, attrs):
        print(f"Empty : {tag}")
        for i in attrs:
            print(f"-> {i[0]} > {i[1]}")


if __name__ == "__main__":
    N = int(input())
    parser = FindSolution()
    parser.feed("".join([input().strip() for _ in range(N)]))
