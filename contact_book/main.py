#use python dictionaries to create a function that prompts a user to enter their name and number and 
#display what the contact book looks like at the moment

def contact_book(name, phone):
    book = {}
    book["name"] = name
    book["phone"] = phone
    
    return book

print(contact_book("Ayanda", "0743283003"))
