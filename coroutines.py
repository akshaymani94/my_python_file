import time
def searcher():
    book = "This is a code for corouitine"
    time.sleep(4)

    while True:
        text = (yield)
        if text in book:
            print("Your text is in the book")
        else:
            print("Your text is not in the book")

search = searcher()
next(search)
search.send("code")

search.close()

 