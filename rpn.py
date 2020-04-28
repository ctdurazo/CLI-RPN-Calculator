def main():
    nums = []
    try:
        while True:
            try:
                user_input = input("> ")
                calculator(user_input, nums)
                print(nums[-1])
            except ZeroDivisionError:
                print("Cannot divide by 0")
                continue
    except EOFError:
        pass


def calculator(input_string, nums):
    input_list = list(input_string.split())
    for user_input in input_list:
        try:
            val = int(user_input)
            nums.append(val)
        except ValueError:  # user_input not an integer, try float
            try:
                val = round(float(user_input), 5)
                nums.append(val)
            except ValueError:  # user_input not an float, try operator
                get_operator(user_input, nums)


def get_operator(user_input, nums):
    if str(user_input) == "+" and len(nums) > 1:
        b = nums.pop()
        a = nums.pop()
        out = a + b
    elif str(user_input) == "-" and len(nums) > 1:
        b = nums.pop()
        a = nums.pop()
        out = a - b
    elif str(user_input) == "*" and len(nums) > 1:
        b = nums.pop()
        a = nums.pop()
        out = a * b
    elif str(user_input) == "/" and len(nums) > 1:
        b = nums.pop()
        if b != 0:
            a = nums.pop()
            out = round(a / b, 5)
        else:
            nums.append(b)
            raise ZeroDivisionError
    elif str(user_input) == "%" and len(nums) > 1:
        b = nums.pop()
        a = nums.pop()
        out = a % b
    elif str(user_input) == "^" and len(nums) > 1:
        b = nums.pop()
        a = nums.pop()
        out = a**b
    elif str(user_input) == "q":
        raise EOFError
    else:
        print("invalid input try again")
        out = None
    if out is not None:
        nums.append(out)


if __name__ == "__main__":
    main()
