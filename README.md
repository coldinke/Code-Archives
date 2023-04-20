# Code Collection: A Curation of Interesting Snippets

## Introduction
The contents of this repository are organized into classes based on the type of code they contain, such as algorithms, data structures, and utilities.

## Contents
> 
### 1. Recursion
output the number like this:
```bash
486
48
4
48
486
```
Code: 
```rust
fn cascade(n: u32) {
    if n < 10 {
        println!("{n}");
    } else {
        println!("{n}");
        sum_digits(n / 10);
        println!("{n}");
    }
}

fn main() {
    cascade(486);
}
```