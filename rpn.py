def main():
    calculator()


def calculator():
    nums = []
    try:
        user_input = input("> ")
        while str(user_input) != "q":
            try:
                val = int(user_input)
                nums.append(val)
                print(val)
            except ValueError:
                try:
                    val = float(user_input)
                    nums.append(val)
                    print(val)
                except ValueError:
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
                        a = nums.pop()
                        out = a / b
                    elif str(user_input) == "q":
                        raise EOFError
                    else:
                        out = inline_calculator(list(user_input.split(" ")), nums)
                    if out is not None:
                        nums.append(out)
                        print(out)
                    else:
                        print(nums[-1])
            user_input = input("> ")
    except EOFError:
        pass


def inline_calculator(input_list, nums):
    out = None
    for user_input in input_list:
        try:
            val = int(user_input)
            nums.append(val)
        except ValueError:
            try:
                val = float(user_input)
                nums.append(val)
            except ValueError:
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
                    a = nums.pop()
                    out = a / b
                elif str(user_input) == "q":
                    raise EOFError
                else:
                    print("invalid input try again")
                if out is not None:
                    nums.append(out)
    return out


if __name__ == "__main__":
    main()
