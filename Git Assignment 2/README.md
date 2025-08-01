# JMeter Assignment – Book API Test Plan

## Description
This JMeter test plan automates CRUD operations using the Simple Books API:

- **POST** request to create order using data from `books.csv`
- **GET** to verify created order and assert customer name
- **PATCH** to update the name
- **PUT** to update full order
- **DELETE** to remove the order
- Final **GET** to confirm deletion (expects `Not Found`)

## Files Included
- `JMeter_Collection.jmx` – The full JMeter test plan
- `books.csv` – CSV file with sample customer names

## API Used
[Simple Books API](https://simple-books-api.glitch.me)

## Prepared by:
**Hiba Fatima**  
QA Batch-05
