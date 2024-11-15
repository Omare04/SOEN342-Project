# SOEN342 Project - Lesson Booking System

## Overview

This project is a **Lesson Booking System** designed to support an organization offering group or private lessons (e.g., yoga, swimming) to clients. The system manages lesson schedules, instructor registration, client bookings, and availability. It includes features such as concurrency controls for readers and writers, which ensures safe access to data.

### Key Features
- **Lesson Management**: Create and manage various types of lessons.
- **Instructor Management**: Register seasonal instructors and set their availability.
- **Client Registration**: Register clients and allow them to book lessons.
- **Scheduling and Bookings**: Schedule lessons at specific locations and allow clients to make bookings.
- **Concurrency Control**: Ensure mutual exclusion for data access by using reader-writer locks.

## Project Structure

The project consists of the following main components:

- **models/**: Contains data models representing entities in the system (e.g., `Lesson`, `Instructor`, `Client`, `Schedule`, `Booking`).
- **managers/**: Contains manager classes responsible for handling the business logic and file operations (e.g., `InstructorManager`, `BookingManager`, `ScheduleManager`).
- **data/**: Directory containing CSV files for data persistence (e.g., `Instructors.csv`, `Clients.csv`, `Lessons.csv`).
- **OrganizationSystem.java**: The main entry point of the program, demonstrating the functionalities provided by the system.

## Getting Started

### Prerequisites

- **Java**: Ensure you have Java (JDK 11 or later) installed on your machine.
- **Git**: Required for cloning the repository and managing version control.

### Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Omare04/SOEN342-Project.git
