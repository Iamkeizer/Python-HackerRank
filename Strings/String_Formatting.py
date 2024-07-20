def print_formatted(number):
    for i in range(1,number+1):
        print(str(i).rjust(len((bin(number).lstrip("0b")))),(oct(i).lstrip("0o")).rjust(len((bin(number).lstrip("0b")))),(hex(i).lstrip("0x")).rjust(len((bin(number).lstrip("0b")))).upper(),((bin(i).lstrip("0b")).rjust(len(bin(number).lstrip("0b")))))
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)