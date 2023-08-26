const std = @import("std");

pub fn main() void {
    const message = "Hello, Zig!";
    std.debug.print("Message: {}\n", .{message});

    const num1: i32 = 10;
    const num2: i32 = 20;
    const sum = add(num1, num2);
    std.debug.print("Sum: {}\n", .{sum});

    const array: [5]i32 = [1, 2, 3, 4, 5];
    for (array) |elem| {
        std.debug.print("Element: {}\n", .{elem});
    }
}

pub fn add(a: i32, b: i32) i32 {
    return a + b;
}
