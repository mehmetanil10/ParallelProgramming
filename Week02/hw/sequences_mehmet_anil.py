def unique_elements(input_list: list) -> list:
    return list(set(input_list))

def count_occurrences(input_list: list) -> dict:
    element_counts = {}
    
    for element in input_list:
        if element in element_counts:
            element_counts[element] += 1
        else:
            element_counts[element] = 1
    
    return element_counts

def reverse_dictionary(input_dict: dict) -> dict:
    reversed_dict = {}

    for key, value in input_dict.items():
        reversed_dict[value] = key
    
    return reversed_dict

my_list = [10, "Different List", 52.600, False, 21 + 3j]
my_tuple = ("M", "Legend", "King")
my_set = {True, 1}
my_dict = {
    "full_name": "MehmetAnil",
    "nickname": "KraLex",
    "age": 24
}

unique_list = unique_elements(my_list)
occurrences = count_occurrences(my_list)
reversed_dict = reverse_dictionary(my_dict)

print("Unique Elements:", unique_list)
print("Element Occurrences:", occurrences)
print("Reversed Dictionary:", reversed_dict)
