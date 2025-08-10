require('dotenv').config();
const fs = require('fs');
const path = require('path');

const BASE_URL = "https://leetcode.com";
let currentTokenIndex = 1;

function getCurrentToken() {
    return {
        leetcodeSession: process.env[`LEETCODE_SESSION${currentTokenIndex}`],
        csrfToken: process.env[`csrftoken${currentTokenIndex}`]
    };
}

function rotateToken() {
    currentTokenIndex++;
    if (!process.env[`LEETCODE_SESSION${currentTokenIndex}`] || !process.env[`csrftoken${currentTokenIndex}`]) {
        currentTokenIndex = 1; // Reset to the first token if out of bounds
    }
    console.log(`Rotating token. Now using LEETCODE_SESSION${currentTokenIndex} and csrftoken${currentTokenIndex}`);
}

function validateTokens() {
    const { leetcodeSession, csrfToken } = getCurrentToken();
    if (!leetcodeSession) {
        console.error("LEETCODE_SESSION is not defined. Please set the environment variable.");
        process.exit(1);
    }

    if (!csrfToken) {
        console.error("csrftoken is not defined. Please set the environment variable.");
        process.exit(1);
    }
}

validateTokens();

const delay = (ms) => new Promise((res) => setTimeout(res, ms));

function log(message) {
    console.log(`[${new Date().toUTCString()}] ${message}`);
}

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
    const maxRetries = 3;
    const retryDelay = (retryCount) => 2 ** retryCount * 1000;

    for (let attempt = 0; attempt < maxRetries; attempt++) {
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
            console.error(`Attempt ${attempt + 1} failed:`, error.message);

            if (attempt < maxRetries - 1) {
                console.log(`Retrying in ${retryDelay(attempt)}ms...`);
                await delay(retryDelay(attempt));
            } else {
                console.error("Max retries reached. Request failed.");
                rotateToken();
                validateTokens();
                return "TIME OUT!";
            }
        }
    }
}

async function getQuestionID(titleSlug) {
    log(`Getting question details for titleSlug: ${titleSlug}...`);
    const { leetcodeSession, csrfToken } = getCurrentToken();
    const headers = graphqlHeaders(leetcodeSession, csrfToken);
    const graphql = JSON.stringify({
        query: `query questionId($titleSlug: String!) {
            question(titleSlug: $titleSlug) {
                questionId
            }
        }`,
        variables: {
            titleSlug: titleSlug
        },
        operationName: "questionId"
    });

    const result = await executeGraphQLRequest("https://leetcode.com/graphql/", headers, graphql);

    if (!result || !result.question) {
        console.error("Unexpected response format or no question found:", result);
        return null;
    }

    return result.question;
}

async function interpretSolution(problemSlug, questionId, typedCode, dataInput, language = "python3") {
    const { leetcodeSession, csrfToken } = getCurrentToken();
    const url = `${BASE_URL}/problems/${problemSlug}/interpret_solution/`;
    const headers = {
        "content-type": "application/json",
        "origin": BASE_URL,
        "referer": `${BASE_URL}/problems/${problemSlug}/`,
        "x-csrftoken": csrfToken,
        "cookie": `LEETCODE_SESSION=${leetcodeSession}; csrftoken=${csrfToken};`,
        "User-Agent": "curl/8.0.1",
        "Accept": "*/*"
    };

    const body = JSON.stringify({
        lang: language,
        question_id: questionId,
        typed_code: typedCode,
        data_input: dataInput
    });

    const maxRetries = 3;
    const retryDelay = (retryCount) => 5 ** retryCount * 1000;

    for (let attempt = 0; attempt < maxRetries; attempt++) {
        try {
            const response = await fetch(url, {
                method: "POST",
                headers: headers,
                body: body
            });

            if (response.status === 403) {
                throw new Error("Forbidden: You don't have permission to access this resource. interpret_solution route");
            } else if (response.status === 429) {
                throw new Error("Too Many Requests: You have sent too many requests in a given amount of time. interpret_solution route");
            }

            const result = await response.json();

            if (result.errors) {
                console.error("Errors:", result.errors);
                return null;
            }

            return result;
        } catch (error) {
            console.error('Error:', error.message);

            if ((error.message.includes("Too Many Requests") || error.message.includes("Forbidden")) && attempt < maxRetries - 1) {
                console.log(`Retrying in ${retryDelay(attempt)}ms...`);
                await delay(retryDelay(attempt));
            } else {
                if (error.message.includes("Forbidden")) {
                    const errorResponse = {
                        response: true,
                        status: "error"
                    };
                    console.log("Saving error response:", errorResponse);
                    return errorResponse;
                }
                rotateToken();
                validateTokens();
                return null;
            }
        }
    }
}

async function checkSubmissionStatus(problemSlug, interpretId) {
    const { leetcodeSession, csrfToken } = getCurrentToken();
    const url = `${BASE_URL}/submissions/detail/${interpretId}/check/`;
    const headers = {
        "content-type": "application/json",
        "referer": `${BASE_URL}/problems/${problemSlug}/submissions`,
        "x-csrftoken": csrfToken,
        "cookie": `LEETCODE_SESSION=${leetcodeSession}; csrftoken=${csrfToken};`,
        "User-Agent": "curl/8.0.1",
        "Accept": "*/*"
    };

    try {
        const response = await fetch(url, {
            method: "GET",
            headers: headers
        });
        const result = await response.json();

        if (result.errors) {
            console.error("Errors:", result.errors);
            return null;
        }

        return result;
    } catch (error) {
        console.log("Error:", error);
        return null;
    }
}

