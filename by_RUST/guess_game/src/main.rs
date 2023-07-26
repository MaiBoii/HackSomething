extern crate rand;

use std::io;
use std::cmp::Ordering;
use rand::Rng;

fn main() {
    println!("새끼... 기열!\n어디서 해병이 되어서 그런 흘러빠진 소리를 하느냐!\n랜덤으로 숫자를 맞추면 수육형만은 면하게 해주겠다!");

    let secret_num = rand::thread_rng().gen_range(69,75);
    println!("비밀번호는 {}입니다.",secret_num);
    loop {
        println!("시간이 없다 아쎄이! 어서 숫자를 입력해라!: ");
        let mut guess = String::new();
        io::stdin().read_line(&mut guess).expect("불러오는데 실패해부러쓰");
        let guess : i32 = guess.trim().parse().expect("아쎄이! 숫자를 입력해라!");

        println!("아쎄이: 악! 제가 예상한 값이 {}라는 것을 확인 받는 것에 승인을 요구하는 것에 대하여 여쭤봐도 되겠습니까!", guess);

        match guess.cmp(&secret_num){
            Ordering::Less => println!("새끼... 미만!! 즉시 수육으로 만들어 주겠다!"),
            Ordering::Greater=> println!("새끼... 초과!! 즉시 전우애인 형에 처하겠다!"),
            Ordering::Equal=>{
                println!("새끼... 기합!!\n그 아쎄이는 즉시 선임의 생각을 읽은 죄를 물어 수육형에 처했으나 아무렴 뭐 어떠랴!\n오도해병은 늘 앞을 지향하는 법이다!");
                break;
                }
            }
        }
}
