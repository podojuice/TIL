
// function makeArticle (id, title, content) {
//     return {
//         id: id,
//         title: title,
//         content: content,
//         makeOne: function () {
//             return `${this.id} 번 글: ${this.title} => ${this.content}`
//         }
//     }
// }

// 리팩토링 해보기. key랑 value가 같다면, 한번만 써도 키밸류처럼 작동됨. 함수는 function 날려도 됨.

function makeArticle (id, title, content) {
    return {
        id,
        title,
        content,
        makeOne () {
            return `${this.id} 번 글: ${this.title} => ${this.content}`
        },
    }
}
const myObj = {

};

