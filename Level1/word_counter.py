# Level 1 - Task 3
# Word Counter
# Codveda Python Internship

def word_counter(filename):
    try:
        with open(filename, "r") as file:
            content = file.read()
            words = content.split()
            print(f"Total number of words: {len(words)}")

    except FileNotFoundError:
        print("Error: File not found. Please check the file name.")
    except Exception as e:
        print("An unexpected error occurred:", e)


def main():
    print("===== Word Counter Program =====")
    filename = input("Enter the file name (with extension): ")
    word_counter(filename)

main()
