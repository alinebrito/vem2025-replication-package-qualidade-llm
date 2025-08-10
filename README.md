# Analisando a Qualidade e Eficácia de Códigos Gerados por  LLMs: Um Estudo com Problemas da Plataforma LeetCode

## Instruções de Replicação/Reprodução

### Passo 1: Clonar o Repositório

```bash
git clone https://github.com/alinebrito/vem2025-replication-package-qualidade-llm
cd Codigos
```

> **Nota:** Nesta pasta se encontram todos os scripts executados durante o projeto.

### Passo 2: Instalação de Dependências

* Instale o Docker [Link](https://www.docker.com/products/docker-desktop/)
* Instale o Node [Link](https://nodejs.org/en/download/package-manager)
* Instale o Python3 [Link](https://www.python.org/downloads/)
* Instale as dependências do Python:

  ```bash
  pip install -r requirements.txt
  ```

---

## Scripts

### Script de Coleta de Perguntas

1. Acesse a pasta:

   ```bash
   cd 1-script-coleta-perguntas/
   ```

2. Preencha o arquivo `.env` com os cookies `"csrftoken"` e `"LEETCODE_SESSION"`. (Faça login na plataforma LeetCode [Link](https://leetcode.com/))
   > **Dica:** Utilize a extensão do Chrome "Cookie-Editor". [Link](https://chromewebstore.google.com/detail/cookie-editor/hlkenndednhfkekhgcdicdfddnkalmdm)

3. Execute os seguintes comandos:

   ```bash
   npm install
   node 1_get_algorithms_problems.js   # Gera o arquivo data.json
   node 2_filtered_sorted_problems.js   # Gera o arquivo dataFiltered.json
   docker run -p 3000:3000 alfaarghya/alfa-leetcode-api:2.0.1
   node 3_update_problems.js            # Gera o arquivo dataUpdated.json
   node 4_update_problems_comments.js   # Gera o arquivo dataUpdatedClasses.json
   node 5_update_class_problems.js      # Gera o arquivo dataUpdatedWithSolutions.json
   node 6_count_level_frequency.js      # Gera o arquivo frequencyOutput.json
   ```

### Script de Coleta de Respostas

1. Acesse a pasta:

   ```bash
   cd 2-script-coleta-respostas/
   ```

2. Execute os seguintes comandos:

   ```bash
   python3 1_get_data.py                # Gera os arquivos dataToResponse_llm.json
   python3 2_get_response.py            # Gera todos os arquivos .py de respostas por LLM
   ```

### Script de Assertividade

1. Acesse a pasta:

   ```bash
   cd 3-script-assertividade/
   ```

2. Preencha o arquivo `.env` com os cookies `"csrftoken"` e `"LEETCODE_SESSION"`. (Faça login na plataforma LeetCode [Link](https://leetcode.com/))
   > **Dica:** Utilize a extensão do Chrome "Cookie-Editor". [Link](https://chromewebstore.google.com/detail/cookie-editor/hlkenndednhfkekhgcdicdfddnkalmdm)

3. Execute os seguintes comandos:

   ```bash
   npm install
   node get_assertivity.js              # Gera os arquivos filteredDataToResponse_llm.json
   ```

### Script de Coleta de Métricas SonarQube

1. Acesse a pasta:

   ```bash
   cd 4-script-coleta-metricas-sonar/
   ```

2. Execute os seguintes comandos:

   ```bash
   docker pull sonarqube
   docker run -d --name sonarqube-db -e POSTGRES_USER=sonar -e POSTGRES_PASSWORD=sonar -e POSTGRES_DB=sonarqube postgres:alpine
   docker run -d --name sonarqube -p 9000:9000 --link sonarqube-db:db -e SONAR_JDBC_URL=jdbc:postgresql://db:5432/sonarqube -e SONAR_JDBC_USERNAME=sonar -e SONAR_JDBC_PASSWORD=sonar sonarqube
   npm install
   node 1_get_projects.js
   node 2_get_metrics.js                # Gera os arquivos all_metrics_llm.json
   ```

### Script de Parafraseamento

1. Acesse a pasta:

   ```bash
   cd 5-script-parafraseamento/
   ```

2. Preencha o arquivo `.env` com os cookies `"csrftoken"` e `"LEETCODE_SESSION"`. (Faça login na plataforma LeetCode [Link](https://leetcode.com/))
   > **Dica:** Utilize a extensão do Chrome "Cookie-Editor". [Link](https://chromewebstore.google.com/detail/cookie-editor/hlkenndednhfkekhgcdicdfddnkalmdm)

3. Execute os seguintes comandos:

   ```bash
   python3 1_get_data.py                # Gera os arquivos incorrect_questions_llm.json
   python3 2-get_paraphasing_response.py
   python3 3-get_assertivity.py
   python3 4-get_table.py               # Gera o arquivo assertivity_rates.csv
   ```

### Script de Gráficos

1. Acesse a pasta:

   ```bash
   cd 6-script-graficos/
   ```

2. Execute os seguintes comandos:

   ```bash
   python3 1-caracterizacao_plots.py
   python3 2.1-distribuicao_sonar_metrics.py
   python3 2-all_metrics_sonar_qube.py
   python3 3-assertividade_plots.py
   ```
