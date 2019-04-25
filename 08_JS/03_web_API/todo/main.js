const init = () => {
    const todoBox = document.querySelector('#todo_box');
    const reverseButton = document.querySelector('#reverse_btn');
    const fetchButton = document.querySelector('#fetch_btn');
    const box = document.querySelector('#add_todo_input');
    const btn = document.querySelector('#add_todo_btn');
    // TODO: input, ADD 버튼 누르면 addTodo 이벤트 리스너 잘 버무린다.

    reverseButton.addEventListener('click', e => {
        reverseTodos()
    });

// TODO: 버튼 만들고, 데이터 받아오게 이벤트 리스너 클릭 얍

    const fetchData = URL => {
        fetch(URL)
            .then(res => res.json())
            .then(todos => {
                for (const todo of todos) {
                    addTodo(todo.title, todo.completed);
                }
            })
    };

    const pushToDOM = () => {

    };

    const addTodo = (inputText, completed = false) => {
        const todoBox = document.querySelector('#todo_box');
        const todoCard = document.createElement('div');

        todoCard.classList.add('ui', 'segment', 'todo-item');

        if (completed) todoCard.classList.add('secondary');

        const wrapper = document.createElement('div');
        wrapper.classList.add('ui', 'checkbox');

        const input = document.createElement('input');
        input.setAttribute('type', 'checkbox');
        input.checked = completed;

        input.addEventListener('click', e => {
            if (input.checked) {
                todoCard.classList.add('secondary');
                label.classList.add('completed-label');
                // input.classList.remove('completed-label')
            } else {
                todoCard.classList.remove('secondary');
                label.classList.remove('completed-label');
            }
        });

        const label = document.createElement('label');
        label.innerHTML = inputText;
        if (completed) label.classList.add('completed=label');


        const deleteIcon = document.createElement('i'); // <i></i>
        deleteIcon.classList.add('close', 'icon', 'delete-icon'); // <i class="close icon"></i>

        deleteIcon.addEventListener('click', e => {
            todoCard.remove()

        });

        wrapper.appendChild(input);
        wrapper.appendChild(label);
        todoCard.appendChild(wrapper);
        todoCard.appendChild(deleteIcon);
        todoBox.appendChild(todoCard);
        return todoCard
    };

    const reverseTodos = () => {
        const allTodos = Array.from(document.querySelectorAll('.todo-item'));

        while (todoBox.firstChild) {
            todoBox.removeChild(todoBox.firstChild)
        }

        for (const todo of allTodos.reverse()) {
            todoBox.appendChild(todo)
        }
    };



    fetchData('https://koreanjson.com/todos');


};



init();



