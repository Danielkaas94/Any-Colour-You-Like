section .data
    msg db 'Hello, world!', 0

section .text
    global _start

_start:
    ; write message to stdout
    mov edx, 13  ; message length
    mov ecx, msg ; message to write
    mov ebx, 1   ; file descriptor (stdout)
    mov eax, 4   ; system call number for sys_write
    int 0x80     ; call kernel

    ; exit program
    mov eax, 1   ; system call number for sys_exit
    xor ebx, ebx ; exit code 0
    int 0x80     ; call kernel




section .data
    num1 dd 10     ; first number (integer)
    num2 dd 20     ; second number (integer)
    result dd 0    ; result variable

section .text
    global _start

_start:
    ; load num1 into eax
    mov eax, [num1]
    ; add num2 to eax
    add eax, [num2]
    ; store result in result variable
    mov [result], eax

    ; exit program
    mov eax, 1   ; system call number for sys_exit
    xor ebx, ebx ; exit code 0
    int 0x80     ; call kernel





section .data
    array dd 1, 2, 3, 4, 5  ; array of integers
    array_len equ ($ - array) / 4  ; calculate array length

section .text
    global _start

_start:
    ; initialize loop counter
    mov esi, 0

loop_start:
    ; check if loop counter is equal to array length
    cmp esi, array_len
    je loop_end

    ; access array element at index esi
    mov eax, dword [array + esi*4]

    ; perform some operation with the array element
    ; for example, print it
    ; (code for printing omitted for brevity)

    ; increment loop counter
    inc esi

    ; jump back to loop_start
    jmp loop_start

loop_end:
    ; exit program
    mov eax, 1   ; system call number for sys_exit
    xor ebx, ebx ; exit code 0
    int 0x80     ; call kernel
