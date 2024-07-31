import re

def assess_password_strength(password):
    length_weight = 1
    uppercase_weight = 1
    lowercase_weight = 1
    number_weight = 1
    special_weight = 1


    score = 0
    feedback = []

    if len(password) >= 8:
        score += length_weight
    else:
        feedback.append("Password should be at least 8 characters long.")

    if re.search(r'[A-Z]', password):
        score += uppercase_weight
    else:
        feedback.append("Password should include at least one uppercase letter.")

    if re.search(r'[a-z]', password):
        score += lowercase_weight
    else:
        feedback.append("Password should include at least one lowercase letter.")

    if re.search(r'\d', password):
        score += number_weight
    else:
        feedback.append("Password should include at least one number.")

    if re.search(r'[\W_]', password):
        score += special_weight
    else:
        feedback.append("Password should include at least one special character (e.g., !, @, #, $, etc.).")

    total_possible_score = (length_weight + uppercase_weight + lowercase_weight + number_weight + special_weight)

    strength = (score / total_possible_score) * 100

    if strength == 100:
        feedback.append("Your password is very strong.")
    elif strength >= 80:
        feedback.append("Your password is strong.")
    elif strength >= 60:
        feedback.append("Your password is moderate.")
    else:
        feedback.append("Your password is weak.")

    return strength, feedback

password = input("Enter a password to assess its strength: ")
strength, feedback = assess_password_strength(password)

print(f"Password Strength: {strength:.2f}%")
print("Feedback:")
for message in feedback:
    print(f"- {message}")
