volume_bytes = 1.44 * 1024 *1024
weight_book_bytes = 100 * 50 * 25* 4
count_books = volume_bytes // weight_book_bytes
count_books = int(count_books)
print("Количество книг, помещающихся на дискету:", count_books)
