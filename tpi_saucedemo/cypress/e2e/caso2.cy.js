
// Organizar el conjunto de pruebas para SauceDemo
describe('SauceDemo - Carrito y Validación de Checkout', () => {
    
    // Loguearse antes de cada test
    beforeEach(() => {
        // Comando para visitar la URL
        cy.visit('https://www.saucedemo.com/');
        
        // Logueo
        cy.get('#user-name').type('standard_user');
        cy.get('#password').type('secret_sauce');
        cy.get('#login-button').click();
        
        // Verificar que el login fue exitoso
        cy.url().should('include', '/inventory.html');
    });

    it('Caso 2: Agregar productos, ir al checkout y validar errores de formulario', () => {
        
        // --- 1. Incorporar al carrito todos los elementos ---
        // Seleccionar todos los botones y hacer clic en ellos
        cy.get('.btn_inventory').click({ multiple: true });
        
        // Verificar que el icono del carrito muestre el total (6)
        cy.get('.shopping_cart_badge').should('have.text', '6');

        // --- 2. Ir al carrito y verificar elementos ---
        cy.get('.shopping_cart_link').click();
        
        // Verificar que la URL es la del carrito
        cy.url().should('include', '/cart.html');
        
        // Verificar que hay 6 elementos listados
        cy.get('.cart_item').should('have.length', 6);

        // --- 3. Ir al checkout ---
        cy.get('#checkout').click();
        
        // Verificar que la URL es la del checkout
        cy.url().should('include', '/checkout-step-one.html');

        // --- 4. Validar error de Apellido ---
        // Ingresar el nombre
        cy.get('#first-name').type('Juan');
        cy.get('#continue').click();
        
        // Verificar el mensaje de error de Apellido
        cy.get('.error-message-container').should('contain', 'Error: Last Name is required');

        // --- 5. Validar error de Código Postal ---
        // Ingresar el apellido
        cy.get('#last-name').type('Perez');
        cy.get('#continue').click();
        
        // Verificar el mensaje de error de Código Postal
        cy.get('.error-message-container').should('contain', 'Error: Postal Code is required');

    });
});