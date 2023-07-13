disc_size = 1.44*(1024**2)   # Размер памяти дискеты в байтах

page_count = 100
count_string_on_page = 50
count_simbol_on_page = 25

max_count_book_on_disk = int(disc_size / (page_count * count_string_on_page * count_simbol_on_page * 4))
print("Количество книг, помещающихся на дискету:", max_count_book_on_disk)
