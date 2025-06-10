def verify_guest_lists(list1, list2):
    list1_lower = [name.lower() for name in list1]
    list2_lower = [name.lower() for name in list2]

    list1_sorted = sorted(list1_lower)
    list2_sorted = sorted(list2_lower)

    if list1_sorted == list2_sorted:
        print("Lists match")
    else:
        print("Lists do not match")



verify_guest_lists(['Alice', 'Bob'], ['bob', 'ALICE'])  
verify_guest_lists(['Alice', 'Charlie'], ['bob', 'ALICE'])
