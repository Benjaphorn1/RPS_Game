def int_checker(to_check):
    """checks users enters an integer more than/equal to 13"""

    error = "please enter an integer more than/ equal to 13."

    while True:

        #check for infinite mode
        if to_check == "":
            return "infinite"
        try:
            response = int(to_check)

            if response < 1:
               # print(error)
                return "invalid"
            else:
                return response

        except ValueError:
            # print(error)
            return "invalid"

# Automated testing is below in the form (test_case, expected_value)
to_test = [
    ('xlii', 'invalid'),
    ('0.5', 'invalid'),
    ('0', 'invalid'),
    (1, 1),
    (2, 2),
    ('', 'infinite'),
]

# run tests!
for item in to_test:
    # retrieve test case and expected value
    case = item[0]
    expected = item[1]

    # get actual value (ie: test ticket function)
    actual = int_checker(case)

    # compare actual and expected and output pass / fail
    if actual == expected:
        print(f" ✅✅✅Passed! Case: {case}, expected: {expected}, received: {actual} ✅✅✅")
    else:
        print(f"❌❌❌ Failed! Case: {case}, expected: {expected}, received: {actual} ❌❌❌")