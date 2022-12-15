def binary_search(numbers, search_element, Low, High):
    if Low > High:
        return False
    else:
        Mid = (Low + High)//2
        if numbers[Mid] == search_element:
            return Mid
        else:
            if search_element < numbers[Mid]:
                return binary_search(numbers, search_element, Low, Mid-1)
            elif search_element > numbers[Mid]:
                return binary_search(numbers, search_element, Mid + 1, High)
            else:
                return -1


search_element = 16
numbers = [2,5,6,8,10,11,13,15,16]
result = binary_search(numbers, search_element, 0, len(numbers)-1)
if result != -1:
    print("Index", result)