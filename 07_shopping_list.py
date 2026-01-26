def shopping_list():
    my_list = []
    
    while True:
        item = input("What do you want to buy? (Writes exit to finish): ")
        if item.lower() == "exit":
            break

        my_list.append(item)
        print(f'added: {item}')

    for product in my_list:
        print(f"- {product}")

shopping_list()
