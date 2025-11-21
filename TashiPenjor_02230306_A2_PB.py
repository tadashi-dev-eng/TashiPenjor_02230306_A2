student_names = [
  "Tashi", "Pejor", "Sonam", "Dawa", "Karma", "Pema", "Choden",
  "Dorji", "Sangay", "Tshering", "Jigme", "Wangchuk", "Namgay",
  "Lhamo", "Tobgay", "Phuntsho", "Ugyen", "Yeshey", "Dorji", "Chimi",
]

test_scores = [88, 45, 92, 55, 72, 40, 78, 65, 95, 52, 82, 67, 43, 90, 77, 58, 98, 63, 75, 85]

book_prices = [500, 150, 650, 555, 330, 110, 950, 120, 450, 650, 100, 120, 350, 750, 300]


def bubble_sort(arr):
  """Return a sorted copy of arr using bubble sort (ascending)."""
  a = arr.copy()
  n = len(a)
  for i in range(n - 1):
    for j in range(n - i - 1):
      if a[j] > a[j + 1]:
        a[j], a[j + 1] = a[j + 1], a[j]
  return a


def insertion_sort(arr):
  """Return a sorted copy of arr using insertion sort (ascending)."""
  a = arr.copy()
  for i in range(1, len(a)):
    key = a[i]
    j = i - 1
    while j >= 0 and a[j] > key:
      a[j + 1] = a[j]
      j -= 1
    a[j + 1] = key
  return a


def partition(array, low, high):
  pivot = array[high]
  i = low - 1
  for j in range(low, high):
    if array[j] <= pivot:
      i += 1
      array[i], array[j] = array[j], array[i]
  array[i + 1], array[high] = array[high], array[i + 1]
  return i + 1


def quicksort_inplace(array, low=0, high=None):
  """In-place quicksort. Helper used by quick_sort_copy."""
  if high is None:
    high = len(array) - 1
  if low < high:
    pivot_index = partition(array, low, high)
    quicksort_inplace(array, low, pivot_index - 1)
    quicksort_inplace(array, pivot_index + 1, high)


def quick_sort_copy(arr):
  """Return a sorted copy of arr using quick sort (ascending)."""
  a = arr.copy()
  quicksort_inplace(a)
  return a


def show_original_and_sorted(original, sorted_list):
  print("Original:", original)
  print("Sorted:", sorted_list)
  print()


def print_menu():
  print("=== Sorting Algorithms Menu ===")
  print("Select a sorting operation (1-4):")
  print("1. Bubble Sort - Sort Student Names")
  print("2. Insertion Sort - Sort Test Scores")
  print("3. Quick Sort - Sort Book Prices")
  print("4. Exit program")


def main():
  while True:
    print_menu()
    choice = input("Enter your choice: ").strip()
    if choice == "1":
      print("\nBubble Sort - Sort Student Names")
      sorted_names = bubble_sort(student_names)
      show_original_and_sorted(student_names, sorted_names)
    elif choice == "2":
      print("\nInsertion Sort - Sort Test Scores")
      sorted_scores = insertion_sort(test_scores)
      show_original_and_sorted(test_scores, sorted_scores)
    elif choice == "3":
      print("\nQuick Sort - Sort Book Prices")
      sorted_prices = quick_sort_copy(book_prices)
      show_original_and_sorted(book_prices, sorted_prices)
    elif choice == "4":
      print("Thank you for using the sorting program!")
      break
    else:
      print("Invalid choice. Please enter a number from 1 to 4.\n")
      continue

    again = input("Would you like to perform another sort? (y/n): ").strip().lower()
    while again not in {"y", "n"}:
      again = input("Please enter 'y' or 'n': ").strip().lower()
    if again == "n":
      print("Thank you for using the sorting program!")
      break


if __name__ == "__main__":
  main()
