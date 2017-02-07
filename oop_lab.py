class Books:
    def __init__(self, title, author, publisher, isbn):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.isbn = isbn

    def view_book_info(self):
        return "Title: {}," \
               "Author: {}" \
               "ISBN: {}" \
               "Publisher".format(self.title, self.author, self.isbn, self.publisher)


class FictionBooks(Books):
    def __init__(self, title, author, publisher, isbn, genre, form):
        Books.__init__(self, title, author, publisher, isbn)
        self.genre = genre
        self.form = form  # e.g short story, comic book, etc

    def view_book_info(self):
        return Books.view_book_info(self) + "Genre: {}" \
                                        "form: {}".format(self.genre, self.form)


class TextBooks(Books):
    def __init__(self, title, author, publisher, isbn, subject, level, difficulty):
        Books.__init__(self, title, author, publisher, isbn)
        self.subject = subject
        self.level = level  # level of student it is intended for e.g high school
        self.difficulty = difficulty  # beginner, intermediate or advanced

    def view_book_info(self):
        return Books.view_book_info(self) + "Subject: {}" \
                                        "Level: {}" \
                                        "Difficulty {}".format(self.subject, self.level, self.difficulty)

ac = TextBooks('Advanced Calculus',
               'John Smith',
               'Harper Collins',
               '1232312',
               'Calculus',
               'University',
               'Advanced')

got = FictionBooks('Game of Thrones',
                   'George R.R. Martin',
                   'Harper Collins',
                   '9780553386790',
                   'Fantasy',
                   'Novel')
print(ac.title)
print(got.author)
