// Prueba completa del Caso 2
describe('Caso 2 - SauceDemo', () => {
  it('Automatización completa:caso 2', () => {
    cy.visit('https://www.saucedemo.com/');
    cy.wait(3000);
// Ingreso las credenciales usuario y contraseña
    cy.get('[data-test="username"]').type('standard_user');
    cy.wait(2000); 
    cy.get('[data-test="password"]').type('secret_sauce');
    cy.wait(2000);

    cy.get('[data-test="login-button"]').click();
    cy.wait(4000); 

    // Agrego todos los productos al carrito
    cy.get('.inventory_item').each(($el) => {
      cy.wrap($el).find('button').contains('Add to cart').click();
      cy.wait(1000);
    });

    // Voy al carrito
    cy.get('.shopping_cart_link').click();
    cy.wait(3000);

    cy.url().should('include', '/cart.html');
    cy.wait(2000);

    // Verifico que estén todos los productos
    cy.get('.cart_item').should('have.length', 6);
    cy.wait(2500);

    // Voy al checkout
    cy.get('[data-test="checkout"]').click();
    cy.wait(3000);

    // Ingreso solo el nombre
    cy.get('[data-test="firstName"]').type('Ricardo');
    cy.wait(2000);

    cy.get('[data-test="continue"]').click();
    cy.wait(2500);

    // Verifico el error por falta de apellido
    cy.get('[data-test="error"]').should('contain', 'Error: Last Name is required');
    cy.wait(2000);

    // Ingreso el apellido
    cy.get('[data-test="lastName"]').type('Urbina');
    cy.wait(1500);

    cy.get('[data-test="continue"]').click();
    cy.wait(2000);

    // Verifico el error por falta de código postal
    cy.get('[data-test="error"]').should('contain', 'Error: Postal Code is required');
    cy.wait(3000);
  });
});
