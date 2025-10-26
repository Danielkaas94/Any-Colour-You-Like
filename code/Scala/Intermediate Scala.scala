// Case classes and pattern matching
case class Person(name: String, age: Int)

def describe(person: Person): String = person match
  case Person(_, age) if age < 18 => "Minor"
  case Person(_, age) if age < 65 => "Adult"
  case _ => "Senior"

val people = List(Person("Bob", 15), Person("Alice", 30), Person("John", 70))
people.map(describe).foreach(println)

// Traits and inheritance
trait Animal:
  def speak(): String

class Dog extends Animal:
  def speak() = "Woof!"

class Cat extends Animal:
  def speak() = "Meow!"

val animals: List[Animal] = List(Dog(), Cat())
animals.foreach(a => println(a.speak()))

// Options and safe handling
def findPerson(name: String): Option[Person] =
  people.find(_.name == name)

findPerson("Alice").foreach(p => println(s"Found ${p.name}, age ${p.age}"))
