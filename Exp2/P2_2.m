fun1 = @(x) x^3-2*x+2;
fun2 = @(x)(-x^3+5*x);
fzero(fun1, 0)
fzero(fun2, 1.35)