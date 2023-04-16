const a = 1;

console.log(a);

let b = 2;
console.log(b);
b = 3;
console.log(b);

const obj = {
    a: 1,
    b: 2,
    c: 3,
    d: 4
}

console.log(obj.a);
console.log(obj.d);

const array = [1, 2, 3, 4]
console.log(array);
console.log(array[1]);

function square(a) {
    return a * a;
}

console.log(square(10));

const squareB = function(a){
    console.log(a * a);
}

squareB(11);

const squareC = (a) => {
    console.log(a * a);
}

squareC(13);

console.log(1 > 2);
console.log(1 < 2);
console.log(1 === 2);

const flagIf = true
if(flagIf){
    console.log("Correct");
} else {
    console.log("InCorrect");
}

const greeting = flagIf? "Good Morning": "Hello";
console.log(greeting);

const numbers = [1, 2, 3, 4];

const number10 = numbers.map((number, index) => {
    console.log(`index: ${index}`);
    return number * 100;
})

console.log(number10);

numbers.forEach((num) => {
    console.log(num);
});

const obj16 = {name: "Jhone", age: 38, contory: "USA"};

const { name, contory} = obj16;

console.log(`${name} is from ${contory}.`);

const array16 = [1, 2, 3, 3, 5, 5, 6, 7];

const array16_ = [...array16];
array16_.push(14);

console.log(array16);
console.log(array16_);

const outputForEach = array16.forEach((dat) => {
    console.log(dat);
    return dat;
})

console.log("outputForEach", outputForEach);

const array16_10 = array16.map((dat) => {
    return dat * 10;
})
console.log(array16_10);

const array16_even = array16.filter((dat) => {
    return dat % 2 === 0;
})

console.log(array16_even);

const array16_even_first = array16.find((dat) => {
    return dat % 2 === 0;
})

console.log(array16_even_first);


const persons = [
    {name: "Jhone", age: 38, contory: "USA"},
    {name: "Taro", age: 40, contory: "Japan"},
    {name: "Jiro", age: 32, contory: "Japan"},
    {name: "Tom", age: 12, contory: "USA"},
    {name: "Kim", age: 22, contory: "KOREA"},
    {name: "Li", age: 43, contory: "CHINA"},
]

const usaPersons = persons.filter((person) => {
    return person.contory === "USA";
})

console.log(usaPersons);

const japanPersons = persons.filter((person) => {
    return person.contory === "Japan";
})

console.log(japanPersons);
