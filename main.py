# From file or module? then the entity
from person import Person
from color import Color, get_warmth

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
  # The "lambda" keyword is basically a "=>" or "->" or even C#'s "delegate" keyword
  persons.sort(key=lambda p : p.age or 0)
  # Display all persons
  for person in persons:
    print(person)

  # Working with enums
  print(get_warmth(Color.BLUE))
  print(get_warmth(Color.RED))
  print(get_warmth(Color.GREEN))
    

# Run Main
if __name__ == "__main__":
  main()