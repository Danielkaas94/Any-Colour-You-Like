open System
open System.Linq
open System.IO
open System.Numerics

//let changeColor(color)
//    Console.ForegroundColor <- color
//changeColor(ConsoleColor.Blue)
    



// For more information see https://aka.ms/fsharp-console-apps
printfn "Hello from F#"


// https://www.youtube.com/watch?v=c7eNDJN758U 19:45 / 1:24:00

let hello name = 

    Console.ForegroundColor <- ConsoleColor.Red

    printfn "Hej, %s og glædelig jul!" name 

    Console.ResetColor()

Console.ForegroundColor <- ConsoleColor.Yellow


let hello2() =
    printf "Enter your name : "

    let name  = Console.ReadLine()

    //printfn "Hello %s" name
    hello name

    //  %i
    //  %f
    //  %b
    //  %A
    //  %O
   
let myPi() =

    Console.ForegroundColor <- ConsoleColor.Blue
    

    printfn ""

    let big_pi = 3.141592653589793238462643383M
    let big_pi2 = System.Math.PI

    printfn "Big PI : %M" big_pi
    printfn "System.Math PI : %f" big_pi2
    printfn "%-5s %5s" "a" "b"
    printfn "%-5s %5s" "Test1" "Test2"

    printfn "%*s" 10 "Hej"



    printfn "PI : %f" 3.141592653589793238462643383
    printfn "PI : %.4f" 3.141592653589793238462643383


let bind_stuff() =
    let mutable weight = 175
    weight <- 64

    printfn "Vægt : %i" weight

    let change_me  = ref 10
    change_me := 50

    printfn "Change : %i" !change_me


let do_funcs() =
    
    Console.ForegroundColor <- ConsoleColor.Green

    let get_sum (x : int, y : int) : int = x + y

    printfn "5 + 7 = %i" (get_sum(5,7))

let recursive_funcs() =

    Console.ForegroundColor <- ConsoleColor.Magenta

    let rec factorial x =
        if x < 1 then 1
        else x * factorial (x - 1)

    printfn "Factorial 4 : %i" (factorial 4)

let lambda() =

    Console.ForegroundColor <- ConsoleColor.Cyan

    let random_list = [1;2;3]

    let random_list2 = List.map (fun x -> x *2) random_list // coding is fun

    printfn "Original List : %A" random_list
    printfn "Double List : %A" random_list2

    [5;6;7;8]
    |> List.filter (fun v -> (v % 2) = 0)
    |> List.map (fun x -> x * 2)
    |> printfn "Even Doubles : %A"



bind_stuff()

do_funcs()

recursive_funcs()   

lambda()

myPi()
hello2()

Console.ReadKey() |> ignore