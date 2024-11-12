// Change data type
// Change to String
const nomor = 123;
const boolean = true;
const strnomor = String(nomor);
const strboolean = String(boolean);
console.log(strnomor)
console.log(strboolean)

// Change to Number
const stringNomer = '123';
const stringFloat = '3.14';
const boolBoolean = true;
const numFromString = Number(stringNomer);
const floatFromString = Number(stringFloat);
const numFromBoolean = Number(boolBoolean);
console.log(numFromString);
console.log(floatFromString);
console.log(numFromBoolean);
// INTEGER
const berat = '100kg';
const tinggi = '180cm';
const intFromBerat = parseInt(berat);
const intFromTinggi = parseInt(tinggi);
console.log(intFromBerat);
console.log(intFromTinggi);
// FLOAT
const panjang = '25.60cm';
const lebar = '30.55cm';
const floatFromPanjang = parseFloat(panjang);
const floatFromLebar = parseFloat(lebar);
console.log(floatFromPanjang);
console.log(floatFromLebar);

// Change to Boolean
const nomere = 123;
const setring = 'Dicoding';
const kosong = null;
const boolFromNomere = Boolean(nomere);
const boolFromSetring = Boolean(setring);
const boolFromKosong = Boolean(kosong);
console.log(boolFromNomere);
console.log(boolFromSetring);
console.log(boolFromKosong);


// Convertion Implisit
const umur = 25;
const mesen = 'Umur Kulo: ' + umur;
console.log(mesen);

const strNowmer = '123';
const dadine = strNowmer * 2;
console.log(dadine);

const bool = true;
const dadiwae = 1 + bool;
console.log(dadiwae);
