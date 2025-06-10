def get_company_abbreviation(company_name):
    words = company_name.split()
    first_letters = [word[0] for word in words]

    abbreviation = ''.join(first_letters).upper()

    print(abbreviation)

get_company_abbreviation("International Business Machines")  # Output: IBM
get_company_abbreviation("Tech Solutions Limited")           # Output: TSL
