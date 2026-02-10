"use strict";

/* Variables */ console.log("Variables:");
let admin;
let name = "John";

admin = name;
console.log(admin);

let ourPlanetName = "Earth";
let currentUserName = "John";

const BIRTHDAY = '18.04.1982';


/* Comparison */ console.log("\nComparison:");
console.log(5 > 4);
console.log("apple" > "pineapple");
console.log("2" > "12");
console.log(undefined == null);
console.log(undefined === null);
console.log(null == "\n0\n");
console.log(null === +"\n0\n");


/*If-else*/ console.log("\nIf-else:");
if ("0") {
    console.log("Hello");
};

let arbitraryNum = -0.32;
if (arbitraryNum == 0) {
    console.log(0);
} else if (arbitraryNum > 0) {
    console.log(1);
} else {
    console.log(-1);
};

let a = 5, b = -5;
let result = (a + b < 4) ? "Below" : "Over";
console.log(result);

let login = "";
let message;
(login == "Employee") ? message = "Hello" :
    (login == "Director") ? message = "Greetings" :
    (login == '') ? message = "No login" :
    '';

console.log(message);


/*Logical operators*/ console.log("\nLogical operators:");
let age = 19;
if (age >= 14 && age <= 90) {
    console.log("In range");
} else {
    console.log("Not in range");
};
if (!(age >= 14 && age <= 90)) {
    console.log("Not in range");
} else {
    console.log("In range");
};
if (age < 14 || age > 90) {
    console.log("Not in range");
} else {
    console.log("In range");
};

let username = "Admin";
let password = "TheMaster";
if (username === "Admin") {
    if (password === "TheMaster") {
        console.log("Logged in. Greetings");
    } else if (password === '' || password === null || password === undefined) {
        console.log("Canceled password");
    } else {
        console.log("Wrong password");
    }
} else if (username === '' || username === null || username === undefined) {
    console.log("Canceled login");
} else {
    console.log("I don't know you");
};


/*Loops*/ console.log("\nLoops:");
for (let c = 2; c <= 10; c++) {
    if (c % 2 != 0) continue;
    console.log(c);
};

let i = 0;
while (i < 3) {
    console.log(`Number ${i}!`);
    i++;
};

let number = 10;
subNumber:
for (let subNum = 2; subNum <= number; subNum++) {
    for (let divisor = 2; divisor <= (subNum ** 0.5); divisor++) {
        if (subNum % divisor == 0) continue subNumber;
    };
    console.log(subNum);
};


/*Switch*/ console.log("\nSwitch:");
let browser = "Opera";
switch (browser) {
    case "Edge":
        console.log("You've got the Edge!");
        break;

    case "Chrome":
    case "Firefox":
    case "Safari":
    case "Opera":
        console.log("Okay we support these browsers too");
        break;

    default:
        console.log("We hope that this page looks ok!");
};

a = 2;
switch(a) {
    case 0:
        console.log(0);
        break;
    case 1:
        console.log(1);
        break;
    case 2:
    case 3:
        console.log(2, 3);
        break;
};


/*Functions*/ console.log("\nFunctions:");
function checkAge(age) {
    if (age > 18) {
        return true;
    } else {
        return console.log("Did parents allow you?");
    };
};
function checkAge(age) {
    return (age > 18) ? true : console.log("Did parents allow you?");
};
function checkAge(age) {
    return (age > 18) || (console.log("Did parents allow you?"));
};

function min(a, b) {
    return (a > b) ? b : a;
};

function pow(x, n) {
    if (x <= 0) return; 
    let result = x;
    for (let c = 1; c < n; c++) {
        result *= x;
    };
    return result;
};
console.log(pow(2, 3));

/*Arrow functions*/ console.log("\nArrow functions:");
function ask(confirmation, yes, no) {
    if (confirmation) yes();
    else no();
};
ask(
    "Yes",
    function() {console.log("You agreed.");},
    function() {console.log("You canceled the execution.");}
);

function ask(confirmation, yes, no) {
    if (confirmation) yes();
    else no();
};
ask(
    "Yes",
    () => console.log("You agreed."),
    () => console.log("You canceled the execution.")
);

let double = n => n * 2;