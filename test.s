main:
    li $t0, 0x7f800000
    li $a0, 0x10000000
    and $t1, $t0, $a0
    srl $t1, $t1, 23
    move $a0, $t1
    li $v0, 1
    syscall
    jr		$ra					# jump to $ra
    