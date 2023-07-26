use std::io;

fn main(){
    let mut score = String::new();
    io::stdin().read_line(&mut score).expect("똑바로 넣어라 자식아");
    let score : i32 = score.trim().parse().expect("숫자 입력");
    if score >= 90{
        println!("A")
    }else if score >= 80 {
        println!("B")
    }else if score >= 70 {
        println!("C")
    }else if score >= 60 {
        println!("D")
    }else {
        println!("F")
    }
}