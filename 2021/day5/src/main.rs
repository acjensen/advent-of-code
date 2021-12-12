// use regex::Regex;
// use std::error::Error;
// use std::fs::File;
// use std::io::BufRead;
// use std::io::BufReader;

// fn _solve() {
//     let re = Regex::new(r"(\d),(\d) -> (\d),(\d)").unwrap();
//     let text = std::fs::read_to_string("test_input.txt").unwrap().as_str();
//     for cap in re.captures_iter(text) {
//         println!("Month: {} Day: {} Year: {}", &cap[2], &cap[3], &cap[1]);
//     }
// }

// fn main() {
//     println!("{}", "");
// }

//type str_vec<'a> = Vec<&'a String>;
struct StrVec {
    contents: Vec<String>,
}

fn main() {
    let mut sv: StrVec{};
    let mut v: &mut Vec<&mut String> = &mut Vec::new();
    let mut a: &mut String = &mut String::from("hahahha");
    v.push(a);
    something(v, &String::from("hahaha"));
    println!("{}", v[0]);
}

fn something(v: &mut Vec<&mut String>, text: &String) {
    v[0].push_str(text);
}
