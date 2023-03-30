print("This program takes some side-by-side operations and converts the to vertical operations and solves them.\n"
      "There are some restrictions of this program:\n"
      "1. It can take a maximum of 5 operations.\n"
      "2. The numbers can have maximum 4 digits.\n"
      "3. There must be a blank between numbers and operation symbols.\n"
      "4. You can enter only \"+\" and \"-\" operations.\n")
list_of_operations = []

for i in range(5):
    user_input = input("Enter a side-by-side operation to be written in vertical form(or press enter to stop): ")
    if len(list_of_operations) == 5:
        print("Error: Too many problems.")
        break
    if user_input == "":
        break
    list_of_operations.append(user_input)


def arithmetic_arranger(operations):
    n1 = []
    op_n2 = []
    n2 = []
    res = []
    for element in operations:
        elements = element.split()
        bl_len1 = 5 - int(len(elements[0]))
        bl_len2 = 5 - int(len(elements[2]))
        if not elements[0].isdigit() or not elements[2].isdigit():
            print("Error: Numbers must only contain digits.")
            break
        if len(elements[0]) > 4 or len(elements[2]) > 4:
            print("Error: Numbers cannot be more than four digits.")
            break
        if elements[1] != "+" and elements[1] != "-":
            print("Error: Operator must be '+' or '-'.")
            break
        blank1 = ""
        blank2 = ""
        blanks1 = ""
        blanks2 = ""
        m = 0
        n = 1
        while m < bl_len1:
            blank1 += " "
            m += 1
        elementss1 = blank1 + elements[0]

        while n < bl_len2:
            blank2 += " "
            n += 1
        elementss2 = blank2 + elements[2]

        if elements[1] == "+":
            res.append(int(elements[0]) + int(elements[2]))

        if elements[1] == "-":
            res.append(int(elements[0]) - int(elements[2]))

        n1.append(elementss1)
        op_n2.append(elements[1] + elementss2)
        n2.append(elementss2)
    l1 = ""
    l2 = ""
    l3 = "-----    "
    l4 = ""

    for n11 in n1:
        l1 += n11
        l1 += "    "
    print(l1)
    for opp_n2 in op_n2:
        l2 += opp_n2
        l2 += "    "
    print(l2)
    k = 0
    d_line = ""
    while k < len(n1):
        d_line += l3
        k += 1
    print(d_line)
    for ress in res:
        p = len(str(ress))
        r = 5 - p
        s = 1
        while s <= r:
            l4 += " "
            s += 1
        l4 += str(ress)
        l4 += "    "
    print(l4)


arithmetic_arranger(list_of_operations)

