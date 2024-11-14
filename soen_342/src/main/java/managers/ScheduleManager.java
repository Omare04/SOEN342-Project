package src.main.java.managers;

import src.main.java.models.Schedule;

import java.io.IOException;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class ScheduleManager {
    private static final String SCHEDULES_FILE = "src/data/Schedules.csv";

    public void createSchedule(int id, String location, String lessonType, String day, String timeSlot) {
        Schedule schedule = new Schedule(id, location, lessonType, day, timeSlot);
        try {
            // Convert data to CSV format and write it as a single row
            CSVManager.writeCSV(SCHEDULES_FILE, Collections.singletonList(new String[]{
                    String.valueOf(id), location, lessonType, day, timeSlot
            }));
            System.out.println("Schedule created successfully.");
        } catch (IOException e) {
            System.err.println("Error creating schedule: " + e.getMessage());
        }
    }
}
