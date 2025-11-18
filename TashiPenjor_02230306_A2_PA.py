def linear_search(student_ids, target_id):

    # Iterate over indices so we can return a 1-indexed position
    for i in range(len(student_ids)):
        if student_ids[i] == target_id:
            # return position with the index
            return i + 1

    # return index not found
    return -1


# Hardcoded list of 20 student IDs
student_ids = [
    "301", "302", "303", "304", "305",
    "306", "307", "308", "309", "310",
    "311", "312", "313", "314", "315",
    "316", "317", "318", "319", "320"
]

def main():
    print("STUDENT ID LINEAR SEARCH")
    print("=" * 50)

    # Show the available IDs to the user.
    print("\nAvailable Student IDs:")
    for sid in student_ids:
        print(sid, end="  ")
    print("\n" + "=" * 50)

    # read the target ID 
    target = input("\nEnter the Student ID to search for: ").strip()

    # Call the linear search function
    position = linear_search(student_ids, target)

    # Output the result to the user and point the position when found.
    print("\n" + "-" * 50)
    if position != -1:
        print(f"✓ Student ID '{target}' FOUND at position {position}")
    else:
        print(f"✗ Student ID '{target}' NOT FOUND")
    print("-" * 50)


# Run the program
if __name__ == "__main__":
    main()