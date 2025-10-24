
/// <reference types="cypress" />

describe('Punto 3 - PokeAPI', () => {
    
    it('Caso 1', () => {
        cy.request('GET', 'https://pokeapi.co/api/v2/berry/1').then((resp) => {
            expect(resp.status).to.equal(200);
            const body = resp.body;
            expect(body).to.have.property('size', 20);
            expect(body).to.have.property('soil_dryness', 15);
            // firmness es un objeto con name
            expect(body.firmness).to.have.property('name', 'soft');
        });
    });

    it('Caso 2', () => {
        // Traigo berry/1 primero para comparar
        cy.request('GET', 'https://pokeapi.co/api/v2/berry/1').then((r1) => {
            expect(r1.status).to.equal(200);
            const size1 = r1.body.size;
            const soil1 = r1.body.soil_dryness;

            cy.request('GET', 'https://pokeapi.co/api/v2/berry/2').then((r2) => {
                expect(r2.status).to.equal(200);
                const b2 = r2.body;
                expect(b2.firmness).to.have.property('name', 'super-hard');
                expect(b2.size).to.be.greaterThan(size1);
                expect(b2.soil_dryness).to.equal(soil1);
            });
        });
    });

    it('Caso 3', () => {
        cy.request('GET', 'https://pokeapi.co/api/v2/pokemon/pikachu/').then((resp) => {
            expect(resp.status).to.equal(200);
            const p = resp.body;
            expect(p).to.have.property('base_experience');
            expect(p.base_experience).to.be.greaterThan(10);
            expect(p.base_experience).to.be.lessThan(1000);

            // types es un array de objetos { slot, type: { name, url } }
            const types = p.types.map(t => t.type.name);
            expect(types).to.include('electric');
        });
    });
});
