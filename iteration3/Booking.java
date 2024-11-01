public class Booking {
    private String bookingId;
    private Client client;
    private Lesson lesson;

    public Booking(String bookingId, Client client, Lesson lesson) {
        this.bookingId = bookingId;
        this.client = client;
        this.lesson = lesson;
    }

    public String getBookingId() {
        return bookingId;
    }

    public Client getClient() {
        return client;
    }

    public Lesson getLesson() {
        return lesson;
    }
}