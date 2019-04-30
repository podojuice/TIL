// function makeCoffee(order) {
//     let cup;
//
//     // 컵을 커피 기계 밑에 두기.
//     setTimeout(() => {
//         cup = order;
//     }, 2000);
//
//     return cup;
// }
//
// const myCoffee = makeCoffee('latte');
//
// console.log(myCoffee);

// 이 코드를 내가 원하는 대로 돌게 하려면,

function makeCoffee(order, serve) {
    let cup;

    // 컵을 커피 기계 밑에 두기.
    setTimeout(() => {
        cup = order;
        serve(cup)
    }, 2000);

}

makeCoffee('latte', console.log);
