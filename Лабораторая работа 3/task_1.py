def search_item(list_produck, produck):
    count = 0
    for item in list_produck:
        if item == produck:
           return count
        else:
           count += 1


items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = search_item(items_list, find_item)
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")


# def funkcia(list_produck, produck):
    #for i, t in enumerate(list_produck):
        #if t == produck:
            #return i





