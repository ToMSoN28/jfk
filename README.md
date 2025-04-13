# jfk
Study project - own compilator

## Done
* initialization int as Number
* initizlization float as double
* initialization bool as bool equation
* overriding virables as equation using virables
* printing to screen (also equation)
* short-circiut boolean evaluation
* Makefile - make to compile and run code from code.txt
* writing from screan (float)
* Static text analysis on compilation level
* if anf if_else statemant
* while loop
* declaration of function that returns value (int, float, bool)

## TODO
list,
matrix,
string,
structures,
loop over list

## Working code
```
func int max (int a, int b) {
    int i = 0;
    if a > b {
        while i < a {
            print(i*a);
            i = i+1;
        }
        return a;
    } else {
        while i < b {
            print(i*b);
            i = i+1;
        }
        return b;
    }
}
int res = 0;
res = max(5, 10);
print(res);
```
