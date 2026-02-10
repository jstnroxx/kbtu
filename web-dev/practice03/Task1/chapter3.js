/*Objects*/ console.log("Objects:");
let user = {};
user.name = "John";
user.surname = "Smith";
user.name = "Pete"; 
delete user.name;

function isEmpty(obj) {
    for (let key in obj) {
        return true;
    }
    return false;
};

let salaries = {
    John: 100,
    Ann: 160,
    Pete: 130
};

let total = 0;
for (let key in salaries) {
    total += salaries[key];
}
console.log(total);

let menu = {
    width: 200,
    height: 300,
    title: "My menu"
};

function multiplyNumeric(obj) {
    for (let key in obj) {
        obj[key] = (typeof(obj[key]) == "number") ? obj[key] *= 2 : obj[key];
    }
};

console.log(menu);
multiplyNumeric(menu);
console.log(menu);


/*Object methods, "this"*/ console.log("\nObject methods:");
let calculator = {
    read(_a, _b) {
        this.a = _a;
        this.b = _b;
    },
    sum() {
        return this.a + this.b;
    },
    mul() {
        return this.a * this.b;
    }
};

calculator.read(5, 5);
console.log(calculator.sum());
console.log(calculator.mul());

let ladder = {
  step: 0,
  up() {
    this.step++;
    return this;
  },
  down() {
    this.step--;
    return this;
  },
  showStep: function() {
    console.log( this.step );
    return this;
  }
};

ladder.up().up().down().showStep().down().showStep();


/*Constructor, operator "new"*/ console.log("\nConstructor, 'new':");
let obj = {};

function A() { return obj; }
function B() { return obj; }

console.log( new A() == new B() );

function Calculator() {
    this.read = function(_a, _b) {
        this.a = _a;
        this.b = _b;
    };
    this.sum = function() {
        return this.a + this.b;
    };
    this.mul = function() {
        return this.a * this.b;
    };
};

calculator = new Calculator();
calculator.read(5, 4);

console.log( "Sum = " + calculator.sum() );
console.log( "Mul = " + calculator.mul() );

function Accumulator(_startingValue) {
    this.value = _startingValue;
    this.read = function(_amount) {
        this.value += _amount;
    };
};

let accumulator = new Accumulator(1);
accumulator.read(2);
accumulator.read(5);
console.log(accumulator.value);


