//Este caso lo dividi en 4 bloques, me resulto mucho mas facil automatizar e ir corrigiendo los errores


//Bloque 1: Login y agregar un producto al carrito

describe('Caso 3 - SauceDemo', () => {
  it('Login, agrega un producto y accede al carrito', () => {
    cy.visit('https://www.saucedemo.com/');
    cy.wait(3000);
    cy.get('[data-test="username"]').type('standard_user');
    cy.wait(2000); 
    cy.get('[data-test="password"]').type('secret_sauce');
    cy.wait(2000);
    cy.get('[data-test="login-button"]').click();
    cy.wait(3500); 

    // se agrega el producto al carrito

    cy.get('.inventory_item').first().find('button').contains('Add to cart').click();
    cy.wait(2000); 
    cy.get('.shopping_cart_link').click();
    cy.wait(3000); 

  // verificacion de que está en la página del carrito
    cy.url().should('include', '/cart.html');
    cy.wait(2000); 
  });
});

//Bloque 2: Agregar y remover producto
describe('Bloque 2', () => {
  it('Agrega y remueve un artículo, verifica el carrito vacío y vuelve a la tienda', () => {
    cy.visit('https://www.saucedemo.com/');
    cy.wait(3000);
    cy.get('[data-test="username"]').type('standard_user');
    cy.wait(2000);
    cy.get('[data-test="password"]').type('secret_sauce');
    cy.wait(2000);
    cy.get('[data-test="login-button"]').click();
    cy.wait(3500);
//se agrega el producto al carrito
    cy.get('.inventory_item').first().find('button').contains('Add to cart').click();
    cy.wait(2000);
    cy.get('.shopping_cart_link').click();
    cy.wait(3000);
//se elimina el producto del carrito y verifica que este vacio
    cy.get('.cart_item').first().find('button').contains('Remove').click();
    cy.wait(2000);
    cy.get('.cart_item').should('not.exist');
    cy.wait(2500);

//vuelve a la tienda y verifica la url correcta
    cy.get('[data-test="continue-shopping"]').click();
    cy.wait(3000);
    cy.url().should('include', '/inventory.html');
    cy.wait(2000);
  });
});

//Bloque 3: Agregar dos productos
describe('Bloque 3', () => {
  it('Agrega dos productos y verifica que estén en el carrito', () => {
    cy.visit('https://www.saucedemo.com/');
    cy.wait(3000);
    cy.get('[data-test="username"]').type('standard_user');
    cy.wait(2000);
    cy.get('[data-test="password"]').type('secret_sauce');
    cy.wait(2500);
    cy.get('[data-test="login-button"]').click();
    cy.wait(3500);

// El usuario agrega dos productos y accede al carrito
    cy.get('.inventory_item').eq(0).find('button').contains('Add to cart').click();
    cy.wait(2000);
    cy.get('.inventory_item').eq(1).find('button').contains('Add to cart').click();
    cy.wait(2000);
    cy.get('.shopping_cart_link').click();
    cy.wait(3000);

//confirmacion que hay dos productos en el carrito
    cy.get('.cart_item').should('have.length', 2);
    cy.wait(2000);
  });
});

//Bloque 4: Checkout y confirmación
describe('Bloque 4', () => {
  it('Realiza el checkout, finaliza la compra y verifica confirmación', () => {
    cy.visit('https://www.saucedemo.com/');
    cy.wait(3000);
    cy.get('[data-test="username"]').type('standard_user');
    cy.wait(2000);
    cy.get('[data-test="password"]').type('secret_sauce');
    cy.wait(2000);
    cy.get('[data-test="login-button"]').click();
    cy.wait(3500);

// El usuario agrega dos productos y accede al carrito
    cy.get('.inventory_item').eq(0).find('button').contains('Add to cart').click();
    cy.wait(2000);
    cy.get('.inventory_item').eq(1).find('button').contains('Add to cart').click();
    cy.wait(2000);
    cy.get('.shopping_cart_link').click();
    cy.wait(3000);

// se inicia el checkout y se completa con los datos
    cy.get('[data-test="checkout"]').click();
    cy.wait(2500);
    cy.get('[data-test="firstName"]').type('Ricardo');
    cy.wait(1500);
    cy.get('[data-test="lastName"]').type('Urbina');
    cy.wait(1500);
    cy.get('[data-test="postalCode"]').type('1712');
    cy.wait(2000);
    cy.get('[data-test="continue"]').click();
    cy.wait(2500);

//Se finaliza la compra y muestra de confirmacion
    cy.get('[data-test="finish"]').click();
    cy.wait(3000);
    cy.get('.complete-header').should('contain', 'Thank you for your order!');
    cy.wait(2000);
  });
});
