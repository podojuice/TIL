//  인자로 배열을 받는다. 해당 배열의 모든 요소를 더해서 더한 숫자를 리턴한다.

const numbersEachAdd = numbers => {
    let acc = 0;
    for (const number of numbers) {
        acc += number
    }
    return acc;
};

console.log(numbersEachAdd([1,2,3,4,5]));

// 이번엔 배열을 받아 배열의 모든 요소를 뺀 숫자를 리턴해보자.

const numbersEachSub = numbers => {
    let acc = 0;
    for (const number of numbers) {
        acc -= number;
    }
    return acc;
};
console.log(numbersEachSub([1,2,3,4,5]));

// 이번엔 배열을 받아 배열의 모든 요소를 곱한 숫자를 리턴해보자.

const numbersEachMul = numbers => {
    let acc = 1;
    for (const number of numbers) {
        acc *= number;
    }
    return acc;
};
console.log(numbersEachMul([1,2,3,4,5]));


// 위에 작업들을 편하게 바꿀 수 없을까? 숫자로 이루어진 배열의 요소들을 각각 ??한다.

const numberEach = (numbers, callback) => {
  let acc; // js는 변수 선언만 가능.
  for (const num of numbers) {
      acc = callback(num, acc)
  }
  return acc;
};

const adder = (number, sum=0) => {
  return sum + number;
};

numberEach([1,2,3,4,5], adder);

const muler = (num, sum=1) => {
    return sum *= num
};

numberEach([1,2,3,4,5], muler);


// 결국 하고싶은 것은

console.log(numberEach([1,2,3,4,5], (number, sum=0) => sum + number ));