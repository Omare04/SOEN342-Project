package src.main.java.models;

public class Booking {
    private int id;
    private int clientId;
    private int scheduleId;
    private String status; // e.g., "available" or "not available"

    public Booking(int id, int clientId, int scheduleId, String status) {
        this.id = id;
        this.clientId = clientId;
        this.scheduleId = scheduleId;
        this.status = status;
    }

    // Getters and Setters

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public int getClientId() {
        return clientId;
    }

    public void setClientId(int clientId) {
        this.clientId = clientId;
    }

    public int getScheduleId() {
        return scheduleId;
    }

    public void setScheduleId(int scheduleId) {
        this.scheduleId = scheduleId;
    }

    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }
}
