/*
파이썬이었다면, def my_function(arg1, arg2):
                    ...
                    return value

*/

//1. 함수 키워드 정의
function add(num1, num2) {
    return num1 + num2;
}

//2. 변주에 함수 로직 할당
const sub = function (num1, num2) {
    return num1 - num2;
};

//3. 함수 표현식 2가지
const mul = function (num1, num2) {
    return num1 * num2
}

//function 없앰.
// 괄호와 중괄호 사이에 => 넣는다.

let mul = (num1, num2) => {return num1 * num2};

// 근디 인자가 하나라면, 괄호도 생략 가능하고, 함수 블록안에 코드가 return문 하나라면, {}&return 마저 삭제 가능하다.

let square = function (num) {
    return num**2;
};

square = num => num**2;


let noArgs = () => {
    return 'nothing'
};

noArgs = () => 'nothing';

//바꿔보자.
function sayHello (name = 'ssafy') {
    return `hi ${name} !`
}

const sayHello = (name = 'ssafy') => `hi ${name}!`;

// 익명함수 사용방법

(num => num**2)(4);

// 위에 처럼 쓰면 14가 리턴되는것.

