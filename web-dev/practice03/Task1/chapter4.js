/*Methods of primitives*/ console.log("Methods of primitives:");
let str = "Hello";
str.test = 5;
console.log(str.test);

let n = 1.23456;
console.log(n.toFixed(2));

str = "Hello!";
console.log(str.toUpperCase());


/*Numbers*/ console.log("\nNumbers:");
let num = 255;
console.log(num.toString(16));
console.log(num.toString(2));   
console.log(123456..toString(36));

num = 1.23456;
console.log(Math.round(num * 100) / 100); 

function randomInteger(min, max) {
    let rand = min + Math.random() * (max + 1 - min);
    return Math.floor(rand);
}

console.log(randomInteger(1, 3));


/*Strings*/ console.log("\nStrings:");
function ucFirst(str) {
    if (!str) return str;

    return str[0].toUpperCase() + str.slice(1);
};

console.log(ucFirst("somestring"));

function checkSpam(str) {
    let strlower = str.toLowerCase();

    return strlower.includes("viagra") || strlower.includes("xxx");
}

function truncate(str, maxlen) {
    return (str.length > maxlen) ?
        str.slice(0, maxlen - 3) + "..." : str;
}; 

console.log(truncate("abcdefghi", 6));

function extractCurrencyValue(str) {
    return +str.slice(1);
}

console.log(extractCurrencyValue("$228"));


/*Arrays*/ console.log("\nArrays:");
let fruits = ["Apples", "Pear", "Orange"];
let shoppingCart = fruits;
shoppingCart.push("Banana");
console.log( fruits.length );

let styles = ["Jazz", "Blues"];
styles.push("Rock-n-Roll");
styles[Math.floor((styles.length - 1) / 2)] = "Classics";
console.log(styles.shift());
styles.unshift("Rap", "Reggae");

function getMaxSubSum(arr) {
    let maxSum = 0;
    let partialSum = 0;
    for (let item of arr) { 
        partialSum += item;
        maxSum = Math.max(maxSum, partialSum); 
        if (partialSum < 0) partialSum = 0; 
    }
    return maxSum;
}

console.log( getMaxSubSum([-1, 2, 3, -9]) ); 
console.log( getMaxSubSum([-1, 2, 3, -9, 11]) );
console.log( getMaxSubSum([-2, -1, 1, 2]) );
console.log( getMaxSubSum([100, -9, 2, -3, 5]) ); 
console.log( getMaxSubSum([1, 2, 3]) );
console.log( getMaxSubSum([-1, -2, -3]) );


/*Array methods*/ console.log("\nArray methods:");
function camelize(str) {
    let words = str.split('-');
    let uppercasedWords = words.map((word, index) => (index == 0) ? word : word[0].toUpperCase() + word.slice(1));
    return uppercasedWords.join('');
};
let someSeparatedString = "-background-color";
console.log(camelize(someSeparatedString));

function filterRange(arr, a, b) {
    return arr.filter(item => (item >= a && item <= b));
};
let arr = [5, 3, 8, 1];
console.log(filterRange(arr, 1, 4));

function filterRangeInPlace(arr, a, b) {
    for (let ind = 0; ind < arr.length; ind++) {
        if (arr[ind] >= a && arr[ind] <= b) {
            continue;
        } else {
            arr.splice(ind, 1);
            ind--;
        };
    };
};
filterRangeInPlace(arr, 1, 4);
console.log(arr);

arr = [5, 2, 1, -10, 8];
arr.sort();
arr.reverse();
console.log(arr);

function copySorted(arr) {
    return arr.slice().sort();
};
arr = ["HTML", "JavaScript", "CSS"];
let sortedArr = copySorted(arr);
console.log(sortedArr);

function Calculator() {
    this.methods = {
        "+" : (a, b) => a + b,
        "-" : (a, b) => a - b
    };
    this.calculate = function(str) {
        let split = str.split(' ');
        let num1 = +split[0];
        let opr = split[1];
        let num2 = +split[2];

        if (!this.methods[opr] || isNaN(num1) || isNaN(num2)) return NaN;

        return this.methods[opr](num1, num2);
    };
    this.addMethod = function(name, func) {
        this.methods[name] = func;
    };
};
let calc1 = new Calculator;
console.log(calc1.calculate("1 + 2"));
calc1.addMethod("**", (a, b) => a ** b);
console.log(calc1.calculate("2 ** 3"));

let john = {name: "John", age: 25};
let pete = {name: "Pete", age: 30};
let mary = {name: "Mary", age: 28};
let users = [john, pete, mary];
let names = users.map(item => item.name);
console.log(names);

john = {name: "John", surname: "Smith", id: 1};
pete = {name: "Pete", surname: "Hunt", id: 2};
mary = {name: "Mary", surname: "Key", id: 3};
users = [john, pete, mary];
let usersMapped = users.map(item => ({
    fullName: `${item.name} ${item.surname}`,
    id: item.id
}));
console.log( usersMapped[0].id )
console.log( usersMapped[0].fullName ) 

function sortByAge(arr) {
    return arr.sort((obj1, obj2) => obj1.age - obj2.age);
};
john = {name: "John", age: 25};
pete = {name: "Pete", age: 30};
mary = {name: "Mary", age: 29};
arr = [pete, john, mary];
sortByAge(arr);
console.log(arr[0].name);
console.log(arr[1].name);
console.log(arr[2].name);

