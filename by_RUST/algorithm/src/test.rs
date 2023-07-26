use std::io;

fn main(){
    let mut n = String::new();
    io::stdin().read_line(&mut n).unwrap();
    let n :i32 = n.trim().parse().unwrap();
    for i in 0..n{
        for j in 0..=i{
            print!("*")
        }
        print!("\n")
    }
}