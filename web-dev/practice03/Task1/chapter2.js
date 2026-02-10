/*Coding style*/ console.log("Coding style:");

/*
function pow(x,n)
{
  let result=1;
  for(let i=0;i<n;i++) {result*=x;}
  return result;
}

let x=prompt("x?",''), n=prompt("n?",'')
if (n<=0)
{
  alert(`Power ${n} is not supported, please enter an integer number greater than zero`);
}
else
{
  alert(pow(x,n))
}
*/

function pow(x, n) {
    let result = 1;

    for (let i = 0; i < n; i++) {
        result *= x;
    }

    return result;
}

let x = 2;
let n = 5;

if (n <= 0) {
    console.log(`Power ${n} is not supported,
    please enter an integer number greater than zero`);
} else {
    console.log( pow(x, n) );
}


