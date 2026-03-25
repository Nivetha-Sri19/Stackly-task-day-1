def format_sentence():
    name = input("Enter your name: ")
    product = input("Enter product name: ")

    sentence = f"{name} bought a {product}"
    print("\nFormatted Sentence:")
    print(sentence)

def show_padding():
    text = input("\nEnter text for padding: ")

    print("\nLeft Align  : ", text.ljust(20, "*"))
    print("Right Align : ", text.rjust(20, "*"))
    print("Center Align: ", text.center(20, "*"))

def main():
    format_sentence()
    show_padding()

main()