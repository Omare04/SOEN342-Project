package src.main.java.managers;

import src.main.java.models.Instructor;

import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class InstructorManager {
    private static final String INSTRUCTORS_FILE = "src/data/Instructors.csv";

    public void registerInstructor(int id, String name, String phone, String specialization, List<String> cities) {
        Instructor instructor = new Instructor(id, name, phone, specialization, cities);
        try {
            // Convert data to CSV format and write it as a single row
            CSVManager.writeCSV(INSTRUCTORS_FILE, Collections.singletonList(new String[]{
                    String.valueOf(id), name, phone, specialization, String.join(";", cities)
            }));
            System.out.println("Instructor registered successfully.");
        } catch (IOException e) {
            System.err.println("Error registering instructor: " + e.getMessage());
        }
    }


    public List<Instructor> loadInstructors() {
        List<Instructor> instructors = new ArrayList<>();
        try {
            List<String[]> records = CSVManager.readCSV(INSTRUCTORS_FILE);
            for (String[] record : records) {
                int id = Integer.parseInt(record[0]);
                String name = record[1];
                String phone = record[2];
                String specialization = record[3];
                List<String> cities = Arrays.asList(record[4].split(";"));
                instructors.add(new Instructor(id, name, phone, specialization, cities));
            }
        } catch (IOException e) {
            System.err.println("Error loading instructors: " + e.getMessage());
        }
        return instructors;
    }
}

