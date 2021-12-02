use std::fs;
use std::error::Error;
use std::vec::Vec;

fn main() -> Result<(), Box<dyn Error>> {
    let contents = fs::read_to_string("inputs/day1_part1")?; 
    let measurements: Vec<i32> = contents.split_whitespace()
        .map(|x| x.parse::<i32>())
        .collect::<Result<Vec<i32>, _>>()?;

    let mut prev = 0;
    let mut inc = -1;

    for x in (&measurements).iter() {
        if *x > prev {
            inc = inc + 1;
        }
        prev = *x;
    }
    println!("total increases = {}", inc);

    prev = 0;
    inc = -1;
    for x in 0 .. (measurements.len() - 2) {
        let sum = measurements[x] + measurements[x+1] + measurements[x+2];
        if sum > prev {
            inc = inc + 1;
        }
        prev = sum;
    }
    println!("sum increases = {}", inc);

    Ok(())
}
