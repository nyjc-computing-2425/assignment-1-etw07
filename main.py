seconds = input('Enter the number of seconds (integer): ')
seconds = int(seconds)

# ... complete the code below
hours = seconds//3600
minutes = (seconds - 3600*hours)//60
seconds = seconds - minutes*60 - hours*3600
# Follow the formatting given
# e.g. The duration is X hours, X minutes, and X seconds.
print("The duration is", hours, "hours,", minutes, "minutes, and", seconds, "seconds.")
