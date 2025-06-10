company_name = input("Enter the full company name: ")

# Split the name into words and take the first letter of each
abbreviation = ''.join(word[0].upper() for word in company_name.split())

print("Abbreviation:", abbreviation)
