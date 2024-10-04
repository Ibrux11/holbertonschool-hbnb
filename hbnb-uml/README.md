# HBnB Project: Comprehensive Technical Blueprint Documentation

## Introduction

The HBnB project is a web-based platform designed to allow users to book accommodations, review properties, and manage place listings. This technical document serves as a blueprint for implementing the system by detailing the system architecture, core business logic, and API interactions. It consolidates various diagrams, including high-level package diagrams, class diagrams for business logic, and sequence diagrams illustrating API flows. The objective is to guide the development process, ensuring that the system is built according to a well-defined architecture.

This document will act as a reference for developers throughout the project implementation, helping ensure that the platform remains scalable, maintainable, and robust.

---

## Table of Contents

1. Introduction
2. High-Level Architecture
   - Overview of Layered Architecture
   - High-Level Package Diagram
3. Business Logic Layer
   - Overview of Core Services
   - Detailed Class Diagram with Explanations
4. API Interaction Flow
   - Sequence Diagrams for Key API Operations
     - User Registration Flow
     - Review Submission Flow
     - Place Creation Flow
     - Fetching a List of Places Flow
5. Conclusion

---

## 1. High-Level Architecture

### Overview of Layered Architecture

The HBnB platform adopts a multi-layered architecture to separate concerns and ensure scalability and maintainability. The architecture consists of three primary layers:

- **Presentation Layer**: Responsible for interacting with the user via the web interface and API calls. It handles user requests and displays information.
- **Business Logic Layer**: The core of the system where the main business operations occur, including booking management, payment processing, and user authentication.
- **Persistence Layer**: Manages the system's interaction with the database, ensuring that data is stored and retrieved correctly.

Each layer interacts with the others in a well-defined manner, with the presentation layer forwarding user actions to the business logic layer, which then communicates with the persistence layer for data access.

### Explanation

- **Presentation Layer**:
  - **WebUI**: This component represents the interface users interact with, allowing them to browse listings, manage bookings, and leave reviews.
  - **APIController**: The API Controller manages requests coming from external applications (like mobile apps) and handles communication between the UI and the business logic.

- **Business Logic Layer**: This layer contains the essential services that manage business operations:
  - **BookingService**: Manages all activities related to booking properties, including creation, updates, and cancellation of bookings.
  - **PaymentService**: Responsible for handling payments and issuing refunds.
  - **UserService**: Manages user authentication, registration, and profile updates.
  - **ReviewService**: Allows users to submit, view, and delete reviews for properties.
  - **ListingService**: Manages property listings, including creation, modification, and search functionality.

- **Persistence Layer**: This layer contains repositories that interact with the database, ensuring data consistency:
  - **UserRepository**: Manages the storage of user details, including credentials and roles.
  - **ListingRepository**: Stores property listings and their associated data.
  - **BookingRepository**: Manages data related to bookings.
  - **PaymentRepository**: Handles the storage of payment transaction details.
  - **ReviewRepository**: Manages user reviews for listings.

---

## 2. Business Logic Layer

The Business Logic Layer is responsible for processing user actions and managing key workflows such as bookings, payments, user management, and reviews. It abstracts the complexity of data operations and provides clearly defined services for handling requests.

### Detailed Class Diagram for Business Logic

This diagram outlines the core services and their interactions within the business logic layer. Each service is designed to be modular, focusing on a specific domain of the application.

### Key Components and Design Decisions

- **BookingService**:
  - **Purpose**: Manages the creation, update, and cancellation of bookings. Ensures that listings are available and processes any booking updates.
  - **Key Methods**: 
    - `createBooking()`: Creates a new booking.
    - `updateBooking()`: Updates an existing booking.
    - `cancelBooking()`: Cancels a booking.

- **PaymentService**:
  - **Purpose**: Handles all payment-related transactions, including payment processing and issuing refunds.
  - **Key Methods**: 
    - `processPayment()`: Processes a booking payment.
    - `issueRefund()`: Issues a refund for a canceled booking.

- **ListingService**:
  - **Purpose**: Allows hosts to create and manage property listings, and allows users to search for listings based on various criteria (location, price, etc.).
  - **Key Methods**: 
    - `createListing()`: Allows hosts to add a new property listing.
    - `searchListings()`: Enables users to search for listings.

- **ReviewService**:
  - **Purpose**: Manages the reviews that users leave on property listings, allowing them to submit, view, or delete reviews.
  - **Key Methods**: 
    - `submitReview()`: Adds a review for a property.
    - `removeReview()`: Deletes a user’s review.

- **UserService**:
  - **Purpose**: Manages user authentication, registration, and profile updates.
  - **Key Methods**: 
    - `registerUser()`: Registers a new user.
    - `loginUser()`: Authenticates an existing user.

---

## 3. API Interaction Flow

This section provides sequence diagrams that illustrate how the system processes key user interactions through the API. These diagrams showcase the flow of data between the API, business logic, and persistence layers during typical operations like user registration, review submission, and listing creation.

---

#### Diagram: User Registration Sequence Diagram

### Explanation

1. **API Call**: A user submits a registration request through the API with their username, email, and password.
2. **Validation**: The API validates the user input to ensure all required fields are provided and formatted correctly.
3. **Business Logic**: The `UserService` processes the request and registers the user if validation passes.
4. **Database**: The `UserRepository` saves the new user details in the database.
5. **Response**: A success message is returned to the API, which then responds to the user with a status message.

---

### 3.2 Review Submission Flow



#### Diagram: Review Submission Sequence Diagram



### Explanation

1. **API Call**: A user submits a review for a property they booked through the API.
2. **Validation**: The API validates the review data, including user ID, property ID, and rating.
3. **Business Logic**: The `ReviewService` processes the review and checks if the user is allowed to submit the review.
4. **Database**: The `ReviewRepository` stores the review data in the database.
5. **Response**: The API returns a success message to the user, confirming that their review has been submitted.

---

### 3.3 Place Creation Flow



#### Diagram: Place Creation Sequence Diagram



### Explanation

1. **API Call**: A host submits a request to create a new place listing through the API.
2. **Validation**: The API checks that all required fields (name, address, category) are valid and complete.
3. **Business Logic**: The `ListingService` processes the request and ensures that the listing is valid and there are no conflicts.
4. **Database**: The new place listing is saved to the database via the `ListingRepository`.
5. **Response**: A success message is returned to the host, confirming the place has been created.

---

### 3.4 Fetching a List of Places Flow

#### Diagram: Fetching a List of Places Sequence Diagram

### Explanation

1. **API Call**: A user sends a request to fetch available places based on filters like location and price.
2. **Validation**: The API validates the search criteria.
3. **Business Logic**: The `ListingService` retrieves a list of places that match the search criteria.
4. **Database**: The listings are fetched from the `ListingRepository`.
5. **Response**: The API sends the list of available places to the user, displaying the results in the UI.

By Ibrahim Hassan Ali