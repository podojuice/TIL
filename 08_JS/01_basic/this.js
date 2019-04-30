function hi () {

}

const bye = () => {

};

const me = {
    name: 'goo',
    phone: '010',
    mail: 'google',
    intro: function () {
        return `Hi my name is ${this.name}`
    }
};
console.log(me.intro())
const you = {
    name: 'yu',
    phone: '010',
    mail: 'google',
    // arrow function에서는 this를 어디서 찾고자 하느냐. 자기를 담고 있는 객체 밖에서 찾으려고 함.
    // 위에 me 객체에서 있는 intro처럼 function을 만들면 제 위치에 있는 친구를 찾아감. this 키워드가 좀 이상하다.
    intro: () => {
        return `Hi my name is ${this.name}`
    },
    wait: function () {
        setTimeout(() => {
            console.log(this.mail)
        }, 1000)
    }
};

console.log(you.intro());
console.log(you.wait());