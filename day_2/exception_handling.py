# Finally we look at exception handling
#  Exceptions are runtime errors that happen
#  when a programme runs into unexpected circumstances
# such as dividing by 0 or attempting to access a list
# element that does not exist
# use try/except block to manage exceptions in Py3.

# The try block code runs
try:
    f = open("90DaysOfDevOps.txt", "r")
    try:
        f.write("Python is great!")
    # the except block code runs to handle the exception.
    except:
        print("Something went wrong when writing to the file.")
finally:
    print("Idk brev")