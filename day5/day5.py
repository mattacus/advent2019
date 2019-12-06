def password_test(password):
    # Adjacent number criteria
    str_pwd = str(password)
    has_adjacent = False
    for idx, digit in enumerate(str_pwd):
        if idx < len(str_pwd) - 1:
            if digit == str_pwd[idx + 1]:
                has_adjacent = True

    # Increasing digit criteria
    digits = [int(d) for d in list(str_pwd)]
    is_increasing = digits == sorted(digits)

    return has_adjacent & is_increasing


input_range = range(152085, 670283)
input_list = list(input_range)
criteria_pwds = [pwd for pwd in input_list if password_test(pwd)]
print(criteria_pwds)
print(len(criteria_pwds))
