const object ={
    a: 1,
    b: 2,
}
const {a, b =2} = object;
console.log(a,b);
console.log("object값 출력: ",object.a, object.b);
const animal ={
    name : "멍멍이",
    type : "개"   
}
const { name : nickname } = animal;
console.log( name, nickname);
const id =1;
const product = "구두";

const goods1 = {
    id : id ,
    product : product ,
}

const goods2 = {
    id ,
    product,
}
// console.log(goods2)

console.log(new Date()); 
// const [data, month,year]=dataInfo(new DataTransfer());