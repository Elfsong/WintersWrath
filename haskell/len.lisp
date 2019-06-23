(define (len list)
    (if (null? list)
        0
        (+ 1 (len (cdr list)))))
(define x '(a "b" 42))
x
(len x)
