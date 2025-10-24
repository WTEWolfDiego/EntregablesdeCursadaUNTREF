
/// <reference types="cypress" />

describe("Punto 3 - Saucedemo", () => {
    beforeEach(() => {
        cy.intercept({ method: 'GET', url: /\/event/ }, { statusCode: 200, body: '' }).as('EVENTO');

        cy.intercept({ method: 'POST', url: /events\.backtrace\.io\/.*/ }, { statusCode: 200, body: '' }).as('BACKTRACE');

        cy.intercept({ method: 'POST', url: /\/api\/.*submit.*/ }, { statusCode: 200, body: '' }).as('ANALYTICS');

        cy.on('uncaught:exception', (err, runnable) => {
            return false;
        });
    });

    it("Caso 1", () => {
        cy.visit("https://www.saucedemo.com/");
        cy.get("#user-name").type("standard_user");
        cy.get("#password").type("secret_sauce");
        cy.get("#login-button, button[type='submit']").click();

        cy.url().should("include", "/inventory.html");

        cy.get('.product_sort_container').then($sel => {
            const visibleText = 'Price (low to high)';
            const value = 'lohi';
            // buscar opción por texto exacto

            const hasVisible = $sel.find('option').toArray().some(opt => opt.innerText.trim() === visibleText);
            
            if (hasVisible) {
                cy.wrap($sel).select(visibleText);
            } else {
                cy.wrap($sel).select(value);
            }
        });

        cy.get('.inventory_item_price').should('have.length.greaterThan', 0);

        cy.get('.inventory_item_price').then($els => {
            const prices = Array.from($els).map(el =>
                parseFloat(el.innerText.replace(/[^0-9.]/g, ''))
            );

            for (let i = 1; i < prices.length; i++) {
                expect(prices[i]).to.be.at.least(prices[i - 1]);
            }
        });
    });

    it("Caso 2", () => {
        cy.visit("https://www.saucedemo.com/");
        cy.get("#user-name").type("standard_user");
        cy.get("#password").type("secret_sauce");
        cy.get("#login-button, button[type='submit']").click();

        cy.url().should("include", "/inventory.html");

        cy.get('.inventory_item').its('length').then((count) => {
            cy.get('.inventory_item').each($el => {
                cy.wrap($el).find('button').click();
            });

            cy.get('.shopping_cart_link').click();

            cy.get('.cart_item').should('have.length', count);

            cy.get('[data-test="checkout"], #checkout').click();

            cy.get('#first-name').type('Jack');
            cy.get('[data-test="continue"], #continue').click();
            cy.get('[data-test="error"], .error-message-container').should('contain.text', 'Error: Last Name is required');

            cy.get('#last-name').type('Sparrow');
            cy.get('[data-test="continue"], #continue').click();
            cy.get('[data-test="error"], .error-message-container').should('contain.text', 'Error: Postal Code is required');
        });
    });
    
    it("Caso 3", () => {
        cy.visit("https://www.saucedemo.com/");
        cy.get("#user-name").type("standard_user");
        cy.get("#password").type("secret_sauce");
        cy.get("#login-button, button[type='submit']").click();

        cy.url().should("include", "/inventory.html");

        cy.get('.inventory_item').first().find('button').click();

        cy.get('.shopping_cart_link').click();

        cy.get('.cart_item').first().find('button').click();

        cy.get('body').find('.cart_item').should('not.exist');

        cy.contains('button', /continue shopping/i).click();

        cy.get('.inventory_item').eq(0).find('button').click();
        cy.get('.inventory_item').eq(1).find('button').click();

        cy.get('.shopping_cart_link').click();

        cy.get('.cart_item').should('have.length', 2);
        cy.get('.cart_item .inventory_item_name').should('have.length', 2);

        cy.get('[data-test="checkout"], #checkout').click();
        cy.get('#first-name').type('Jack');
        cy.get('#last-name').type('Sparrow');
        cy.get('#postal-code').type('12345');
        cy.get('[data-test="continue"], #continue').click();

        cy.get('[data-test="finish"], #finish').click();

        cy.get('.complete-header').should('contain.text', 'Thank you for your order!');
    });
});
