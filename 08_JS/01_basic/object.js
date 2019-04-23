const me = {
    name: 'hyunGoo',
    'phone number': '01012341234', // 띄어쓰기가 있으면, 'key': 이렇게 쿼트 안에 넣어줘야.
    appleProducts: {
        ipad: '2018pro',
        iphone: '6s+',
        macbook: '2018 pro',
    }

};

me.name === me[name] === me['name']

me.appleProducts.ipad // 이런식으로 접근 가능

//만약 띄어쓰기가 있다면,
me['phone number']
//이렇게 가야함.