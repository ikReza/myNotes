const printPyramid = (limit) => {
  for (let i = 1; i < 2 * limit; i++) {
    console.log(`${i > limit ? 2 * limit - i : i} `);
  }
};

let number = 9;

// printPyramid(parseInt(number));

const reverseMe = (test) => {
  let step1 = test.split("");
  step1;
  let step2 = step1.reverse();
  step2;
  let step3 = step2.join("");
  step3;
};

let str = "Hello bro";

reverseMe(str);

const reverseMe2 = (test) => {
  return [...test].reverse().join("");
};

console.log(reverseMe2(str));

const reverseLine = (test) => {
  step1 = test.split(" ").reverse().join(" ");
  step1;
};

reverseLine("He is good");
