def modify_file(old_file, new_file):
    try:
        # Read from the old file
        with open(old_file, "r") as file:
            content = file.read()

        # Modify the content (example: convert to uppercase)
        modified_content = content.upper()

        # Write to the new file
        with open(new_file, "w") as file:
            file.write(modified_content)

        print(f"✅ File has been successfully modified and saved as '{new_file}'")

    except FileNotFoundError:
        print(f"❌ Error: The file '{old_file}' does not exist.")
    except PermissionError:
        print(f"❌ Error: Permission denied to read/write the file.")
    except Exception as e:
        print(f"⚠️ An unexpected error occurred: {e}")


# --- Main Program ---
if __name__ == "__main__":
    old_file = input("Enter the name of the file to read: ")
    new_file = "modified_" + old_file

    modify_file(old_file, new_file)