async function getConsolePanelConfig(titleSlug) {
    log(`Getting console panel config for titleSlug: ${titleSlug}...`);
    const { leetcodeSession, csrfToken } = getCurrentToken();
    const headers = graphqlHeaders(leetcodeSession, csrfToken);
    const graphql = JSON.stringify({
        query: `query consolePanelConfig($titleSlug: String!) {
            question(titleSlug: $titleSlug) {
                exampleTestcaseList
            }
        }`,
        variables: {
            titleSlug: titleSlug
        },
        operationName: "consolePanelConfig"
    });

    const result = await executeGraphQLRequest("https://leetcode.com/graphql/", headers, graphql);

    if (!result || !result.question) {
        console.error("Unexpected response format or no question found:", result);
        return null;
    }

    return result.question;
}

function createFilteredJsonFiles() {
    const dataDir = path.join(__dirname, 'data');
    const responseDir = path.join(__dirname, 'response');
    const llms = ['gpt-4', 'claude-3-haiku', 'llama-3.1', 'gemini'];

    for (const llm of llms) {
        const originalFilePath = path.join(dataDir, `dataToResponse_${llm}.json`);
        const newFilePath = path.join(responseDir, `filteredDataToResponse_${llm}.json`);

        // Verificar se o arquivo filtrado já existe
        if (fs.existsSync(newFilePath)) {
            log(`Filtered JSON file for ${llm} already exists. Skipping creation.`);
            continue;
        }

        const originalData = JSON.parse(fs.readFileSync(originalFilePath, 'utf8'));

        const filteredData = originalData.map(item => ({
            questionId: item.questionId,
            titleSlug: item.titleSlug,
            fileName: item.fileName,
            response: false
        }));

        fs.writeFileSync(newFilePath, JSON.stringify(filteredData, null, 2));
        log(`Created filtered JSON file for ${llm}`);
    }
}

async function dataToResponse_LLM() {
    const responseDir = path.join(__dirname, 'response');
    const llms = ['gpt-4', 'claude-3-haiku', 'llama-3.1', 'gemini'];

    for (const llm of llms) {
        const llmFilePath = path.join(responseDir, `filteredDataToResponse_${llm}.json`);
        const llmData = JSON.parse(fs.readFileSync(llmFilePath, 'utf8'));
        const llmPath = path.join(responseDir, llm);

        log("==========================================================");
        log(`Processing LLM: ${llm}`);

        // Verificar se é um diretório
        if (fs.lstatSync(llmPath).isDirectory()) {
            // Obter a lista de arquivos dentro da pasta LLM
            const files = fs.readdirSync(llmPath);
            const totalFiles = files.length;
            let processedFiles = 0;

            for (let i = 0; i < files.length; i++) {
                const file = files[i];
                const filePath = path.join(llmPath, file);

                // Encontrar o índice correto no JSON filtrado
                let jsonIndex = llmData.findIndex(item => item.fileName === file);

                if (jsonIndex === -1) {
                    const fileId = file.split('_')[0];
                    jsonIndex = llmData.findIndex(item => item.questionId == fileId);
                }

                if (jsonIndex === -1) {
                    log(`File ${file} not found in JSON data. Skipping.`);
                    continue;
                }

                // Verificar se a resposta já foi processada
                if (llmData[jsonIndex].response !== false) {
                    log("==========================================================");
                    log(`Skipping already processed file: ${file}`);
                    processedFiles++;
                    continue;
                }

                // Ler o conteúdo do arquivo e ajustar o texto
                const typedCode = fs.readFileSync(filePath, 'utf8').replace(/\n/g, '\r\n');
                log("==========================================================");
                log(`Processing file: ${file}`);

                // Executar a lógica existente com o conteúdo do arquivo
                const question = await getQuestionID(llmData[jsonIndex].titleSlug);
                if (!question) {
                    log(`Failed to get question details for file: ${file}`);
                    continue;
                }

                const consolePanelConfig = await getConsolePanelConfig(llmData[jsonIndex].titleSlug);
                if (!consolePanelConfig) {
                    log(`Failed to get console panel config for file: ${file}`);
                    continue;
                }

                const result = await interpretSolution(
                    llmData[jsonIndex].titleSlug,
                    question.questionId,
                    typedCode,
                    consolePanelConfig.exampleTestcaseList.join('\n')
                );

                if (!result) {
                    log(`Failed to interpret solution for file: ${file}`);
                    continue;
                }

                log(`Checking submission for submissionId: ${result.interpret_id}...`);
                await delay(5000);

                const interpretId = result.interpret_id;
                const submissionStatus = await checkSubmissionStatus(llmData[jsonIndex].titleSlug, interpretId);

                if (!submissionStatus) {
                    log(`Failed to check submission status for file: ${file}`);
                    continue;
                }

                // Atualizar o status da resposta
                let status;
                if (submissionStatus.status_code === 10) {
                    if (submissionStatus.total_correct === submissionStatus.total_testcases) {
                        status = 'success';
                    } else {
                        status = 'incorrect';
                    }
                } else {
                    status = 'error';
                }

                llmData[jsonIndex] = {
                    ...llmData[jsonIndex],
                    response: true,
                    status: status,
                    details: submissionStatus
                };

                // Atualizar o arquivo JSON
                fs.writeFileSync(llmFilePath, JSON.stringify(llmData, null, 2));
                log(`Updated JSON file for ${llm}: ${file}`);

                processedFiles++;
                log(`Processed ${processedFiles}/${totalFiles} files for ${llm}`);
                await delay(5000);
            }
        }
    }
}

// Chamar a função para criar os arquivos JSON filtrados
createFilteredJsonFiles();

// Chamar a função para processar as respostas
dataToResponse_LLM();