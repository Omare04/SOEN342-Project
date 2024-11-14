package src.main.java.managers;

import java.io.IOException;
import java.util.List;

public class OfferingViewer {
    private static final String SCHEDULES_FILE = "src/data/Schedules.csv";
    private static final String BOOKINGS_FILE = "src/data/Bookings.csv";

    public void viewAvailableOfferings() {
        try {
            List<String[]> schedules = CSVManager.readCSV(SCHEDULES_FILE);
            List<String[]> bookings = CSVManager.readCSV(BOOKINGS_FILE);

            System.out.println("Available Offerings:");
            for (String[] schedule : schedules) {
                String scheduleId = schedule[0];
                boolean isAvailable = true;

                // Check if this schedule has any bookings
                for (String[] booking : bookings) {
                    if (booking[2].equals(scheduleId) && booking[3].equals("not available")) {
                        isAvailable = false;
                        break;
                    }
                }

                // Display only available offerings
                if (isAvailable) {
                    System.out.println("ID: " + schedule[0] + ", Location: " + schedule[1] +
                            ", Lesson Type: " + schedule[2] + ", Day: " + schedule[3] +
                            ", Time Slot: " + schedule[4]);
                }
            }
        } catch (IOException e) {
            System.err.println("Error displaying available offerings: " + e.getMessage());
        }
    }
}

