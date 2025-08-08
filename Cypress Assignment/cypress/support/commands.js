Cypress.Commands.add('login', (username, password) => {
  cy.get('#user-name').clear().type(username);
  cy.get('#password').clear().type(password);
  cy.get('#login-button').click();
});
