# https://www.youtube.com/watch?v=8wZ2ZD--VTk&ab_channel=MikeDane - 11:39

=begin
    Names are case-sensitive
    Who codes in Ruby 💎?
=end


puts "Hello"
print "World"
puts "!"


name = "Daniel"
age = 27
gpa = 3.5
is_tall = true

puts "Your name is #{name}"
puts "Your name is " + name



# CASTING & CONVERTING

puts 3.14.to_i
puts 3.to_f
puts 3.0.to_s

puts 100 + "50".to_i
puts 100 + "50.99".to_f


# STRINGS


greeting = "Hello"
#indexes:   01234

puts greeting.length
puts greeting[0]
puts greeting.include? "llo"
puts greeting.include? "z"
puts greeting[1,3]



# NUMBERS

puts 2 * 3          # Basic arithmetic: +, -, /, *
puts 2**3           # Exponent
puts 10 % 3         # Modulus Op. : returns remainder of 10/3
puts (1 + 2) * 3      # Order of Operations
puts 10 / 3.0       # int's and doubles


num = 10
num += 100
puts num

num = -36.8
puts num.abs()
puts num.round()

# Math class has useful math methods
puts Math.sqrt(144)
puts Math.log(0)



# USER INPUT
puts  "Enter your name: "
name = gets
puts  "Hello #{name}, how are you?"

puts "Enter first num: "
num1 = gets.chomp
puts "Enter second num: "
num2 = gets.chomp
puts num1.to_f + num2.to_f