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
* string: declaration, printing, assigning
* table: declaration, assigning whole (must afret dclaration), assiging single value, accesing single value, printing whole table
* loop over list (iterator)
* matrix
  
## TODO
structures,

## Working code
small part for presentation in `presentation_code`

```
string str = "Hello";
print(str);
str = "Word";
print(str);
print("str");

func int max (int a, int b) {
    int [20] table;
    table = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0];
    int i = 0;
    string t = "A jest wiksze od B";
    string n = "B jest wiksze od A";
    if a > b {
        print(t);
        while i < a {
            print(i*a);
            table[i] = i*a;
            i = i+1;
        }
        print(table);
        return a;
    } else {
        print(n);
        while i < b {
            print(i*b);
            table[i] = i*b;
            i = i+1;
        }
        print(table);
        return b;
    }
}
int a = 5;
int b = 7;
int res = 0;
res = max(a, b);
print(res);
```
