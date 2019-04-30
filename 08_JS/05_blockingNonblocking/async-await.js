
const getUser = id =>{
    const users = [{ id: 1, githubID: 'podo' }, { id: 2, githubID: 'juice' }];
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            const user = users.find(user => user.id===id);
            if (user) {
                resolve(user)
            } else {
                reject(new Error('can not find user'))
            }

        }, 2000)
    });
};

const getRepos = user => {
    const repos = ['TIL', 'Workshop_HW', 'Python', 'JS',];
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            if (repos) {
                resolve(repos)
            } else {
                reject(new Error('break'))
            }
        }, 2000)
    });
};

const getCommits = repos => {
    const commits = ['Init repo','Make index.html' ];
    return new Promise((resolve, reject)=> {
        setTimeout(() => {
            if (commits) {
                resolve(commits);
            } else {
                reject(new Error('ERROR'));
            }

        }, 2000)
    });
};

console.log('Start Program');
// getUser(1, user => {
//     getRepos(user, repos => {
//         getCommits(repos[0], commits => {
//             console.log(`${commits.length}개 커밋`);
//         })
//     });
// });

async function main () {
    try {
        const user = await getUser(1);
        const repos = await getRepos(user);
        const commits = await getCommits(repos[0]);
        console.log(commits.length)
    } catch (e) {
        console.error(e);
    }
}

main();


