#1.Homework 1. ToDo List Application

Define Task Class:
Create a Task class with attributes such as task title, description, due date, and status.
Define ToDoList Class:
Create a ToDoList class that manages a list of tasks.
Include methods to add a task, mark a task as complete, list all tasks, and display incomplete tasks.
Create Main Program:
Develop a simple CLI to interact with the ToDoList.
Include options to add tasks, mark tasks as complete, list all tasks, and display only incomplete tasks.
Test the Application:
Create instances of tasks and test the functionality of your ToDoList.

  from datetime import datetime

class Task:
    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = datetime.strptime(due_date, "%Y-%m-%d")
        self.completed = False

    def mark_complete(self):
        self.completed = True

    def __str__(self):
        status = "Done" if self.completed else "Pending"
        return f"Title: {self.title}\nDescription: {self.description}\nDue Date: {self.due_date.date()}\nStatus: {status}"

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def mark_task_complete(self, title):
        for task in self.tasks:
            if task.title.lower() == title.lower():
                task.mark_complete()
                return f"Task '{title}' marked as complete."
        return f"Task '{title}' not found."

    def list_all_tasks(self):
        if not self.tasks:
            return "No tasks found."
        return "\n\n".join(str(task) for task in self.tasks)

    def list_incomplete_tasks(self):
        incomplete = [task for task in self.tasks if not task.completed]
        if not incomplete:
            return "All tasks are complete."
        return "\n\n".join(str(task) for task in incomplete)

def main():
    todo_list = ToDoList()

    while True:
        print("\nToDo List Menu:")
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. List All Tasks")
        print("4. List Incomplete Tasks")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            title = input("Enter task title: ")
            desc = input("Enter task description: ")
            due = input("Enter due date (YYYY-MM-DD): ")
            try:
                task = Task(title, desc, due)
                todo_list.add_task(task)
                print("Task added successfully.")
            except ValueError:
                print("Invalid date format. Use YYYY-MM-DD.")
        elif choice == '2':
            title = input("Enter task title to mark as complete: ")
            print(todo_list.mark_task_complete(title))
        elif choice == '3':
            print("\nAll Tasks:\n")
            print(todo_list.list_all_tasks())
        elif choice == '4':
            print("\nIncomplete Tasks:\n")
            print(todo_list.list_incomplete_tasks())
        elif choice == '5':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please select between 1 and 5.")

if __name__ == "__main__":
    main()

#2Homework 2. Simple Blog System

Define Post Class:
Create a Post class with attributes like title, content, and author.
Define Blog Class:
Create a Blog class that manages a list of posts.
Include methods to add a post, list all posts, and display posts by a specific author.
Create Main Program:
Develop a CLI to interact with the Blog system.
Include options to add posts, list all posts, and display posts by a specific author.
Enhance Blog System:
Add functionality to delete a post, edit a post, and display the latest posts.
Test the Application:
Create instances of posts and test the functionality of your Blog system.


from datetime import datetime

