def linear_search(student_ids, target_id):
  # Define a linear search function that scans `student_ids` for `target_id`.
  comparisons = 0  # Initialize counter for number of comparisons done.
  for i in range(len(student_ids)):
    # Loop over indices from 0 to length-1 to examine each element.
    comparisons += 1  # Increment comparison count for this element check.
    if student_ids[i] == target_id:
      # If current element equals target, return 1-based position and comparisons.
      return i + 1, comparisons

  # If loop finishes without finding target, return -1 (not found) and comparisons.
  return -1, comparisons


# Hardcoded list of 20 student IDs (integers) from 301 to 320 inclusive.
student_ids = list(range(301, 321))  # Creates [301, 302, ..., 320]


def main():
    # A simple linear-search demo function that prints IDs and asks for input.
    print("STUDENT ID LINEAR SEARCH") 
    print("=" * 50)  # Separator line made of 50 equals signs.

    # Show the available IDs to the user.
    print("\nAvailable Student IDs:")
    for sid in student_ids:
        # Print each student ID on the same line separated by two spaces.
        print(sid, end="  ")
    print("\n" + "=" * 50)  # Newline then another separator.

    # read the target ID from user input as text (note: not converted to int here).
    target = input("\nEnter the Student ID to search for: ").strip()

    # Call the linear search function (this will compare values; types should match).
    position = linear_search(student_ids, target)

    # Output the result to the user and point the position when found.
    print("\n" + "-" * 50)
    if position != -1:
        # If position isn't -1, the function returned a found position.
        print(f"✓ Student ID '{target}' FOUND at position {position}")
    else:
        # Position -1 means not found.
        print(f"✗ Student ID '{target}' NOT FOUND")
    print("-" * 50)


def binary_search(arr, targetVal):
  # Standard iterative binary search on a sorted list `arr` for `targetVal`.
  left = 0  # Left boundary index.
  right = len(arr) - 1  # Right boundary index.
  comparisons = 0  # Counter for comparisons made.

  while left <= right:
    # Continue while there is a valid range to search.
    mid = (left + right) // 2  # Middle index (floor division).
    comparisons += 1  # Count the comparison with arr[mid].

    if arr[mid] == targetVal:
      # Found the value at mid; return 1-based position and comparisons.
      return mid + 1, comparisons

    if arr[mid] < targetVal:
      # Target is in upper half; move left boundary right of mid.
      left = mid + 1
    else:
      # Target is in lower half; move right boundary left of mid.
      right = mid - 1

  # Not found: return -1 and the number of comparisons performed.
  return -1, comparisons


# Sample sorted scores for binary search (must be sorted for binary search to work).
scores = [40, 43, 45, 52, 55, 58, 63, 65, 67, 72, 75, 77, 78, 82, 85, 88, 90, 92, 95, 98]


def searching_menu():
  """Interactive menu for choosing search operations."""
  while True:
    # Print the menu options for the user.
    print("\n=== Searching Algorithms Menu ===")
    print("\nSelect a search operation (1-3):")
    print("1. Linear Search - Find Student ID")
    print("2. Binary Search - Find Score")
    print("3. Exit program")

    choice = input("\nEnter your choice: ").strip()  # Read user's menu choice.

    if choice == '1':
      # Linear search branch: show list and ask for the student ID to search.
      print(f"Searching in the list: {student_ids}")
      raw = input("Enter Student ID to search: ").strip()
      try:
        # Convert the input string to integer; binary/linear functions expect numbers.
        target = int(raw)
      except ValueError:
        # If conversion fails, inform the user and skip this iteration.
        print("Please enter a numeric Student ID.")
        continue

      # Call linear_search, receive position and comparisons.
      pos, comps = linear_search(student_ids, target)
      if pos != -1:
        # Print found message with position and comparisons.
        print(f"Result: Student ID {target} found at position {pos} Comparisons made: {comps}")
      else:
        # Print not-found message with comparisons.
        print(f"Result: Student ID {target} not found. Comparisons made: {comps}")

    elif choice == '2':
      # Binary search branch: show sorted scores and ask for a score to search.
      print(f"Sorted scores: {scores}")
      raw = input("Enter score to search: ").strip()
      try:
        # Convert the string input to integer for searching.
        target = int(raw)
      except ValueError:
        # If conversion fails, tell the user and continue the menu loop.
        print("Please enter a numeric score.")
        continue

      # Call binary_search with the `scores` list and the target.
      pos, comps = binary_search(scores, target)
      if pos != -1:
        # Found: print position and comparisons count.
        print(f"Result: Score {target} found at position {pos} Comparisons made: {comps}")
      else:
        # Not found: print not-found with comparisons.
        print(f"Result: Score {target} not found. Comparisons made: {comps}")

    elif choice == '3':
      # Exit choice: thank the user and break the menu loop.
      print("\nThank you for using the search program!")
      break

    else:
      # Invalid menu input: inform user and let loop repeat.
      print("Invalid choice. Please enter 1, 2, or 3.")

    # Ask if user wants another search; if they say anything other than 'y', exit.
    again = input("Would you like to perform another search? (y/n): ").strip().lower()
    if again != 'y':
      print("\nThank you for using the search program!")
      break


if __name__ == "__main__":
  searching_menu()