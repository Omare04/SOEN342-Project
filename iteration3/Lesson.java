// Lesson.java
public class Lesson {
    private String lessonId;
    private boolean available;

    public Lesson(String lessonId) {
        this.lessonId = lessonId;
        this.available = true;
    }

    public String getLessonId() {
        return lessonId;
    }

    public boolean isAvailable() {
        return available;
    }

    public void setAvailable(boolean available) {
        this.available = available;
    }
}


