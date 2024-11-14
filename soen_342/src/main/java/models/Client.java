package src.main.java.models;

public class Client {
    private int id;
    private String name;
    private int age;
    private Integer guardianId; // Null if not underage

    public Client(int id, String name, int age, Integer guardianId) {
        this.id = id;
        this.name = name;
        this.age = age;
        this.guardianId = guardianId;
    }

    public boolean isUnderage() {
        return age < 18;
    }

    // Getters and Setters
}

