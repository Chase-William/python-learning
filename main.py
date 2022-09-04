from person import Person

# Main Function
def main():
  # Collection of persons
  persons = [
      Person("Rhase Coth", 22),
      Person("Rark Meynolds", 38),
      Person("Host Lope")
    ]
  # Sort using a anonymous function to target age member as key
  # Because age is nullable, we must use the python null-coalescing operator "or"
  persons.sort(key=lambda p : p.age or 0)
  # Display all persons
  for person in persons:
    print(person)
    

# Run Main
if __name__ == "__main__":
  main()