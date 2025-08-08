import LoginPage from '../pageObjects/loginPage';
import InventoryPage from '../pageObjects/inventoryPage';

const loginPage = new LoginPage();
const inventoryPage = new InventoryPage();

describe('SauceDemo Tests', () => {
  beforeEach(() => {
    loginPage.visit();
  });

  it('Invalid login shows error message', () => {
    loginPage.login('invalid_user', 'invalid_pass');
    loginPage.getError().should('contain', 'Username and password do not match');
  });

  it('Valid login and visit product', () => {
    loginPage.login('standard_user', 'secret_sauce');
    inventoryPage.verifyInventoryPage();
    inventoryPage.selectProduct('Sauce Labs Backpack');
    inventoryPage.verifyProductPage();
  });
});
