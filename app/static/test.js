var numberOfStudentsEjected = 0;

function sayHi() { 
    alert("Hi2");
    alert("Hi3");
}

function ejectStudent() {
    //Update the database
    numberOfStudentsEjected += 1;
    displayNumberOfStudentsEjected(); 
}

function displayNumberOfStudentsEjected() {
    alert ("Number of Students : "+ numberOfStudentsEjected);
}

