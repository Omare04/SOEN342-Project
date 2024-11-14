package src.main.java.models;


public class Lesson {
    private int id;
    private String lessonType; // e.g., Yoga, Swimming, Judo
    private String mode;       // "Private" or "Group"
    private int duration;      // Duration in minutes

    public Lesson(int id, String lessonType, String mode, int duration) {
        this.id = id;
        this.lessonType = lessonType;
        this.mode = mode;
        this.duration = duration;
    }

    public int getId() {
        return id;
    }

    public String getLessonType() {
        return lessonType;
    }

    public String getMode() {
        return mode;
    }

    public int getDuration() {
        return duration;
    }

    @Override
    public String toString() {
        return "Lesson{" +
                "id=" + id +
                ", lessonType='" + lessonType + '\'' +
                ", mode='" + mode + '\'' +
                ", duration=" + duration +
                '}';
    }
}

