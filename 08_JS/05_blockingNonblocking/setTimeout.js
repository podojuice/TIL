function sleep_3s() {
    setTimeout(() => {
        console.log('Wake up!')
    }, 3000)
}

console.log('start sleeping');
sleep_3s();
console.log('end');
// non 블로킹함.

// const logEnd = () => {
//     console.log('END')
// };
//
// setTimeout(logEnd, 3000);
// console.log('s');