class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author
        self.created_at = datetime.now()

    def edit_content(self, new_content):
        self.content = new_content

    def __str__(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nDate: {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}\nContent: {self.content}\n"

class Blog:
    def __init__(self):
        self.posts = []

    def add_post(self, post):
        self.posts.append(post)

    def list_all_posts(self):
        if not self.posts:
            return "No posts found."
        return "\n\n".join(str(post) for post in self.posts)

    def list_posts_by_author(self, author):
        author_posts = [post for post in self.posts if post.author.lower() == author.lower()]
        if not author_posts:
            return f"No posts found by {author}."
        return "\n\n".join(str(post) for post in author_posts)

    def delete_post(self, title):
        for post in self.posts:
            if post.title.lower() == title.lower():
                self.posts.remove(post)
                return f"Post '{title}' has been deleted."
        return f"Post '{title}' not found."

    def edit_post(self, title, new_content):
        for post in self.posts:
            if post.title.lower() == title.lower():
                post.edit_content(new_content)
                return f"Post '{title}' has been edited."
        return f"Post '{title}' not found."

    def list_latest_posts(self, n=5):
        sorted_posts = sorted(self.posts, key=lambda post: post.created_at, reverse=True)
        latest_posts = sorted_posts[:n]
        if not latest_posts:
            return "No posts available."
        return "\n\n".join(str(post) for post in latest_posts)

def main():
    blog = Blog()

    while True:
        print("\nBlog Menu:")
        print("1. Add Post")
        print("2. List All Posts")
        print("3. List Posts by Author")
        print("4. Delete Post")
        print("5. Edit Post")
        print("6. List Latest Posts")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            title = input("Enter post title: ")
            content = input("Enter post content: ")
            author = input("Enter author name: ")
            post = Post(title, content, author)
            blog.add_post(post)
            print("Post added successfully.")
        elif choice == '2':
            print("\nAll Posts:\n")
            print(blog.list_all_posts())
        elif choice == '3':
            author = input("Enter author name to filter by: ")
            print("\nPosts by Author:\n")
            print(blog.list_posts_by_author(author))
        elif choice == '4':
            title = input("Enter post title to delete: ")
            print(blog.delete_post(title))
        elif choice == '5':
            title = input("Enter post title to edit: ")
            new_content = input("Enter new content: ")
            print(blog.edit_post(title, new_content))
        elif choice == '6':
            n = input("Enter number of latest posts to display: ")
            try:
                print("\nLatest Posts:\n")
                print(blog.list_latest_posts(int(n)))
            except ValueError:
                print("Invalid number. Please enter an integer.")
        elif choice == '7':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please select between 1 and 7.")

if __name__ == "__main__":
    main()


#3.Homework 3. Simple Banking System

Define Account Class:
Create an Account class with attributes like account number, account holder name, and balance.
Define Bank Class:
Create a Bank class that manages a list of accounts.
Include methods to add an account, check balance, deposit money, and withdraw money.
Create Main Program:
Develop a CLI to interact with the Banking system.
Include options to add accounts, check balance, deposit money, and withdraw money.
Enhance Banking System:
Add functionality to transfer money between accounts, display account details, and handle account overdrafts.
Test the Application:
Create instances of accounts and test the functionality of your Banking system.


class Account:
    def __init__(self, account_number, holder_name, initial_balance=0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited ${amount}. New balance: ${self.balance}."
        else:
            return "Deposit amount must be greater than zero."

    def withdraw(self, amount):
        if amount <= 0:
            return "Withdrawal amount must be greater than zero."
        elif amount > self.balance:
            return "Insufficient funds for this withdrawal."
        else:
            self.balance -= amount
            return f"Withdrew ${amount}. New balance: ${self.balance}."

    def get_balance(self):
        return f"Account balance: ${self.balance}"

    def __str__(self):
        return f"Account Number: {self.account_number}\nAccount Holder: {self.holder_name}\nBalance: ${self.balance}"

class Bank:
    def __init__(self):
        self.accounts = {}

    def add_account(self, account):
        if account.account_number in self.accounts:
            return f"Account with number {account.account_number} already exists."
        self.accounts[account.account_number] = account
        return f"Account for {account.holder_name} added successfully."

    def get_account(self, account_number):
        return self.accounts.get(account_number, None)

    def transfer(self, from_account_number, to_account_number, amount):
        from_account = self.get_account(from_account_number)
        to_account = self.get_account(to_account_number)

        if not from_account:
            return f"Account {from_account_number} not found."
        if not to_account:
            return f"Account {to_account_number} not found."
        if amount <= 0:
            return "Transfer amount must be greater than zero."
        if from_account.balance < amount:
            return "Insufficient funds for transfer."
        
        from_account.withdraw(amount)
        to_account.deposit(amount)
        return f"Transferred ${amount} from account {from_account_number} to account {to_account_number}."

def main():
    bank = Bank()

    while True:
        print("\nBanking System Menu:")
        print("1. Add Account")
        print("2. Check Account Balance")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. Transfer Money")
        print("6. Display Account Details")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            account_number = input("Enter account number: ")
            holder_name = input("Enter account holder's name: ")
            initial_balance = float(input("Enter initial balance (default is 0): ") or 0)
            account = Account(account_number, holder_name, initial_balance)
            print(bank.add_account(account))

        elif choice == '2':
            account_number = input("Enter account number to check balance: ")
            account = bank.get_account(account_number)
            if account:
                print(account.get_balance())
            else:
                print(f"Account {account_number} not found.")

        elif choice == '3':
            account_number = input("Enter account number to deposit money into: ")
            amount = float(input("Enter deposit amount: "))
            account = bank.get_account(account_number)
            if account:
                print(account.deposit(amount))
            else:
                print(f"Account {account_number} not found.")

        elif choice == '4':
            account_number = input("Enter account number to withdraw from: ")
            amount = float(input("Enter withdrawal amount: "))
            account = bank.get_account(account_number)
            if account:
                print(account.withdraw(amount))
            else:
                print(f"Account {account_number} not found.")

        elif choice == '5':
            from_account_number = input("Enter source account number: ")
            to_account_number = input("Enter destination account number: ")
            amount = float(input("Enter transfer amount: "))
            print(bank.transfer(from_account_number, to_account_number, amount))

        elif choice == '6':
            account_number = input("Enter account number to view details: ")
            account = bank.get_account(account_number)
            if account:
                print(account)
            else:
                print(f"Account {account_number} not found.")

        elif choice == '7':
            print("Exiting... Goodbye!")
            break

        else:
            print("Invalid choice. Please select between 1 and 7.")

if __name__ == "__main__":
    main()
