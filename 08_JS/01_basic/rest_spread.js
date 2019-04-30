// rest operator가 없다면..

function addAll(a, b, c, d, e) {
    const numbers = [a, b, c, d, e];
    let sum = 0;
    for (const number of numbers) {
        sum += number;
    }
    return sum;
}

// rest operator가 있다면

function addAll(...numbers) {
    let sum = 0;
    for (const number of numbers) {
        sum += number;
    }
    return sum;
}

const a1 = [1,2,3,4];
const a2 = [5,6,7,8];
// a1하고 a2를 그대로 더하면 '1,2,3,45,6,7,8' 이런 스트링이 리턴됨. 그래서 [1,2,3,4,5,6,7,8]이라는 리스트를 만들고 싶다면,
const a3 = [...a1, ...a2];
// 이래하면됨. 여기서 ...은 스프레드.

function solveMe(...numbers) {
    let result= [];
    let idx = 0;
    while (idx < numbers.length) {
        if (idx !== 0) {
            result = [...result, numbers[idx]*numbers[0]]
        }
        idx += 1;
    }
    return result;
}
const c = solveMe(2, 1, 2, 3, 4); // [2, 4, 6, 8]
const b = solveMe(5, 10, 20); // [50, 100]
console.log(c);
console.log(b);
console.log([...c, ...b]); // [2, 4, 6, 8, 50, 100]