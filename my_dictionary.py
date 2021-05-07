dictionary = {"멋사": "멋쟁이 사자처럼", "파이썬": "지금 배우는 언어"}


def create_word():
    # 함수를 완성해보세요.


def read_dictionary():
    # 함수를 완성해보세요.


def update_word():
    # 함수를 완성해보세요.


def delete_word():
    # 함수를 완성해보세요.


def console_help():
    print("Command list")
    print("---")
    print("C for create")
    print("R for read")
    print("U for update")
    print("D for delete")
    print("Q for quit")


def receive_input():
    command = input("Input command: ")
    if command == 'c' or command == 'C':
        create_word()
        return True
    if command == 'r' or command == 'R':
        read_dictionary()
        return True
    if command == 'u' or command == 'U':
        update_word()
        return True
    if command == 'd' or command == 'D':
        delete_word()
        return True
    if command == 'q' or command == 'Q':
        return False
    else:
        print("Please enter one of the letters above.")
        return True


def main():
    console_help()
    while receive_input():
        pass


if __name__ == "__main__":
    main()