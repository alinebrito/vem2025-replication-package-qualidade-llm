const fs = require('fs');
const data = JSON.parse(fs.readFileSync('./data/dataFiltered.json'));
const problemsData = data;

const delay = (ms) => new Promise(resolve => setTimeout(resolve, ms));

async function fetchDataForProblems(problemsData) {
    const updatedProblems = [];
    let i = 0;
    const size = problemsData.length;

    for (const problem of problemsData) {
        try {
            await delay(5000);

            // HTTP Request to get additional data from dockerized API (https://github.com/alfaarghya/alfa-leetcode-api)
            const response = await fetch(`http://localhost:3000/select?titleSlug=${problem.stat.question__title_slug}`);
            const data = await response.json();

            // Requisição GraphQL
            const graphqlQuery = {
                query: `
                    query discussionTopic($questionSlug: String!) {
                        questionDiscussionTopic(questionSlug: $questionSlug) {
                            id
                            commentCount
                            topLevelCommentCount
                        }
                    }
                `,
                variables: {
                    questionSlug: problem.stat.question__title_slug
                }
            };

            // GraphQL Request to get discussion data
            const graphqlResponse = await fetch('https://leetcode.com/graphql/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(graphqlQuery)
            });

            const graphqlData = await graphqlResponse.json();

            updatedProblems.push({
                ...problem,
                additionalData: data,
                discussionData: graphqlData.data.questionDiscussionTopic
            });

            i++;
            console.log(i + '/' + size);
        } catch (error) {
            console.error('Error fetching data for problem:', problem.stat.question__title_slug, error);
            updatedProblems.push({ ...problem, additionalData: null, discussionData: null });
        }
    }

    return updatedProblems;
}

async function main() {
    try {
        const updatedProblems = await fetchDataForProblems(problemsData);
        console.log('Problemas atualizados:', updatedProblems);

        const jsonContent = JSON.stringify(updatedProblems);
        
        fs.writeFile("./data/dataUpdated.json", jsonContent, 'utf8', function (err) {
            if (err) {
                return console.log(err);
            }
            console.log("The file was saved!");	
        });
    } catch (error) {
        console.error('Error fetching data for problems:', error);
    }
}

main();