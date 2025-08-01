# Postman Assignment – Simple Books API

This folder contains the completed Postman collection and environment setup for **Assignment No. 1** using the [Simple Books API](https://simple-books-api.glitch.me).

---

## Features Covered

- [x] **GET**, **POST**, **PATCH**, **DELETE**, **PUT** methods used 
- [x] **Base URL** set as a variable and reused
- [x] **Random data** generated in pre-request script
- [x] **Chai assertion** checks using Postman test scripts
- [x] **Intentionally failing test** included
- [x] **Environment variables** created and reset during execution
- [x] **Chained requests** using variables from previous responses

---

## Files Included

| File Name                  | Description                              |
|--------------------------------------------|--------------------------|
| `Postman_Collection.json`  | Main Postman collection                  |
| `Postman_Environment.json` | Postman environment with base URL        |

---

## Notes

- `PUT` request is a dummy placeholder since the API doesn’t officially support it.
- Random names like `Ali`, `Sara`, etc. are used as customer names during order placement.
- Access token is generated via `POST Get Access Token` and reused in following requests.

---

## Prepared by:
**Hiba Fatima**  
QA Batch-05