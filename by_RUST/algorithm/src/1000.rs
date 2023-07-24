use std::io::{stdin, Read};

fn main() {
	let mut input = ::new();
    stdin().read_line(&mut input).unwrap();
    println!("{}??!",input.trim())
}