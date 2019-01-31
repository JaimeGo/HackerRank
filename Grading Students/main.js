'use strict';

const fs = require('fs');

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.trim().split('\n').map(str => str.trim());

    main();
});

function readLine() {
    return inputString[currentLine++];
}

/*
 * Complete the gradingStudents function below.
 */
function gradingStudents(grades) {
    /*
     * Write your code here.
     */
    
    let gradesList = []
    
    for (let oldGrade of grades) {

        let newGrade = oldGrade
        
        if (oldGrade >= 38) {

            let rem = oldGrade % 5

            if (5 - rem < 3) {

                newGrade = oldGrade + 5 - rem
                
            } 

        }

        gradesList.push(newGrade)

    }

    return gradesList

}

function main() {
    const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

    const n = parseInt(readLine(), 10);

    let grades = [];

    for (let gradesItr = 0; gradesItr < n; gradesItr++) {
        const gradesItem = parseInt(readLine(), 10);
        grades.push(gradesItem);
    }

    let result = gradingStudents(grades);
    
    ws.write(result.join("\n") + "\n");

    ws.end();
}
