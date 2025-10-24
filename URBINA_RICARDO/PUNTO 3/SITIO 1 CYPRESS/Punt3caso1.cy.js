// Prueba básica de login y orden por precio en Swag Labs
describe('Login y orden por precio en Swag Labs', () => {
  it('Chequea si los precios están en orden ascendente', () => {
    cy.visit('https://www.saucedemo.com/')
    cy.wait(3000) // espero 3 segundos para que cargue bien el sitio

    // ingreso usuario y contraseña 
    cy.get('[data-test="username"]').type('standard_user')
    cy.wait(4000)
    cy.get('[data-test="password"]').type('secret_sauce')
    cy.wait(4000)
    cy.get('[data-test="login-button"]').click()
    cy.wait(2000)

    // me fijo que haya ingresado a la pagina inicial
    cy.url().should('include', '/inventory.html')
    cy.wait(5000)

    // selecciono el filtro de precios de menor a mayor
    cy.get('select.product_sort_container', { timeout: 10000 })
      .should('be.visible')
      .select('Price (low to high)')
    cy.wait(5000)

    // ahora reviso si los precios están realmente ordenados
    cy.get('.inventory_item_price').then(($prices) => {
      cy.wait(4000) 

      // convierto los precios a números (sacando el $)
      const precios = [...$prices].map(el => parseFloat(el.innerText.replace('$', '')))

      // ordeno los precios para comparar
      const ordenado = [...precios].sort((a, b) => a - b)

      // comparo si están igual (o sea, si ya estaban ordenados)
      expect(precios).to.deep.equal(ordenado)
    })
  })
})
