const myObject = {
    coffee: 'Americano',
    iceCream: 'Cookie and Cream',
};

const jsonData = JSON.stringify(myObject); // 오브젝트(파이썬으로치면 딕셔너리)를 오브젝트 표현식으로 string을 만들어 리턴해주는거.
//문자열이기 때문에 키로 접근하거나 오브젝트 메소드 못씀. 이걸 쓰는 이유는 쉽게 다시 오브젝트로 parsing이 가능함.

const parseData = JSON.parse(jsonData);

console.log(typeof parseData);