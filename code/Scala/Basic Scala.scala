// A simple "Hello World"
@main def hello(): Unit =
  println("Hello, Scala!")

// Immutable and mutable variables
val name = "Alice"     // immutable
var age = 25           // mutable

// Simple function
def greet(person: String): String =
  s"Hello, $person!"

println(greet(name))

// Control flow
if age < 30 then
  println("You're young!")
else
  println("Experience matters.")

// Working with Lists
val nums = List(1, 2, 3, 4, 5)
val doubled = nums.map(_ * 2)
val evens = nums.filter(_ % 2 == 0)

println(doubled)  // List(2, 4, 6, 8, 10)
println(evens)    // List(2, 4)
