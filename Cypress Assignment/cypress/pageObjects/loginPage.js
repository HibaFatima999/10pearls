class LoginPage {
  visit() {
    cy.visit('/');
  }

  enterUsername(username) {
    cy.get('#user-name').clear().type(username);
  }

  enterPassword(password) {
    cy.get('#password').clear().type(password);
  }

  clickLogin() {
    cy.get('#login-button').click();
  }

  login(username, password) {
    this.enterUsername(username);
    this.enterPassword(password);
    this.clickLogin();
  }

  getError() {
    return cy.get('[data-test="error"]');
  }
}

export default LoginPage;
