# **Cypress Assignment – SauceDemo Automation**

## **Overview**
This project is for automating tests on SauceDemo using Cypress.  
It uses Page Object Model (POM) for better structure and Custom Commands for reusable steps.

## **Features**
- **Invalid Login** → Verify correct error message.  
- **Valid Login** → Verify landing on home page.  
- **Product Navigation** → Click product and verify product page opens.  
- **Custom Commands** → For common steps like login.  
- **POM** → Separate page classes for better maintainability.  

## **Project Structure**
cypress-assignment/
│

├── cypress/

│ ├── e2e/ # Test files (e.g., login.cy.js)

│ ├── pageObjects/ # POM classes (loginPage.js, inventoryPage.js)

│ ├── support/ # Custom commands & support setup

│ ├── screenshots/ # Auto-saved screenshots (on failure)

│ ├── videos/ # Auto-saved test run videos

│

├── OUTPUT TERMINAL SCREENSHOTS.pdf # Test run terminal output screenshots

├── .gitignore # Ignore node_modules, screenshots, videos

├── cypress.config.js # Cypress config file

├── package.json # Dependencies & scripts

├── package-lock.json # Auto-generated lock file

└── node_modules/ # Installed dependencies 


## **Note on node_modules/**
The `node_modules/` directory contains all project dependencies and is not uploaded to GitHub because it is large and can be regenerated.  

To install these dependencies, run:
npm install
This will recreate the `node_modules/` folder based on the `package.json` and `package-lock.json` files.
