package src.main.java.managers;



import src.main.java.models.Lesson;

import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class LessonManager {
    private static final String LESSONS_FILE = "src/data/Lessons.csv";

    public void createLesson(int id, String lessonType, String mode, int duration) {
        Lesson lesson = new Lesson(id, lessonType, mode, duration);
        try {
            // Convert data to CSV format and write it as a single row
            CSVManager.writeCSV(LESSONS_FILE, Collections.singletonList(new String[]{
                    String.valueOf(id), lessonType, mode, String.valueOf(duration)
            }));
            System.out.println("Lesson created successfully.");
        } catch (IOException e) {
            System.err.println("Error creating lesson: " + e.getMessage());
        }
    }

    public List<Lesson> loadLessons() {
        List<Lesson> lessons = new ArrayList<>();
        try {
            List<String[]> records = CSVManager.readCSV(LESSONS_FILE);
            for (String[] record : records) {
                int id = Integer.parseInt(record[0]);
                String lessonType = record[1];
                String mode = record[2];
                int duration = Integer.parseInt(record[3]);
                lessons.add(new Lesson(id, lessonType, mode, duration));
            }
        } catch (IOException e) {
            System.err.println("Error loading lessons: " + e.getMessage());
        }
        return lessons;
    }
}

