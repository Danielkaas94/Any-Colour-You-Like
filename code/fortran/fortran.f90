program hello
    print *, 'Hello, World!'
end program hello




program arithmetic
    integer :: a, b, sum
    a = 3
    b = 5
    sum = a + b
    print *, 'The sum of', a, 'and', b, 'is', sum
end program arithmetic




program factorial
    integer :: n, i, fact
    fact = 1
    n = 5
    do i = 1, n
        fact = fact * i
    end do
    print *, 'Factorial of', n, 'is', fact
end program factorial




program array_operation
    real :: numbers(3)
    integer :: i
    
    numbers = [1.0, 2.0, 3.0]
    
    do i = 1, 3
        numbers(i) = numbers(i) ** 2
    end do
    
    print *, 'Squared numbers:', numbers
end program array_operation




program newton_raphson
    real :: x0, f, df, tolerance
    real :: x_new, x_old
    
    ! Initial guess
    x_old = 1.0
    
    ! Tolerance for convergence
    tolerance = 1.0E-6
    
    do
        ! Evaluate function and its derivative
        f = x_old**2 - 2
        df = 2 * x_old
        
        ! Update using Newton-Raphson formula
        x_new = x_old - f / df
        
        ! Check convergence
        if (abs(x_new - x_old) < tolerance) exit
        
        ! Update old value
        x_old = x_new
    end do
    
    print *, 'Root:', x_new
end program newton_raphson