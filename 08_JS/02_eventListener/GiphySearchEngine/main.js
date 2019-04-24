/* 1. <input> 태그 안의 값을 잡는다. */
const inputArea = document.querySelector('#js-userinput');
const button = document.querySelector('#js-go');
const resultArea = document.querySelector('#result-area');


inputArea.addEventListener('keydown', e => {
    if (e.key === 'Enter') {
        searchAndPush(inputArea.value);
    }
});

button.addEventListener('click', e => {
    searchAndPush(inputArea.value);
});

// AJAX 요청을 알아보자.
/*
원래 기존의 요청은
1. 링크 누르고,
2. href로 요청이 가고,
3. 브라우저가 새로고침되고, 응답이 render가 되는건데,

AJAX는
1. 어떤 event가 발생하고,
2. 요청을 전송하고, 응답이 도착할 때가지 기다린다. '화면전환이 없다'.
3. 응답이 오면, 지금 문서에서 응답 내용을 추가로 render 한다.
 */


const searchAndPush = keyword => {
    /* 2. Giphy API 를 통해 data 를 받아서 가공한다. */
    const KEY = 'Ldcqgtqu125iLLI29Vxvexb9VYLFF2yB';
    const URL = `http://api.giphy.com/v1/gifs/search?q=${keyword}&api_key=${KEY}`;
    const AJAXCall = new XMLHttpRequest(); // AJAX 요청을 보내줄 친구
    AJAXCall.open('GET', URL); // 요청 발사 준비
    AJAXCall.send();
    AJAXCall.addEventListener('load', e=> {
        const ParseData = JSON.parse(e.target.response);
        pushToDOM(ParseData);
    });
    /* 3. GIF 파일들을 index.html(DOM)에 밀어 넣어서 보여준다. */
    const pushToDOM = data => {
        resultArea.innerHTML = null;
        const dataArray = data.data;
        let imageURL;
        for (const imgData of dataArray) {
            imageURL = imgData.images.fixed_height.url;
            element = document.createElement('img');
            element.className = 'container-image';
            element.src = imageURL;
            element.alt = 'photo';
            resultArea.appendChild(element);

        }
    };

};














