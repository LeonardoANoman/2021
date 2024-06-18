let age: number;

age = 12;

let userName: string;

userName = "Leo";

let isInstructor: boolean;

isInstructor = false;

let hobbies: string[];

hobbies = ["Sports", "Cooking"];

type Person = {
  name: string;
  age: number;
};

let person: Person;

person = {
  name: "Leo",
  age: 25,
};

let people: Person[];

let course: string | number = "React - The Complete Guide";

course = 124;

function add(a: number, b: number) {
  return a + b;
}

function printOutput(value: any) {
  console.log(value);
}

function insertAtBegging<T>(array: T[], value: T) {
  const newArray = [value, ...array];
  return newArray;
}

const demoArray = [1, 2, 3];

const updatedArray = insertAtBegging(demoArray, -1);
const stringArray = insertAtBegging(["a", "b"], "c");
