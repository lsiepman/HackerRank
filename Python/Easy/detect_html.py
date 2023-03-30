from html.parser import HTMLParser


class MyHTMLparser(HTMLParser):
    def handle_starttag(self, tag: str, attrs) -> None:
        print(tag)
        if len(attrs) > 0:
            for i in attrs:
                print(f"-> {i[0]} > {i[1]}")


if __name__ == "__main__":
    N = int(input())
    parser = MyHTMLparser()
    parser.feed("".join([input().strip() for _ in range(N)]))
