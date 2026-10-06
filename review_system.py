   
def process_review(email, review_text):
    
    review_text = review_text.strip().title()

    
    at_position = email.index("@")

    
    username = email[:at_position]

    username = username.strip()

    return username, review_text


def calculate_average(ratings):
    total = sum(ratings)

    if len(ratings) > 0:
        average = total / len(ratings)
    else:
        average = 0

    return f"Total: {total}, Average: {average:.2f}"


reviewer_emails = []


ratings = []


while True:
    email = input("Enter reviewer email: ")

    review = input("Enter your review: ")

    
    username, cleaned_review = process_review(email, review)

    print("Username:", username)
    print("Cleaned Review:", cleaned_review)

    
    reviewer_emails.append(email)

    
    rating_input = input("Enter product rating (1-5) or 'done': ")

    if rating_input.lower() == "done":
        break

    rating = int(rating_input)
    ratings.append(rating)


print("\nRating Results")
print(calculate_average(ratings))


unique_reviewers = set(reviewer_emails)

print("\nUnique Reviewers:", unique_reviewers)
print("Number of unique reviewers:", len(unique_reviewers))