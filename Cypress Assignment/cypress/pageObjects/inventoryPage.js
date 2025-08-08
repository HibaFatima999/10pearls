class InventoryPage {
  verifyInventoryPage() {
    cy.url().should('include', '/inventory.html');
  }

  selectProduct(productName) {
    cy.contains(productName).click();
  }

  verifyProductPage() {
    cy.url().should('include', '/inventory-item.html');
  }
}

export default InventoryPage;
