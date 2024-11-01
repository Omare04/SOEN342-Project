public class Client {
    private String name;
    private int age;
    private Guardian guardian; // Optional, for minors

    public Client(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public String getName() {
        return name;
    }

    public int getAge() {
        return age;
    }

    public void setGuardian(Guardian guardian) {
        this.guardian = guardian;
    }

    public Guardian getGuardian() {
        return guardian;
    }
}

