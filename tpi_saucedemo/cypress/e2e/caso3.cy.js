
// Conjunto de pruebas para SauceDemo
describe('SauceDemo - Ciclo Completo: Agregar, Remover y Checkout', () => {
    
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

    it('Caso 3: Verificar remoción de artículo y finalizar compra', () => {
        
        // --- 1. Agregar un elemento al carrito ---
        // Selector corregido: usamos .btn_inventory para encontrar el botón
        cy.get('.btn_inventory').first().click(); 
        
        // Verificar que el carrito tiene 1 artículo
        cy.get('.shopping_cart_badge').should('have.text', '1');

        // --- 2. Ir al carrito y remover el artículo ---
        cy.get('.shopping_cart_link').click();
        
        // Remover el artículo del carrito (el botón de remover tiene la clase .btn_secondary en esta vista)
        cy.get('.cart_list').find('.btn_secondary').click(); 

        // --- 3. Verificar que el sitio no tiene artículos agregados ---
        
        // Verificar que el badge del carrito desaparezca (no.exist)
        cy.get('.shopping_cart_badge').should('not.exist');
        
        // Verificar que la lista de ítems en el carrito esté vacía
        cy.get('.cart_list').find('.cart_item').should('not.exist');

        // --- 4. Ir a “Continue Shopping” ---
        cy.get('#continue-shopping').click();
        
        // Verificar que regresó al inventario
        cy.url().should('include', '/inventory.html');
        
        // --- 5. Agregar 2 elementos ---
        // Selector corregido: usamos .btn_inventory para encontrar los botones
        cy.get('.btn_inventory').eq(0).click(); 
        cy.get('.btn_inventory').eq(1).click();

        // --- 6. Ir al carrito y verificar que los 2 elementos existan ---
        cy.get('.shopping_cart_link').click();
        
        // Verificar que hay 2 elementos listados en el carrito
        cy.get('.cart_item').should('have.length', 2);

        // --- 7. Hacer el checkout ---
        cy.get('#checkout').click();
        
        // Llenar el formulario
        cy.get('#first-name').type('Fernando');
        cy.get('#last-name').type('Gomez');
        cy.get('#postal-code').type('1704');
        cy.get('#continue').click();
        
        // Verificar la URL de resumen
        cy.url().should('include', '/checkout-step-two.html');

        // --- 8. Finalizar la compra ---
        cy.get('#finish').click();

        // --- 9. Verificar que la compra fue realizada ---
        cy.url().should('include', '/checkout-complete.html');
        
        // Verificar el mensaje de confirmación final
        cy.get('.complete-header').should('contain', 'Thank you for your order!');
    });
});