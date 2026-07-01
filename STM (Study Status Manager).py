# Day 1: Study Status Manager

# Creating variables to save the study status info, using input to prompt questions
subject_studied = input("Which is the studied subject? ")
progress_percent = input("What is the progress percentage? ")
next_task = input("What is the next task? ")

# Open the file; if it does not exist, create a new one ("a" for append)
with open("my_progress.txt", "a") as file:
    # Write the info inside the file using an f-string so Python recognizes the variables
    file.write(f"Subject: {subject_studied}, Progress: {progress_percent}%, Next task: {next_task}\n")
    # Don't forget the \n (escape character), otherwise the next entry will be appended on the same line