function getAverageAge(arr) {
    return arr.reduce((totalAge, item) => totalAge + item.age, 0) / arr.length;
};
arr = [pete, john, mary];
console.log(getAverageAge(arr));

function unique(arr) {
    let result = [];
    for (let word of arr) {
        if (!result.includes(word)) result.push(word);
    };
    return result;
};
let strings = ["Hare", "Krishna", "Hare", "Krishna",
  "Krishna", "Krishna", "Hare", "Hare", ":-O"
];
console.log(unique(strings));

function groupById(arr) {
    return arr.reduce((obj, item) => {
        obj[item.id] = item;
        return obj;
    }, {});
};
users = [
  {id: 'john', name: "John Smith", age: 20},
  {id: 'ann', name: "Ann Smith", age: 24},
  {id: 'pete', name: "Pete Peterson", age: 31},
];
let usersById = groupById(users);
console.log(usersById);


/*Map and set*/ console.log("\nMap and set:");
function unique(arr) {
    return Array.from(new Set(arr));
}
let values = ["Hare", "Krishna", "Hare", "Krishna",
  "Krishna", "Krishna", "Hare", "Hare", ":-O"
];
console.log(unique(values));

function aclean(arr) {
    let obj = {};
    for (let ind = 0; ind < arr.length; ind++) {
        let key = arr[ind].toLowerCase().split('').sort().join('')
        console.log(key);
        obj[key] = arr[ind];
    };
    return Object.values(obj);
};
arr = ["nap", "teachers", "cheaters", "PAN", "ear", "era", "hectares"];
console.log(aclean(arr));

let map = new Map();
map.set("name", "John");
let keys = Array.from(map.keys());
keys.push("more");
console.log(keys);


/*Object.keys, values, entries*/ console.log("\nObject.keys, values, entries:");
function sumSalaries(obj) {
    let salaries = Object.values(obj);
    if (salaries.length > 0) {
        let totalSalary = 0;
        for (let salary of salaries) totalSalary += salary;
        return totalSalary;
    } else {
        return 0;
    };
};
let salaries = {
  "John": 100,
  "Pete": 300,
  "Mary": 250
};
console.log(sumSalaries(salaries));

function count(obj) {
    return Object.keys(obj).length;
};
let user = {
  name: 'John',
  age: 30
};
console.log(count(user));


/*Destructuring assignment*/ console.log("\nDestructuring assignment:");
user = {name: "John", years: 30};
let {name, years: age, isAdmin = false} = user;
console.log(name);
console.log(age);
console.log(isAdmin);

function topSalary(salaries) {
    let entries = Object.entries(salaries);
    if (entries.length > 0) {
        let [maxName, maxSalary] = entries[0];
        for (let [name, salary] of entries) {
            if (salary > maxSalary) {
                maxSalary = salary;
                maxName = name;
            };
        };
        return maxName;
    } else {
        return null;
    };
};
salaries = {
  "John": 100,
  "Pete": 300,
  "Mary": 250
};
console.log(topSalary(salaries));


/*Date and time*/ console.log("\nDate and time:");
let d1 = new Date(2012, 1, 20, 3, 12);
console.log(d1);

function getWeekDay(date) {
    let days = ["SU", "MO", "TU", "WE", "TH", "FR", "SA"];
    return days[date.getDay()];
};
let date = new Date(2012, 0, 3);
console.log(getWeekDay(date));  

function getLocalDay(date) {
    let day = date.getDay();
    if (day == 0) return 7;
    return day;
};
date = new Date(2012, 0, 3);
console.log(getLocalDay(date));

function getDateAgo(date, days) {
    let cloned = new Date(date);
    cloned.setDate(date.getDate() - days);
    return cloned.getDate();
};
date = new Date(2015, 0, 2);
console.log(getDateAgo(date, 1)); 
console.log(getDateAgo(date, 2));
console.log(getDateAgo(date, 365));

function getLastDayOfMonth(year, month) {
    let date = new Date(year, month + 1, 0);
    return date.getDate();
};
console.log(getLastDayOfMonth(2012, 0));
console.log(getLastDayOfMonth(2012, 1));
console.log(getLastDayOfMonth(2013, 1));

function getSecondsToday() {
    let now = new Date();
    let today = new Date(now.getFullYear(), now.getMonth(), now.getDate());
    let dateDiff = now - today;
    return Math.round(dateDiff / 1000);
};
console.log(getSecondsToday());

function getSecondsToTomorrow() {
     let now = new Date();
    let tomorrow = new Date(now.getFullYear(), now.getMonth(), now.getDate() + 1);
    let dateDiff = tomorrow - now;
    return Math.round(dateDiff / 1000);
};
console.log(getSecondsToTomorrow());


/*JSON methods, to JSON*/ console.log("\nJSON methods, to JSON:");
user = {
  name: "John Smith",
  age: 35
};
let updatedUser = JSON.parse(JSON.stringify(user));
console.log(updatedUser);

let room = {
  number: 23
};
let meetup = {
  title: "Conference",
  occupiedBy: [{name: "John"}, {name: "Alice"}],
  place: room
};
room.occupiedBy = meetup;
meetup.self = meetup;
console.log( JSON.stringify(meetup, function replacer(key, value) {
    return (key != '' && value == meetup) ? undefined : value;
}));