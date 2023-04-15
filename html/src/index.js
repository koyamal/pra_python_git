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
