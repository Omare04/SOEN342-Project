public class BookingSystem {
    private Map<String, Client> clients;
    private Map<String, Lesson> lessons;
    private Map<String, Booking> bookings;
    private Map<String, Guardian> guardians;

    public BookingSystem() {
        this.clients = new HashMap<>();
        this.lessons = new HashMap<>();
        this.bookings = new HashMap<>();
        this.guardians = new HashMap<>();
    }

    public Client registerClient(String name, int age) {
        Client client = new Client(name, age);
        clients.put(name, client);
        return client;
    }

    public Booking bookLesson(Client client, String lessonId) {
        // Check preconditions
        if (!clients.containsValue(client)) {
            throw new IllegalArgumentException("Client is not registered in the system");
        }

        Lesson lesson = lessons.get(lessonId);
        if (lesson == null || !lesson.isAvailable()) {
            throw new IllegalArgumentException("Lesson is not available");
        }

        // Create booking
        String bookingId = UUID.randomUUID().toString();
        Booking booking = new Booking(bookingId, client, lesson);
        bookings.put(bookingId, booking);

        // Update lesson availability
        lesson.setAvailable(false);

        return booking;
    }

    public void cancelBooking(Client client, String bookingId) {
        // Check preconditions
        Booking booking = bookings.get(bookingId);
        if (booking == null || !booking.getClient().equals(client)) {
            throw new IllegalArgumentException("Invalid booking or booking doesn't belong to client");
        }

        // Update lesson availability
        booking.getLesson().setAvailable(true);

        // Remove booking
        bookings.remove(bookingId);
    }

    public void registerGuardian(String guardianName, String minorName, int minorAge) {
        // Create guardian if not exists
        Guardian guardian = guardians.computeIfAbsent(guardianName, Guardian::new);

        // Register minor as client
        Client minor = registerClient(minorName, minorAge);
        
        // Associate minor with guardian
        guardian.addMinor(minor);
        minor.setGuardian(guardian);
    }

    // Helper methods to manage lessons
    public void addLesson(String lessonId) {
        lessons.put(lessonId, new Lesson(lessonId));
    }

    public boolean isLessonAvailable(String lessonId) {
        Lesson lesson = lessons.get(lessonId);
        return lesson != null && lesson.isAvailable();
    }
}