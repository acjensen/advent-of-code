use std::error::Error;
use std::fs::File;
use std::io::BufRead;
use std::io::BufReader;

fn _solve(file: &mut std::fs::File) -> Result<u64, Box<dyn Error>> {
    let mut pos = 0;
    let mut depth = 0;

    for line in BufReader::new(file).lines() {
        let l = line?.parse::<String>()?;
        let pair = l.split_whitespace().collect::<Vec<&str>>();
        let movement = pair[0];
        let amount: u64 = pair[1].parse::<u64>()?;
        if movement == "forward" {
            pos += amount;
        } else if movement == "up" {
            depth -= amount;
        } else if movement == "down" {
            depth += amount;
        }
    }

    Ok(pos * depth)
}

#[test]
fn my_test() {
    let f = &mut File::open("src/input.txt").unwrap();
    let result = _solve(f).unwrap();
    assert_eq!(result, 2147104);
}

fn main() {}