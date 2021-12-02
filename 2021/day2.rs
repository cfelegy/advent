use std::fs;
use std::error::Error;

fn main() -> Result<(), Box<dyn Error>> {
    let contents = fs::read_to_string("inputs/day2")?;
    let commands: Vec<(&str, i32)> = contents
        .split_whitespace()
        .collect::<Vec<&str>>()
        .chunks(2)
        .map(|chunk| {
            let parsed_int = chunk[1].parse::<i32>();
            match parsed_int {
                Ok(int) => Ok((chunk[0], int)),
                Err(e) => Err(e)
            }
        })
        .collect::<Result<Vec<(&str, i32)>, _>>()?;

    let mut depth = 0;
    let mut hzpos = 0;

    for cmd in commands.iter() {
        let arg = (*cmd).1;
        match (*cmd).0 {
            "forward" => {
                hzpos = hzpos + arg;
            },
            "down" => {
                depth = depth + arg;
            },
            "up" => {
                depth = depth - arg;
            },
            _ => {}
        }
    }
    println!("part 1 calculation =>");
    println!("depth*hzpos = {}", depth*hzpos);
    println!();

    let mut depth = 0;
    let mut hzpos = 0;
    let mut aim = 0;

    for cmd in commands.iter() {
        let arg = (*cmd).1;
        match (*cmd).0 {
            "forward" => {
                hzpos = hzpos + arg;
                depth = depth + (aim * arg);
            },
            "down" => {
                aim = aim + arg;
            },
            "up" => {
                aim = aim - arg;
            },
            _ => {}
        }
    }
    println!("part 2 calculation =>");
    println!("depth*hzpos = {}", depth*hzpos);

    Ok(())
}
