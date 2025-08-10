const fs = require('fs');

// Description: This file contains the code to fetch the data from the leetcode website.
let requestOptions = {
   method: 'GET',
   redirect: 'follow'
};

// Fetch the algorithm problems from leetcode
fetch("https://leetcode.com/api/problems/algorithms/", requestOptions)
   .then(response => response.json())
   .then(result => {
      // console.log(result);
      const jsonContent = JSON.stringify(result);
      fs.writeFile("./data/data.json", jsonContent, 'utf8', function (err) {
         if (err) {
             return console.log(err);
         }
     
         console.log("The file was saved!");
      });
   })
   .catch(error => console.log('error', error));