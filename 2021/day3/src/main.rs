use std::error::Error;
use std::fs::File;
use std::io::BufRead;
use std::io::BufReader;

fn _solve(file: &mut std::fs::File, linesize: usize) -> Result<u64, Box<dyn Error>> {
    
    let mut arr = vec![0; linesize];
    for line in BufReader::new(file).lines() {
        let l = line?.parse::<String>()?;
        let c: Vec<_> = l.chars().collect();
        for x in 0..linesize {
            if c[x] == '0' {
                arr[x] -= 1;
            } else {
                arr[x] += 1;
            }
        }
    }

    let base: u64 = 2;
    let mut gamma: u64 = 0;
    let mut epsilon: u64 = 0;
    let mut exponent: usize;

    for x in 0..linesize {
        exponent = linesize - 1 - x;
        let decimal = base.pow(exponent.try_into().unwrap());
        if arr[x] > 0 { // Most common bit was 1.
            gamma += decimal;
        } else { // Most common bit was 0.
            epsilon += decimal;
        }
    }

    Ok(gamma*epsilon)
}

#[test]
fn test() {
    let f = &mut File::open("src/test_input.txt").unwrap();
    let result = _solve(f, 5);
    assert_eq!(result.unwrap(), 198);
}

fn main() {
    let f = &mut File::open("src/input.txt").unwrap();
    let result = _solve(f, 12);
    println!("{}", result.unwrap());
}
