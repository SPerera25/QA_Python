''' Get the user input for hou many seconds and print
how many minutes and hours are in that many seconds '''

sec = int(input("Enter the number of seconds: "))

min = sec / 60
hours = min / 60

print(f"{sec} seconds is equal to {min} minutes or {hours} hours.")
# print(sec, " seconds is equal to ", min, " minutes or ", hours, " hours.")