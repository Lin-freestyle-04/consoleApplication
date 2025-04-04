import hashlib

users = {}
posts = []

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

#signup method
def register_user():
    while True:
        username = input("Enter your username: ")
        if username in users:
            print("Username already exists. Please choose another one.")
        else:
            break
    password = input("Enter your password: ")
    users[username] = {'password': [hash_password(password)], 'posts': []}
    print("Signup successful!")

# login method
def login_user():
    username = input("Enter your username: ")
    if username not in users:
        print("Username not found.")
        return None
    attempts = 3  # Allow 3 attempts
    while attempts > 0:
        password = input("Enter your password: ")
        if hash_password(password) == users[username]['password'][-1]:
            print("Login successful!")
            return username
        else:
            attempts -= 1
            if attempts > 0:
                print(f"Incorrect password. You have {attempts} attempts left.")
            else:
                print("Incorrect password. No attempts left.")
                return None

#change password method
def change_password(username):
    current_password = input("Enter your current password: ")
    if hash_password(current_password) != users[username]['password'][-1]:
        print("Incorrect current password.")
        return
    new_password = input("Enter new password: ")
    if hash_password(new_password) in users[username]['password']:
        print("You can't use any of the last 3 passwords.")
        return
    users[username]['password'].append(hash_password(new_password))
    if len(users[username]['password']) > 3:
        users[username]['password'].pop(0)
    print("Password changed successfully!")

#postContent method
def post_content(username):
    content = input("Enter your post content: ")
    visibility = input("Enter visibility (public/private): ").lower()
    if visibility not in ["public", "private"]:
        print("Invalid visibility option.")
        return
    posts.append({'username': username, 'content': content, 'visibility': visibility})
    users[username]['posts'].append({'content': content, 'visibility': visibility})
    print("Post added successfully!")

#view posts method
def view_posts():
    for post in posts:
        if post['visibility'] == 'public':
            print(f"{post['username']} (Public): {post['content']}")
        else:
            print(f"{post['username']} (Private): {post['content']}")

# Main menu
def main():
    while True:
        print("\nMenu:")
        print("1. Signup")
        print("2. Login")
        print("3. View Posts")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            register_user()
        elif choice == "2":
            username = login_user()
            if username:
                while True:
                    print("\nUser Menu:")
                    print("1. Change Password")
                    print("2. Post Content")
                    print("3. Logout")
                    user_choice = input("Enter your choice: ")
                    if user_choice == "1":
                        change_password(username)
                    elif user_choice == "2":
                        post_content(username)
                    elif user_choice == "3":
                        break
        elif choice == "3":
            view_posts()
        elif choice == "4":
            print("Exiting application.")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
