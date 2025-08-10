const fs = require('fs');
const data = JSON.parse(fs.readFileSync('./data/data.json'));
const problemsData = data["stat_status_pairs"];

// Filter out paid problems and problems without title_slug
let problemsDataFiltered = problemsData.filter((item) => {
    return !item.paid_only && item.stat.question__title_slug != null;   
})

// Sort by total_submitted - Popular problems
let problemsDataSorted = problemsDataFiltered.sort(
    (a,b) => b.stat.total_submitted - a.stat.total_submitted
);

// Get top 25% of the problems
let problemsDataTop25Percent = problemsDataSorted.slice(0, problemsDataSorted.length / 4);

// Save to file
const jsonContent = JSON.stringify(problemsDataTop25Percent);
fs.writeFile("./data/dataFiltered.json", jsonContent, 'utf8', function (err) {
    if (err) {
        return console.log(err);
    }

    console.log("The file was saved!");
});