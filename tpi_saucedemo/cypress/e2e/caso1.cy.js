
// Organiza el conjunto de pruebas para SauceDemo
describe('SauceDemo - Ordenamiento de Productos', () => {
    
    it('Caso 1: Logueo y Verificación de orden por precio (bajo a alto)', () => {
        
        // --- 1. Logueo al sitio como usuario standard_user ---
        // Comando para visitar la URL
        cy.visit('https://www.saucedemo.com/');
        
        // Ingresar Usuario y verificar valor
        cy.get('#user-name').type('standard_user');
        cy.get('#password').type('secret_sauce');
        cy.get('#login-button').click();
        
        // Verificar redirección
        cy.url().should('include', '/inventory.html');
        
        // --- 2. Ordenar los elementos por “price (low to high)” ---
        
        // Ejecución de la selección usando el valor interno 'lohi'
        cy.get('.product_sort_container')
          .select('lohi'); 
          
        // Verificación del valor seleccionado (soluciona el error de desacoplamiento del DOM)
        cy.get('.product_sort_container') 
          .should('have.value', 'lohi');

        // --- 3. Verificar que los elementos estén ordenados ---
        
        // Obtener todos los precios de los productos visibles
        cy.get('.inventory_item_price')
          .then($precios => {
            
            // Mapear los elementos del DOM a un arreglo de números (precio)
            const preciosNumericos = $precios
              .map((index, elemento) => {
                // Obtener el texto, eliminar el símbolo '$' y convertir a número
                return parseFloat(Cypress.$(elemento).text().replace('$', ''));
              })
              .get();
            
            // Crear una copia del arreglo y ordenar manualmente
            const preciosOrdenados = [...preciosNumericos].sort((a, b) => a - b);
            
            // Comparar el arreglo del sitio con el arreglo ordenado manualmente
            expect(preciosNumericos, 'Verificar que el arreglo del sitio sea igual al arreglo ordenado').to.deep.equal(preciosOrdenados);
        });

    });
});