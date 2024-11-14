package src.main.java;

import src.main.java.managers.*;
import src.main.java.models.Lesson;

import java.util.Arrays;
import java.util.List;

public class OrganizationSystem {
    public static void main(String[] args) {
        // Initialize managers
        InstructorManager instructorManager = new InstructorManager();
        BookingManager bookingManager = new BookingManager();
        ClientManager clientManager = new ClientManager();
        ScheduleManager scheduleManager = new ScheduleManager();
        OfferingViewer offeringViewer = new OfferingViewer();
        LessonManager lessonManager = new LessonManager();

        // 1. Create and register a lesson
        System.out.println("Creating Lessons...");
        lessonManager.createLesson(1, "Yoga", "Group", 60);
        lessonManager.createLesson(2, "Swimming", "Private", 30);

        // 2. Register an instructor
        System.out.println("\nRegistering Instructor...");
        instructorManager.registerInstructor(1, "Grace", "514-123-4567", "Swimming", Arrays.asList("Montreal", "Laval"));

        // 3. Register a client
        System.out.println("\nRegistering Client...");
        clientManager.registerClient(1, "James", 32, null);

        // 4. Create a schedule for a Judo lesson
        System.out.println("\nCreating Schedule...");
        scheduleManager.createSchedule(1, "EV-Building Gym", "Judo", "Sunday", "12:00-13:00");

        // 5. Make a booking for the client
        System.out.println("\nMaking Booking...");
        bookingManager.makeBooking(1, 1, 1); // Example IDs for client and schedule

        // 6. View available offerings
        System.out.println("\nViewing Available Offerings...");
        offeringViewer.viewAvailableOfferings();

        // 7. Load and display lessons
        System.out.println("\nLoading and Displaying Lessons...");
        List<Lesson> lessons = lessonManager.loadLessons();
        for (Lesson lesson : lessons) {
            System.out.println(lesson);
        }
    }
}


