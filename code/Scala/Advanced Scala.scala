import scala.concurrent.*
import scala.concurrent.ExecutionContext.Implicits.global
import scala.util.*

def add(x: Int, y: Int): Int = x + y
def multiply(x: Int, y: Int): Int = x * y

def operate(a: Int, b: Int, f: (Int, Int) => Int): Int =
  f(a, b)

println(operate(4, 5, add))      // 9
println(operate(4, 5, multiply)) // 20


val future1 = Future { 40 }
val future2 = Future { 2 }

val combined = for
  x <- future1
  y <- future2
yield x + y

combined.onComplete {
  case Success(value) => println(s"Result: $value")
  case Failure(e) => println(s"Error: ${e.getMessage}")
}

// Wait for the future to complete (only for demo)
Thread.sleep(1000)


sealed trait Shape
case class Circle(radius: Double) extends Shape
case class Rectangle(width: Double, height: Double) extends Shape

def area(shape: Shape): Double = shape match
  case Circle(r) => Math.PI * r * r
  case Rectangle(w, h) => w * h

val shapes: List[Shape] = List(Circle(3), Rectangle(4, 5))
shapes.foreach(s => println(area(s)))

trait Show[T]:
  def show(value: T): String

given Show[Int] with
  def show(value: Int) = s"Int($value)"

given Show[String] with
  def show(value: String) = s"String('$value')"

def printShow[T](value: T)(using s: Show[T]) =
  println(s.show(value))

printShow(42)
printShow("Hello")
