# Write a program that:
# 1.  Reads a file input.txt
# 2.  Writes its content to output.txt line by line
# 3.  If any line is empty, raise a custom error
# 4.  Handle the error and print:
# "Empty line detected"
# 5.  Ensure files are always properly closed
# Constraints:
# Must use with
# Must use try–except–finally
# Must use raise
# No shortcuts

# Solution:

try:
    with open("input.txt", "r") as infile, open("output.txt", "w") as outfile:
        for line in infile:
            stripped = line.rstrip("\n")
            if stripped == "":
                raise ValueError("Empty line in file")
            outfile.write(stripped + "\n")

except ValueError:
    print("Empty line detected")

finally:
    print("File processing completed")