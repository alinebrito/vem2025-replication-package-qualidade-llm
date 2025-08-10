require('dotenv').config();
const fs = require('fs');

const BASE_URL = "https://leetcode.com";
const leetcodeSession = process.env.LEETCODE_SESSION;
const csrfToken = process.env.csrftoken;

if (!leetcodeSession) {
    console.error("LEETCODE_SESSION is not defined. Please set the environment variable.");
    process.exit(1);
}

if (!csrfToken) {
    console.error("csrftoken is not defined. Please set the environment variable.");
    process.exit(1);
}

function log(message) {
    console.log(`[${new Date().toUTCString()}] ${message}`);
}

const delay = (ms) => new Promise((res) => setTimeout(res, ms));

function graphqlHeaders(session, csrfToken) {
    return {
        "content-type": "application/json",
        origin: BASE_URL,
        referer: BASE_URL,
        cookie: `csrftoken=${csrfToken}; LEETCODE_SESSION=${session};`,
        "x-csrftoken": csrfToken,
    };
}

async function executeGraphQLRequest(url, headers, graphql) {
    try {
        const response = await fetch(url, {
            method: "POST",
            headers: headers,
            body: graphql
        });
        const result = await response.json();

        if (result.errors) {
            console.error("GraphQL errors:", result.errors);
            return null;
        }

        return result.data;
    } catch (error) {
        console.log("error", error);
        return null;
    }
}

async function getSolutions(titleSlug, leetcodeSession, csrfToken) {
    log(`Getting question data for "${titleSlug}"...`);

    const headers = graphqlHeaders(leetcodeSession, csrfToken);
    const graphql = JSON.stringify({
        query: `
            query communitySolutions($questionSlug: String!, $skip: Int!, $first: Int!, $query: String, $orderBy: TopicSortingOption, $languageTags: [String!], $topicTags: [String!]) {
                questionSolutions(
                    filters: {questionSlug: $questionSlug, skip: $skip, first: $first, query: $query, orderBy: $orderBy, languageTags: $languageTags, topicTags: $topicTags}
                ) {
                  solutions {
                    id
                    title
                    commentCount
                    topLevelCommentCount
                    viewCount
                    pinned
                    isFavorite
                }
                  totalNum
                }
            }
        `,
        variables: {
            questionSlug: titleSlug,
            skip: 0,
            first: 15,
            query: "",
            orderBy: "most_votes",
            languageTags: ["python3", "python"],
            topicTags: []
        },
        operationName: "communitySolutions"
    });

    const result = await executeGraphQLRequest("https://leetcode.com/graphql/", headers, graphql);

    if (!result?.questionSolutions) {
        console.error("Unexpected response format:", result);
        return;
    }

    await delay(3000);
    return result.questionSolutions;
}

async function getSolutionContent(topic, leetcodeSession, csrfToken) {
    // log(`Getting solution data for ${topic.id} | "${topic.title}"...`);
    log(`Getting solution data for "${topic.id}"...`);

    const headers = graphqlHeaders(leetcodeSession, csrfToken);
    const graphql = JSON.stringify({
        query: `query communitySolution($topicId: Int!) {
            topic(id: $topicId) {
                id
                post {
                    id
                    content
                    isOwnPost
                }
            }
        }`,
        variables: { topicId: topic.id },
        operationName: "communitySolution"
    });

    const result = await executeGraphQLRequest("https://leetcode.com/graphql/", headers, graphql);

    if (!result?.topic) {
        console.error("Unexpected response format:", result);
        return;
    }

    await delay(3000);
    return result.topic;
}

function extractPythonCode(text) {
    // Regex para blocos de código delimitados por backticks com python ou python3
    const blockRegex = /```(?:python3?|Python3?)\s*\[\]\\n([\s\S]*?)\\n```/g;
    let match;
    let codeBlocks = [];

    while ((match = blockRegex.exec(text)) !== null) {
        codeBlocks.push(match[1].replace(/\\n/g, '\n').trim());
    }

    // Regex para identificar funções Python
    const functionRegex = /def\s+\w+\s*\(.*?\)\s*:\s*([\s\S]*?)(?=\ndef\s|\nclass\s|$)/g;
    let functionMatches = [];
    while ((match = functionRegex.exec(text)) !== null) {
        functionMatches.push(match[0].replace(/\\n/g, '\n').trim());
    }

    // Combinar os resultados
    const combinedCode = [...codeBlocks, ...functionMatches].join('\n\n').trim();

    return combinedCode;
}

function getClassAndMethodDefinition(code) {
    const lines = code.trim().split('\n');
    return lines.slice(0, 2).join('\n');
}

async function updateDataWithSolutions() {
    let dataUpdated;
    let progress = 0;

    try {
        dataUpdated = JSON.parse(fs.readFileSync('./data/dataUpdated.json', 'utf8'));
    } catch (error) {
        console.error("Error reading dataUpdated.json:", error);
        return;
    }

    try {
        progress = JSON.parse(fs.readFileSync('./data/progress.json', 'utf8')).progress;
    } catch (error) {
        console.log("No progress file found, starting from the beginning.");
    }

    for (let i = progress; i < dataUpdated.length; i++) {
        const item = dataUpdated[i];
        const titleSlug = item.stat.question__title_slug;
        try {
            const solutions = await getSolutions(titleSlug, leetcodeSession, csrfToken);
            let classAndMethodDefinition = '';

            for (const solution of solutions.solutions) {
                const solutionContent = await getSolutionContent(solution, leetcodeSession, csrfToken);
                const pythonCode = extractPythonCode(solutionContent.post.content);
                classAndMethodDefinition = getClassAndMethodDefinition(pythonCode);

                if (classAndMethodDefinition && classAndMethodDefinition !== "") {
                    break;
                }
            }

            item.classAndMethodDefinition = classAndMethodDefinition;

            fs.writeFileSync('./data/dataUpdatedWithSolutions.json', JSON.stringify(dataUpdated, null, 2), 'utf8');
            fs.writeFileSync('./data/progress.json', JSON.stringify({ progress: i + 1 }), 'utf8');
        } catch (error) {
            console.error(`Error processing item at index ${i}:`, error);
            break;
        }
    }

    log("Data update complete.");
}

updateDataWithSolutions();