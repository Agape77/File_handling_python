try:
    #File creation
    with open("my_file.txt", "w") as file:
        file.write("Hello world!\n")
        file.write("My name is Camille.\n")
        file.write("I am 21 years old\n")

    #File reading and display
    with open("my_file.txt", "r") as file:
        print("Contents of my_file.txt: ")
        print(file.read())

    #File appending
    with open("my_file.txt", "a") as file:
        file.write("I am a student at PLP Academy, 2024 Cohort.\n")
        file.write("I love reading, travelling and cooking.\n")
        file.write("Ienjoy spending time with family and friends.\n")

except FileNotFoundError:
    print("Error: File not Found.")
except PermissionError:
    print("Error: Permission denied while accessing the file.")
except Exception as e:
    print("Error:", e) 

finally:
    print("Execution completed.")                           