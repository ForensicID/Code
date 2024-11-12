// String
const tahunIni = new Date().getFullYear();
const kata = `Sakmeniko tahun ${tahunIni}`;
console.log(kata);

// Number
const hasil = 50 / 5;
console.log(hasil);

const kocak = Number('Dicoding');
console.log(kocak);

// Boolean
const dadi = true;
const rampung = false;
console.log(dadi, rampung);

const luwihGede = 5 < 10;
console.log(luwihGede);

// Null Nilai Kosong
let pesen = null;
console.log(pesen);

let raono;
console.log(raono);

const jeneng1 = { first: 'Dicoding', last: 'null'}
const jeneng2 = { first: 'Dicoding', last: 'undefined'}

console.log(JSON.stringify(jeneng1));
console.log(JSON.stringify(jeneng2));
