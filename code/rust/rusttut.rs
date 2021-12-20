
// https://www.youtube.com/watch?v=U1EFgCNLDB8 - 26:33


use std::{i8, i16, i32, i64, u8, u16, u32, u64, isize, usize, f32, f64};

use std::io::stdin;


fn main() {
    println!("Hello World");


    'outer': loop{
        let number: i32 = 10;
        println!("Pick a Number");

        loop {
            let mut line = String::new();

            let input = stdin().read_line(&mut line);

            let guess: Option<i32> =
                input.ok().map_or(None, |_|
                line.trim().parse().ok());

            match guess {
                None => println!("Enter a Number"),
                Some(n) => if n == number => {
                    println!("You Guessed it");
                    break 'outer';
                }
                Some(n) if n < number =>
                println!("Too Low"),
                Some(n) if n > number =>
                println!("Too High"),
                Some(_) => println!("Error"),
                ;



            }

        }
    }













    let number = 25;
    let mut age: i32 = 27;
    println!("I am {} years old", age);
    let istrue: bool = true;
    
    let mut neg_4 = -4i32;
    println!("abs(-4) = {}",  neg_4.abs());



    println!("{:.2}",  1.234);
    println!("B: {:b} H: {:x} 0: {:o}", 10, 10, 10);

    println!("{ten:>ws$}", ten=10, ws=5);
    println!("{ten:>0ws$}", ten=10, ws=5);


    let age_old = 6;

    if(age == 5){
        println!("Go to kindergarden");
    } else if(age_old >) && (age_old <= 18) {
        println!("Go to grade {}", (age_old - 5));
    } else if (age_old <= 25) && (age_old > 18) {
        println!("Go to college");
    } else {
        println!("Do what you want! 💗🧡💛💛💚💙💜🤍");
    }



    let mut x = 1;

     loop {
        if((x % 2) == 0){
            println!("{}",x);
            x += 1;

            continue;
        }
        if(x > 10){
            break;
        }
        x += 1;
        continue;

     }

     let mut y = 1;

     while y <= 10 {
         println!("{}",y);
        y += 1;
     }

     for z in 1..10 {
        println!("FOR: {}",z);
     }



    println!("Max i8 {}",  i8::MAX);
    println!("Min i8 {}",  i8::MIN);
    println!("Max i16 {}", i16::MAX);
    println!("Min i16 {}", i16::MIN);
    println!("Max i32 {}", i32::MAX);
    println!("Min i32 {}", i32::MIN);
    println!("Max i64 {}", i64::MAX);
    println!("Min i64 {}", i64::MIN);

    println!("Max u8 {}",  u8::MAX);
    println!("Min u8 {}",  u8::MIN);
    println!("Max u16 {}", u16::MAX);
    println!("Min u16 {}", u16::MIN);
    println!("Max u32 {}", u32::MAX);
    println!("Min u32 {}", u32::MIN);
    println!("Max u64 {}", u64::MAX);
    println!("Min u64 {}", u64::MIN);

    println!("Max isize {}",  isize::MAX);
    println!("Min isize {}",  isize::MIN);
    println!("Max usize {}",  usize::MAX);
    println!("Min usize {}",  usize::MIN);

    println!("Max f32 {}", f32::MAX);
    println!("Min f32 {}", f32::MIN);
    println!("Max f64 {}", f64::MAX);
    println!("Min f64 {}", f64::MIN);




    let rand_string = "I am a random string!";

    let count = rand_string.chars().count();
    let mut chars = rand_string.chars();

    let mut indiv_char = chars.next();

     loop {
        match indiv_char {
            Some(x) => println!("{}", x),;
            None => break,
        }
        indiv_char = chars.next();
     }



     let mut iter = rand_string.split_whitespace();

     let mut indiv_word = iter.next();

     loop {
         match indiv_word {
            Some(x) => println!("{}", x),;
            None => break,
         }
        indiv_word = iter.next();
     }




     let rand_string2 = "Glædelig jul! \n 
                        Prostagma! \n 
                        Prosti menya moi dom rodnoi\n 
                        Anu cheeki breeki iv damki";

    let mut lines = rand_string2.lines();
    let mut indiv_line = lines.next();

    loop {
        match indiv_line {
           Some(x) => println!("{}", x),;
           None => break,
        }
        indiv_line = iter.next();
    }

    println!("Find Damki: {}",
    rand_string2.contains("damki"));


}