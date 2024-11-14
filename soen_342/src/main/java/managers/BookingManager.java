package src.main.java.managers;

import src.main.java.models.Booking;

import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class BookingManager {
    private static final String BOOKINGS_FILE = "src/data/Bookings.csv";

    public void makeBooking(int id, int clientId, int scheduleId) {
        Booking booking = new Booking(id, clientId, scheduleId, "not available");
        try {
            // Convert data to CSV format and write it as a single row
            CSVManager.writeCSV(BOOKINGS_FILE, Collections.singletonList(new String[]{
                    String.valueOf(id), String.valueOf(clientId), String.valueOf(scheduleId), "not available"
            }));
            System.out.println("Booking made successfully.");
        } catch (IOException e) {
            System.err.println("Error making booking: " + e.getMessage());
        }
        }

    public List<Booking> loadBookings() {
        List<Booking> bookings = new ArrayList<>();
        try {
            List<String[]> records = CSVManager.readCSV(BOOKINGS_FILE);
            for (String[] record : records) {
                int id = Integer.parseInt(record[0]);
                int clientId = Integer.parseInt(record[1]);
                int scheduleId = Integer.parseInt(record[2]);
                String status = record[3];
                bookings.add(new Booking(id, clientId, scheduleId, status));
            }
        } catch (IOException e) {
            System.err.println("Error loading bookings: " + e.getMessage());
        }
        return bookings;
    }

    public void cancelBooking(int bookingId) {
        List<Booking> bookings = loadBookings();
        boolean bookingFound = false;

        // Update booking status to available
        for (Booking booking : bookings) {
            if (booking.getId() == bookingId) {
                booking.setStatus("available");
                bookingFound = true;
                break;
            }
        }

        // Rewrite updated bookings to CSV
        if (bookingFound) {
            try {
                List<String[]> updatedData = new ArrayList<>();
                for (Booking booking : bookings) {
                    updatedData.add(new String[]{
                            String.valueOf(booking.getId()), String.valueOf(booking.getClientId()),
                            String.valueOf(booking.getScheduleId()), booking.getStatus()
                    });
                }
                CSVManager.writeCSV(BOOKINGS_FILE, updatedData);
                System.out.println("Booking canceled successfully.");
            } catch (IOException e) {
                System.err.println("Error canceling booking: " + e.getMessage());
            }
        } else {
            System.out.println("Booking not found.");
        }
    }
}
