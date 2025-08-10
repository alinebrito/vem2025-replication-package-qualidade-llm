const fs = require('fs');
const path = require('path');
const scanner = require('sonarqube-scanner').default;

const stateFilePath = 'state.json';
const errorLogFilePath = 'error_log.json';

async function runScanner() {
  try {
    const directories = fs.readdirSync('samples').filter(dir => fs.statSync(path.join('samples', dir)).isDirectory());

    let lastProcessedFile = null;
    if (fs.existsSync(stateFilePath)) {
      const state = JSON.parse(fs.readFileSync(stateFilePath, 'utf8'));
      lastProcessedFile = state.lastProcessedFile;
    }

    let startProcessing = !lastProcessedFile;
    for (const dir of directories) {
      const files = fs.readdirSync(path.join('samples', dir)).filter(file => path.extname(file) === '.py').sort();

      for (const file of files) {
        const filePath = path.join(dir, file);

        if (!startProcessing && filePath === lastProcessedFile) {
          startProcessing = true;
          continue;
        }

        if (startProcessing) {
          await new Promise((resolve, reject) => {
            scanner(
              {
                serverUrl: 'http://localhost:9000',
                token: 'squ_97512171768606562570c9962b18c6f41bcf0781',
                options: {
                  'sonar.projectKey': file,
                  'sonar.projectName': file,
                  'sonar.projectDescription': `Description for ${file} project...`,
                  'sonar.sources': path.join('samples', dir, file),
                },
              },
              error => {
                if (error) {
                  console.error(error);
                  const errorLog = fs.existsSync(errorLogFilePath)
                    ? JSON.parse(fs.readFileSync(errorLogFilePath, 'utf8'))
                    : [];
                  errorLog.push(filePath);
                  fs.writeFileSync(errorLogFilePath, JSON.stringify(errorLog, null, 2));
                  reject(error);
                } else {
                  console.log("====================================");
                  console.log('Finalizado! ARQUIVO: ' + file);
                  console.log("====================================");
                  fs.writeFileSync(stateFilePath, JSON.stringify({ lastProcessedFile: filePath }));
                  resolve();
                }
              }
            );
          });
        }
      }
    }
  } catch (error) {
    console.log("====================================");
    console.error('Erro ao rodar o scanner:', error);
    console.log("====================================");
  }
}

runScanner().catch(error => {
  console.log("====================================");
  console.error('Erro ao rodar o scanner:', error);
  console.log("====================================");
});