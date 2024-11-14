package src.main.java.models;

import java.util.List;

public class Instructor {
    private int id;
    private String name;
    private String phoneNumber;
    private String specialization;
    private List<String> availableCities;

    public Instructor(int id, String name, String phoneNumber, String specialization, List<String> availableCities) {
        this.id = id;
        this.name = name;
        this.phoneNumber = phoneNumber;
        this.specialization = specialization;
        this.availableCities = availableCities;
    }

    // Getters and Setters
}
