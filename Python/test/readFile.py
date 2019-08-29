
author = input("")
book = input("")
genre = input("")

file = open("book.json", "w")
file.write('{"author":"' + author + '","book":"' + book + '","genre":"' + genre + '"}')
file.close()
