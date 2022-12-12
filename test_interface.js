const houses = [
    ['206', '2', '0', 'Ouest', '170511.48186231407'],
    ['187', '1', '1', 'Est', '170491.68708712346'],
    ['194', '3', '1', 'Est', '170531.209714976'],
];

describe('Case 1', () => {
    it('should predict house 1', () => {
        cy.visit('/');

        const [size, nb_rooms, garden, _, price] = houses[0];

        cy.get('input[aria-label="Taille maison"]').type(size);
        cy.get('input[aria-label="Nombre de chambre"]').type(nb_rooms);
        cy.get('input[aria-label="Y a un jardin"]').type(garden);

        cy.get('#result').invoke('text').should('eq', price);
    });

    it('should predict all remaining houses', () => {
        houses.slice(1).forEach(([size, nb_rooms, garden, _, price]) => {
            cy.visit('/');

            cy.get('input[aria-label="Taille maison"]').type(size);
            cy.get('input[aria-label="Nombre de chambre"]').type(nb_rooms);
            cy.get('input[aria-label="Y a un jardin"]').type(garden);

            cy.get('#result').invoke('text').should('eq', price);
        });
    });
});
