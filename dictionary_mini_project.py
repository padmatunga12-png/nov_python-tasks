dictionary = {}
while True:
    print("\nDictionary Management System")
    print("1. add a word")
    print("2. search for meaning")
    print("3. display all words")
    print("4. update meaning")
    print("5.delete word")
    print("6.exit")
    choice = input("enter your choice:")
    if choice == "1":
        word = input("enter the word:").lower()
        meaning = input("enter the meaning:")
        dictionary[word] = meaning
        print("word added successfully!")
    elif choice == '2':
        word = input("enter word to search:").lower()
        if word in dictionary:
            print("meaning:", dictionary[word])
        else:
            print("word not found in the dictionary")
    elif choice == '3':
        if dictionary:
            print("words and their meanings:")
            for word, meaning in dictionary.items():
                print(f"{word}:{meaning}")
            else:
                print("dictionary is empty")
    elif choice == '4':
        word = input("enter the word to update meaning:").lower()
        if word in dictionary:
            new_meaning = input("enter the new meaning:")
            dictionary[word] = new_meaning
            print("meaning updated successfully!")
            print("updated meaning:", dictionary[word])
        else:
            print("word not found in the dictionary")
    elif choice == '5':
        word = input("enter the word to delete:").lower()
        if word in dictionary:
            del dictionary[word]
            print("word deleted successfully!")
        else:
            print("word not found in the dictionary")
    elif choice == '6': 
        print("exiting program.....")
        break
    else:
        print("invalid choice! please enter a valid option")
               
    