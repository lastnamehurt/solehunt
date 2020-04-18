# solehunt

## Tech Stack
- Django
- Python 3.8  
- React
- GraphQL
- Cypress

## System Design
### Solehunt uses a **Layered Architecture** pattern with the below layers: 

#### Repos

Domain layer. Each repo is related to an individual *model*

#### Services

API layer. Biz logic goes here

#### Usecases

Simplified, higher-level acceptance layer. Serves as an API for the Frontend

#### Frontend 

React. Using GraphQL with Graphine to create Queries within Django

### Tests

Aside from required `unit` tests, the important `integration` tests can be found at `subscribers/tests/integration
/test_acceptance` since a `Subscriber` is the primary driver of this app.