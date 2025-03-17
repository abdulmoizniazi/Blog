const shoppingCart = [
    {name: 'Apple', price: 1.99, quantity: 3},
    {name: 'Apple', price: 1.99, quantity: 7},
    {name: 'Xiomi', price: 2.99, quantity: 2},
    {name: 'Samsung', price: 3.99, quantity: 1},
    {name: 'Tesla', price: 3.99, quantity: 1},
    {name: 'Tesla', price: 4.99, quantity: 4},
    {name: 'Nokia', price: 4.99, quantity: 4},
];

const products = shoppingCart.reduce((productGroup, product) => {
    const name = product.name;
    if (!productGroup[name]) {
        productGroup[name] = [];
    }
    productGroup[name].push(product);
    return productGroup;
}, {});

const totalAmount = shoppingCart.reduce((prodGroup, prod) => {
    const name = prod.name;
    if (!prodGroup[name]) {
        prodGroup[name] = {quantity:0, price:prod.price}; 
    }
    prodGroup[name].quantity += prod.quantity;
    
    return prodGroup;
}, {}); // Initialize as an object {}

for (name in totalAmount){
    totalAmount[name].totalCostie = (totalAmount[name].quantity * totalAmount[name].price).toFixed(2)
}

console.log(products);
console.log(totalAmount);
