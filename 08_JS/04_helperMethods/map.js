// ES5 for loop
// var numbers = [1,2,3];
// var doubleNumbers = [];
//     for (var i = 0; i<numbers.length(); i++) {
//     doubleNumbers.add(numbers[i]*2)
// }


//ES6+
const numbers = [1,2,3];

function double(n) {
    return n*2;
}

// const doubleNumbers = number.map(double);

const tripleNumbers = numbers.map(number => {
    return number * 3;
});

console.log(tripleNumbers);

const images = [
    {hei :100, wid: 50},
    {hei :100, wid: 51},
    {hei :100, wid: 52},
];

const cal = (k) => {
  return (k['hei']*k['wid']);
};
console.log(images.map(cal));

/*
아래의 pluck 함수를 완성하시오.

 */

function pluck(array, property) {
    return array.map(e => {
        return e[property]
    });
}

const paints = [
    { color: 'red'},
    { color: 'blue'},
    { color: 'white'},
    { smell: 'ughh'},
];

console.log(pluck(paints, 'color')); // ['red', 'blue', 'white']