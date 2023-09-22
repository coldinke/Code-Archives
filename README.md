# Code Collection: A Curation of Interesting Snippets

## Introduction

The contents of this repository are organized into classes based on the type of code they contain, such as algorithms, data structures, and utilities.

## Contents

>

### Recursion

1. Print out a cascading tree of a positive integer `n`.

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

2. Count the number of ways to give out `n` pieces of chocolate if nobody can have more than `m` pieces. (n>0 , m >0)

        ```bash
        # count_part(6, 4)
        9
        ```

Code:

```rust
fn count_part(n: i32, m: i32) -> u32 {
    if n == 0 {
        return 1;
    } else if n < 0 {
        return 0;
    } else if m == 0 {
        return 0;
    } else {
        let with_m = count_part(n-m, m);
        let  wo_m = count_part(n, m - 1);
        return with_m + wo_m;
    }
}

fn main() {
    let res = count_part(6,4);
    println!("res: {res}");
}
```

### Computer System

1. YEMU: A Simple CPU simulator

    ```bash
    ./C/yemu.c  # The code is in this file.
    ```