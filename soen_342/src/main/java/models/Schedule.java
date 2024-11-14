package src.main.java.models;

public class Schedule {
    private int id;
    private String location;
    private String lessonType;
    private String day;
    private String timeSlot;

    public Schedule(int id, String location, String lessonType, String day, String timeSlot) {
        this.id = id;
        this.location = location;
        this.lessonType = lessonType;
        this.day = day;
        this.timeSlot = timeSlot;
    }

    // Getters and Setters
}

