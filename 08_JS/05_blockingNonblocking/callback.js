
function getUser(id, callback) {
    setTimeout(() => {
        const users = [
            { id: 1, githubID: 'podo' },
            { id: 2, githubID: 'juice' },
        ];
        const user = users.find(user => user.id===id);
        callback(user);
    }, 2000)
}

const getRepos = (user, callback) => {
    setTimeout(() => {
        const repos = [
            'TIL',
            'Workshop_HW',
            'Python',
            'JS',
        ];
        console.log(repos);
        callback(repos)
    }, 2000)

};

function getCommits (repos, callback) {
    setTimeout(() => {
        const commits = [
            'Init repo',
            'Make index.html'
        ];
        console.log('loaded');
        console.log(commits);
        callback(commits)
    }, 2000)

}

console.log('Start Program');
getUser(1, user => {
    getRepos(user, repos => {
        getCommits(repos[0], commits => {
            console.log(`${commits.length}개 커밋`);
        })
    });
});



// getRepos(user, repos => {
//     console.log(repos);
// });