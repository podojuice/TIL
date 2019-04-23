const numbers = [1, 2, 3, 4, 5];

numbers[0]

numbers.reverse(); // 뒤집기

numbers.push('a'); // 추가

numbers.pop(); // 스택 빼기

numbers.unshift('a'); // 앞에 넣기

numbers.shift(); // 앞에거빼기

numbers.includes(1); // True 인자 찾기

numbers.includes(0); // False

numbers.indexOf('a'); // 있으면 있는 곳 인덱스 뱉어주고, 없으면 -1뱉어줌

numbers.join('-'); // 파이썬과 적는 방법은 반대지만 같은 결과 나옴. 1-2-3-4 이런식.