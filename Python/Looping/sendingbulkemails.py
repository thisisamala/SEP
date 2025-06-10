email_list = list(map(str, input("Enter the emails separated by space: ").split()))
email_content=("Hello! This is a promotional email. Enjoy our offers!")
print("\n")
for email in email_list:
    print("Sending email to :",email)
    print("Content:",email_content)
    print("Email sent!\n")

email_list = ["user1@example.com", "user2@example.com", "user3@example.com"]
email_content = "Hello! This is a promotional email. Enjoy our offers!"