# Day 1: Study status manager

# Creating variables to save the info about the user study status, using input to make the questions
subject_studied = input("Which's the studied subject? ")
progress_percent = input("What's the progress percent? ")
next_task = input("What's the next task? ")

# open the file, if not found, create a new one ("a" or "w")
with open("my_progress.txt", "a") as file:
    # put the info inside the file, not forgetting "f" (f-string) for python to understand there is variables, not just texts
    file.write(f"subject:{subject_studied}, progress:{progress_percent}%, Next task:{next_task}\n")
    # Don't forget the /n (escape character) or the last information (next_task) and the last text of the terminal will be on the same line