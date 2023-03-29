from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_comment(self, data: str) -> None:
        multiline = True if len(data.split("\n")) > 1 else False
        if multiline:
            print(">>> Multi-line Comment")
        else:
            print(">>> Single-line Comment")
        print(data.strip())

    def handle_data(self, data: str) -> None:
        if data != "\n":
            print(">>> Data")
            print(data)


if __name__ == "__main__":
    N = int(input())
    parser = MyHTMLParser()
    parser.feed("\n".join([input().strip() for _ in range(N)]))
