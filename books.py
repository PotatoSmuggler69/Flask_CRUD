books = [
    (1, "To Kill a Mockingbird", "Harper Lee", 600, 336, True),
    (2, "1984", "George Orwell", 450, 328, True),
    (3, "Pride and Prejudice", "Jane Austen", 350, 279, False),
    (4, "The Lord of the Rings", "J.R.R. Tolkien", 1200, 1178, True),
    (5, "The Hitchhiker's Guide to the Galaxy", "Douglas Adams", 300, 224, False),
    (6, "The Great Gatsby", "F. Scott Fitzgerald", 400, 180, True),
    (7, "Harry Potter and the Philosopher's Stone", "J.K. Rowling", 500, 223, True),
    (8, "The Alchemist", "Paulo Coelho", 350, 197, False),
    (9, "The Diary of a Young Girl", "Anne Frank", 400, 283, True),
    (10, "The Catcher in the Rye", "J.D. Salinger", 450, 234, True),
    (11, "The Little Prince", "Antoine de Saint-Exupéry", 300, 96, False),
    (12, "The Picture of Dorian Gray", "Oscar Wilde", 400, 254, True),
    (13, "The Hunger Games", "Suzanne Collins", 500, 374, True),
    (14, "The Fault in Our Stars", "John Green", 450, 313, False),
    (15, "The Giver", "Lois Lowry", 350, 240, False),
    (16, "The Time Traveler's Wife", "Audrey Niffenegger", 500, 546, True),
    (17, "The Count of Monte Cristo", "Alexandre Dumas", 600, 1276, True),
    (18, "The Three Musketeers", "Alexandre Dumas", 450, 704, True),
    (19, "The Secret Garden", "Frances Hodgson Burnett", 350, 288, False),
    (20, "The Chronicles of Narnia", "C.S. Lewis", 1000, 767, True),
    (21, "The Book Thief", "Markus Zusak", 500, 584, True),
    (22, "The Kite Runner", "Khaled Hosseini", 450, 371, True),
    (23, "The Da Vinci Code", "Dan Brown", 600, 489, True),
    (24, "The Handmaid's Tale", "Margaret Atwood", 500, 311, True),
    (25, "The Shining", "Stephen King", 450, 447, True),
    (26, "The Godfather", "Mario Puzo", 500, 448, True),
    (27, "The Color Purple", "Alice Walker", 400, 295, True),
    (28, "The Book of Lost Things", "John Connolly", 500, 339, False),
    (29, "The Nightingale", "Kristin Hannah", 450, 440, False),
    (30, "The Martian", "Andy Weir", 500, 369, False),
    (31, "The Girl on the Train", "Paula Hawkins", 450, 316, False),
    (32, "The Girl with the Dragon Tattoo", "Stieg Larsson", 500, 672, True),
    (33, "The Curious Incident of the Dog in the Night-Time", "Mark Haddon", 400, 226, False),
    (34, "The Perks of Being a Wallflower", "Stephen Chbosky", 350, 213, False),
    (35, "The Help", "Kathryn Stockett", 400, 451, True),
    (36, "The Girl with the Tattooed Dragon", "Stieg Larsson", 500, 672, True),
    (37, "The Girl Who Played with Fire", "Stieg Larsson", 450, 724, True),
    (38, "The Girl Who Kicked the Hornet's Nest", "Stieg Larsson", 500, 800, True),
    (39, "The House in the Cerulean Sea", "T.J. Klune", 450, 396, False),
    (40, "The Midnight Library", "Matt Haig", 400, 288, False)
]


books_dict = {}
for book in books:
    book_id, title, author, price, pages, is_bestseller = book
    books_dict[book_id] = {
        "title": title,
        "author": author,
        "price": price,
        "pages": pages,
        "is_bestseller": is_bestseller
    }