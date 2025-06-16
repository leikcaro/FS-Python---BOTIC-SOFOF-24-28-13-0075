// -----------------------------
// Concepto de arreglos
// -----------------------------
let userData = ["Lewis", "Hamilton", "l.hamilton@oficina.com"];
console.log("Datos del usuario:", userData);

// -----------------------------
// Agregar elementos al arreglo
// -----------------------------
userData.push("piloto");
console.log("Después de agregar un elemento:", userData);

// -----------------------------
// Eliminar el último elemento
// -----------------------------
userData.pop();
console.log("Después de eliminar el último elemento:", userData);

// -----------------------------
// Actualizar elementos del arreglo
// -----------------------------
userData.push("piloto"); // agregamos nuevamente el pasatiempo
userData[3] = "Fotógrafo";
console.log("Después de actualizar el pasatiempo:", userData);

// -----------------------------
// Acceso por índice
// -----------------------------
console.log("Nombre:", userData[0]);
console.log("Apellido:", userData[1]);
console.log("Correo electrónico:", userData[2]);
console.log("Pasatiempo:", userData[3]);

// -----------------------------
// Propiedad .length
// -----------------------------
console.log("Cantidad de elementos en userData:", userData.length);
userData.pop();
console.log("Cantidad después de eliminar un elemento:", userData.length);

// -----------------------------
// Acceder al primer y último elemento
// -----------------------------
let comprasSemanaFeb15 = [4500, 1200, 2390, 8100, 1500];
console.log("El costo de la primera compra: $" + comprasSemanaFeb15[0]);

let númeroDeCompras = comprasSemanaFeb15.length;
let valorÚltimaCompra = comprasSemanaFeb15[númeroDeCompras - 1];
console.log("El costo de la última compra: $" + valorÚltimaCompra);

// -----------------------------
// Calcular el total de las compras
// -----------------------------
let total = 0;
for (let i = 0; i < comprasSemanaFeb15.length; i++) {
    total += comprasSemanaFeb15[i];
}
console.log("El gasto total fue: $" + total);

// -----------------------------
// Reglas básicas sobre arreglos
// -----------------------------
// Ejemplo de tipos variados
let arregloMixto = ["Texto", 123, true, [1, 2, 3]];
console.log("Arreglo con distintos tipos de datos:", arregloMixto);

console.log("Primer elemento:", arregloMixto[0]);
console.log("Cantidad de elementos:", arregloMixto.length);
