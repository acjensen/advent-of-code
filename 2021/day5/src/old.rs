use std::error::Error;
use std::fs::File;
use std::io::BufRead;
use std::io::BufReader;
use std::collections::HashSet;
use std::hash::Hasher
// use regex::Regex;

struct Point {
    x: u64,
    y: u64,
}

// impl std::cmp::Eq for Point {
//     fn summarize(&self) -> String {
//         format!("{}, by {} ({})", self.headline, self.author, self.location)
//     }
// }


fn _solve(file: &mut std::fs::File, linesize: usize) -> Result<u64, Box<dyn Error>> {
    
    let mut hset = HashSet::new();
    // let re = Regex::new(r"(\d),(\d) -> (\d),(\d)").unwrap();
    for line in BufReader::new(file).lines() {
        let l = line?.parse::<String>()?;
        let pairs = l.split(" -> ");
        let mut v: Vec<Vec<_>> = Vec::new();
        for p in pairs {
            v.push(p.split(",").map(|p| p.parse::<u64>().unwrap()).collect());
        }
        println!("{}", v[0].len());
        println!("{}", v.len());

        let p1 = 0; let p2 = 1; let x = 0; let y = 1;
        for x_point in v[p1][x]..v[p2][x]{
            let p = Point{x: x_point, y: v[p1][y]};
            if hset.contains() {
                hset.insert(p);
            }
        }

        for x in v[p1][y]..v[p2][y]{

        }

        // let res = pairs
        //     .map(|p| p.split(",")
        //     .map(|x| x.parse::<u64>().unwrap())
        // );
        // let tmp = res.map(|p| p.collect::<String>());
        // let new = res.map(|p| p.collect::<String>().parse::<u64>().unwrap());
        // let one: Vec<_> = new.collect();
        // let collected: Vec<_> = res.collect();
        // println!("{}", collected[0])
        // let c = re.captures(&l).unwrap();
        // println!("{}", c.get(0).unwrap().as_str());
    }
    
    Ok(8)
}

fn main() {
    let mut arr: [u16; 9] = [0; 9];
    let f = &mut std::fs::File::open("test_input.txt").unwrap();
    let err = _solve(f, 9);

    println!("{}", "test");
}