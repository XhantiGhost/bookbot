# Function to read the contents of a file and return it as a string
def get_book_text(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        return file.read()

# Main function to print the book contents
def main():
    book_path = "bookbot/books/frankenstein.txt"
    book_text = get_book_text(book_path)
    print(book_text)

# Call main to execute the program
if __name__ == "__main__":
    main()
