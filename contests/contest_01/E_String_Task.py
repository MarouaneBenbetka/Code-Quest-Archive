def process_string(s):
    vowels = "AOYEUIaoyeui"
    result = ""
    for char in s:
        if char not in vowels:
            result += "." + char.lower()
    return result


input_string = input()
print(process_string(input_string))
