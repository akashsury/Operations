class Operations:
    def __init__(self):
        pass

    def aboveBelow(self, values, comparison):
        dict = {"above": 0, "below": 0}             # created as local variable, each call it has to have zero
        if not isinstance(comparison, int) or not isinstance(values, list):
            return False
        for value in values:
            if not isinstance(value, int):
                return False
            elif value > comparison:
                dict["above"] += 1
            elif value < comparison:
                dict["below"] += 1
        return dict

    def stringRotation(self, input_string, rotation_value):
        if not isinstance(input_string, str) or not isinstance(rotation_value, int) or rotation_value < 0:
            return False
        if input_string:      # For handling Zero division
            str_len = len(input_string)
            rotate_by = rotation_value % str_len
            return input_string[str_len - rotate_by:] + input_string[:str_len - rotate_by]
        return input_string

operation = Operations()
print(operation.aboveBelow([1, 2, 3, 4, 5, 6], 3))
print(operation.aboveBelow([1, 2, 3, 4, 5, 6], -1))
print(operation.aboveBelow([1, 2, 3, 4, 5, 6], 100))
print(operation.aboveBelow([], 3))
print(operation.aboveBelow([3, 3, 3], 3))
print(operation.stringRotation("MyString", 2))
print(operation.stringRotation("MyString", 2001))
print(operation.stringRotation("MyString", 0))
print(operation.stringRotation("", 10))

# For invalid inputs printing false
print(operation.aboveBelow("", 3))
print(operation.stringRotation(3, 2))
print(operation.stringRotation("Mystring", -1))

