const http = require('http');
const fs = require('fs');
const path = require('path');

// Configurações da API do SonarQube
const SONARQUBE_URL = 'http://localhost:9000/api';
const METRICS = 'complexity,cognitive_complexity,code_smells,sqale_rating,security_rating,security_hotspots,lines,reliability_rating,reliability_remediation_effort,bugs,vulnerabilities,sqale_index,sqale_debt_ratio,security_remediation_effort,ncloc';
const AUTH_TOKEN = 'squ_91323e14de48fa4356684dabe3f6239d6245e644';

// Função para fazer requisições HTTP GET
function httpGet(url) {
    return new Promise((resolve, reject) => {
        const options = {
            headers: {
                'Authorization': `Basic ${Buffer.from(AUTH_TOKEN + ':').toString('base64')}`
            }
        };

        http.get(url, options, (res) => {
            let data = '';

            res.on('data', (chunk) => {
                data += chunk;
            });

            res.on('end', () => {
                resolve(JSON.parse(data));
            });
        }).on('error', (err) => {
            reject(err);
        });
    });
}

// Função para obter todos os projetos do SonarQube
async function getProjects() {
    const allProjects = [];
    let page = 1;
    let pageSize = 100;
    let total = 0;

    try {
        do {
            const url = `${SONARQUBE_URL}/projects/search?p=${page}&ps=${pageSize}`;
            const response = await httpGet(url);
            const projects = response.components || [];
            allProjects.push(...projects);
            total = response.paging.total;
            page++;
        } while (allProjects.length < total);
    } catch (error) {
        console.error('Erro ao obter projetos:', error);
    }

    return allProjects;
}

// Função para converter valores de rating numéricos para letras
function convertRating(value) {
    switch (value) {
        case '1.0':
            return 'A';
        case '2.0':
            return 'B';
        case '3.0':
            return 'C';
        case '4.0':
            return 'D';
        case '5.0':
            return 'E';
        default:
            return value;
    }
}

// Função para obter métricas de um projeto específico do SonarQube
async function getMetrics(componentKey) {
    try {
        const url = `${SONARQUBE_URL}/measures/component?component=${componentKey}&metricKeys=${METRICS}`;
        const response = await httpGet(url);

        const measures = response.component.measures;
        const metrics = {
            project: componentKey,
            maintainability: {},
            reliability: {},
            security: {},
            complexity: {},
            size: {}
        };

        measures.forEach(measure => {
            switch (measure.metric) {
                case 'code_smells':
                    metrics.maintainability.issues = measure.value;
                    break;
                case 'sqale_index':
                    metrics.maintainability.technical_debt = measure.value;
                    break;
                case 'sqale_debt_ratio':
                    metrics.maintainability.technical_debt_ratio = measure.value;
                    break;
                case 'sqale_rating':
                    metrics.maintainability.maintainability_rating = convertRating(measure.value);
                    break;
                case 'bugs':
                    metrics.reliability.issues = measure.value;
                    break;
                case 'reliability_rating':
                    metrics.reliability.reliability_rating = convertRating(measure.value);
                    break;
                case 'reliability_remediation_effort':
                    metrics.reliability.reliability_remediation_effort = measure.value;
                    break;
                case 'vulnerabilities':
                    metrics.security.issues = measure.value;
                    break;
                case 'security_rating':
                    metrics.security.security_rating = convertRating(measure.value);
                    break;
                case 'security_remediation_effort':
                    metrics.security.security_remediation_effort = measure.value;
                    break;
                case 'complexity':
                    metrics.complexity.cyclomatic_complexity = measure.value;
                    break;
                case 'cognitive_complexity':
                    metrics.complexity.cognitive_complexity = measure.value;
                    break;
                case 'ncloc':
                    metrics.size.lines_of_code = measure.value;
                    break;
                default:
                    break;
            }
        });

        return metrics;
    } catch (error) {
        console.error(`Erro ao obter métricas para o projeto ${componentKey}:`, error);
        return null;
    }
}

// Função principal
async function main() {
    const directories = fs.readdirSync('samples').filter(dir => fs.statSync(path.join('samples', dir)).isDirectory());

    for (const dir of directories) {
        const projects = await getProjects();
        const filteredProjects = projects.filter(project => project.key.endsWith(`${dir}.py`));

        const allMetrics = [];
        for (const project of filteredProjects) {
            const metrics = await getMetrics(project.key);
            if (metrics) {
                allMetrics.push(metrics);
            }
        }

        fs.writeFileSync(`./data/all_metrics_${dir}.json`, JSON.stringify(allMetrics, null, 2));
        console.log(`Métricas salvas em all_metrics_${dir}.json`);
    }
}

main();